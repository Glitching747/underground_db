import json
import os
import random
import re
from urllib.parse import parse_qs, quote, urlencode, urlparse

from flask import Flask, abort, redirect, render_template, request, send_from_directory, url_for
from jinja2 import DictLoader
from werkzeug.middleware.proxy_fix import ProxyFix

import database

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGES_DIR = os.path.join(BASE_DIR, "images")

app = Flask(__name__)

app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1) 



# ---------------------------------------------------------------- images

@app.route("/images/<path:filename>")
def image(filename):
    return send_from_directory(IMAGES_DIR, filename)


def has_image(filename):
    """False for a blank name or a file that isn't in images/ yet."""
    if not filename:
        return False
    return os.path.isfile(os.path.join(IMAGES_DIR, filename))


app.jinja_env.globals["has_image"] = has_image


# ---------------------------------------------------------------- name-linking helpers
#
# Turn a plain name (a collective member, a producer credit) into a URL if it
# matches an existing artist page — used directly from the templates.

def artist_link(name):
    match = database.find_artist_by_name(name)
    return url_for("artist", slug=match["slug"]) if match else None


def collective_link(name):
    match = database.find_collective_by_name(name)
    return url_for("collective", slug=match["slug"]) if match else None


def producer_link(name):
    """Where a producer credit should point: their own artist page (in
    Producer mode) if they have one, otherwise a plain producer credit page."""
    match = database.find_artist_by_name(name)
    if match:
        return url_for("artist", slug=match["slug"]) + "?mode=producer"
    return url_for("producer", slug=database.slugify(name))


def member_link(name):
    """For a collective member: link to their artist page if they have one,
    otherwise to their producer credits page — but only if they're actually
    a credited producer. Unlike producer_link() (used where the name is
    already known to be a real credit), this returns None rather than
    guessing a URL for a name that isn't a producer at all."""
    match = database.find_artist_by_name(name)
    if match:
        return url_for("artist", slug=match["slug"])
    entry = database.get_producer(database.slugify(name))
    return url_for("producer", slug=entry["slug"]) if entry else None


def artist_hover_info(name):
    """Small artist-page summary used by feature/producer hover cards."""
    match = database.find_artist_by_name(name)
    if not match:
        return None
    projects = match.get("projects") or []
    singles = match.get("singles") or []
    song_count = len(singles) + sum(len(p.get("tracks") or []) for p in projects)
    return {
        "name": match["name"],
        "image": match.get("image") or "",
        "projects": len(projects),
        "songs": song_count,
        "url": url_for("artist", slug=match["slug"]),
    }


app.jinja_env.globals["artist_link"] = artist_link
app.jinja_env.globals["artist_hover_info"] = artist_hover_info
app.jinja_env.globals["collective_link"] = collective_link
app.jinja_env.globals["producer_link"] = producer_link
app.jinja_env.globals["member_link"] = member_link


# ---------------------------------------------------------------- playback links
#
# A SoundCloud link (on a single, a track, or a whole project) renders as a
# playable embed right on the page. Anything else — YouTube Music, a YouTube
# playlist, whatever — just becomes a "Play now" link that opens elsewhere.

def is_soundcloud(url):
    return bool(url) and "soundcloud.com" in url.lower()


def soundcloud_embed_src(url):
    return (
        "https://w.soundcloud.com/player/?url=" + quote(url, safe="")
        + "&color=%23ff0000&auto_play=false&hide_related=true"
        + "&show_comments=true&show_user=true&show_reposts=false"
        + "&show_teaser=false&visual=false"
    )

app.jinja_env.globals["is_soundcloud"] = is_soundcloud
app.jinja_env.globals["soundcloud_embed_src"] = soundcloud_embed_src


def _extract_youtube_src(url):
    """If url is a whole <iframe> tag, pull out its src attribute; otherwise
    return url unchanged. Returns None if given an iframe with no src."""
    if not url:
        return None
    if "<iframe" in url:
        match = re.search(r'src=["\']([^"\']+)["\']', url)
        return match.group(1) if match else None
    return url


def youtube_video_id(url):
    """Pull the 11-character video ID out of any common YouTube link shape
    (watch?v=, youtu.be/, /shorts/, /embed/, music.youtube.com watch links) —
    or out of the whole <iframe> snippet YouTube's own Share > Embed gives
    you, if that's what got pasted in instead of a plain link.
    Returns None if nothing recognizable as a single YouTube video is found."""
    raw = _extract_youtube_src(url)
    if not raw:
        return None

    try:
        parsed = urlparse(raw)
    except ValueError:
        return None

    host = (parsed.netloc or "").lower()
    if "youtu.be" in host:
        vid = parsed.path.strip("/").split("/")[0]
        return vid or None

    if "youtube.com" in host:
        query = parse_qs(parsed.query)
        if "v" in query and query["v"][0]:
            return query["v"][0]
        parts = [p for p in parsed.path.split("/") if p]
        if len(parts) >= 2 and parts[0] in ("embed", "shorts", "live"):
            return parts[1]

    return None


def youtube_embed_src(url):
    """Build the /embed/ URL for this video, carrying over any extra query
    params (like YouTube's own "si" share token, or a start time) from
    whatever link or <iframe> was pasted in — the goal is to reproduce
    exactly what YouTube's own Share > Embed gives you, not a stripped-down
    version of it."""
    vid = youtube_video_id(url)
    if not vid:
        return None

    raw = _extract_youtube_src(url)
    try:
        query = parse_qs(urlparse(raw).query)
    except ValueError:
        query = {}
    query.pop("v", None)
    query.pop("list", None)

    extra = urlencode(query, doseq=True)
    return f"https://www.youtube.com/embed/{vid}" + (f"?{extra}" if extra else "")


app.jinja_env.globals["youtube_video_id"] = youtube_video_id
app.jinja_env.globals["youtube_embed_src"] = youtube_embed_src


_IFRAME_TAG_RE = re.compile(r"<iframe.*?</iframe>", re.I | re.S)


def split_music_videos(value):
    """One music_video field can hold more than one video — either several
    plain links separated by spaces, or full pasted <iframe> embed codes
    (which have spaces inside their own attributes, so those are pulled out
    as whole blocks first rather than being split apart). Mixing both in one
    field works too."""
    if not value:
        return []
    text = str(value)
    iframe_blocks = _IFRAME_TAG_RE.findall(text)
    remainder = _IFRAME_TAG_RE.sub(" ", text)
    plain_links = remainder.split()
    return iframe_blocks + plain_links


app.jinja_env.globals["split_music_videos"] = split_music_videos



# ---------------------------------------------------------------- search indexes
#
# JSON blobs handed to the page so the search box can filter client-side with
# no extra requests. The home page gets everything (artists, producers, every
# track and single); an artist page gets only that one artist's own tracks
# and singles.

def _safe_json(data):
    """json.dumps, but safe to drop inside a <script> tag even if some
    title happens to contain '</script' — escapes the slash so it can't
    close the tag early."""
    return json.dumps(data).replace("</", "<\\/")


def _canonical_url(artist, canon):
    """Turn a database.py canonical descriptor into an actual URL."""
    if canon["type"] == "single":
        return url_for("single", slug=artist["slug"], single_slug=canon["slug"])
    return url_for("track", slug=artist["slug"], project_slug=canon["project_slug"], track_slug=canon["track_slug"])


def build_track_hrefs(artist, collab_projects=None):
    """The href to use for every track/single belonging to this artist —
    its own page normally, or the canonical page for that song if this
    occurrence is a duplicate (a deluxe track already on the original
    album, or an album track that's also its own single). Also covers
    tracks on any collab projects cross-listed here from another artist's
    page, resolved against that project's actual owner."""
    canonical = database.build_canonical_track_map(artist)
    hrefs = {}

    for s in artist["singles"]:
        own = url_for("single", slug=artist["slug"], single_slug=s["slug"])
        is_canon = database._is_canonical_single(canonical, s["title"], s["slug"])
        hrefs[f"single:{s['slug']}"] = own if is_canon else _canonical_url(artist, canonical[database.name_key(s["title"])])

    for p in artist["projects"]:
        for t in p["tracks"]:
            own = url_for("track", slug=artist["slug"], project_slug=p["slug"], track_slug=t["slug"])
            is_canon = database._is_canonical_track(canonical, t["title"], p["slug"], t["index"])
            hrefs[f"track:{p['slug']}:{t['index']}"] = own if is_canon else _canonical_url(artist, canonical[database.name_key(t["title"])])

    for cp in (collab_projects or []):
        owner = database.get_artist(cp["owner_slug"])
        if not owner:
            continue
        owner_canonical = database.build_canonical_track_map(owner)
        for t in cp["tracks"]:
            own = url_for("track", slug=owner["slug"], project_slug=cp["slug"], track_slug=t["slug"])
            is_canon = database._is_canonical_track(owner_canonical, t["title"], cp["slug"], t["index"])
            hrefs[f"track:{cp['slug']}:{t['index']}"] = own if is_canon else _canonical_url(owner, owner_canonical[database.name_key(t["title"])])

    return hrefs


def _credit_suffix(features, producers):
    """Featuring/Produced by parts for a search result's sub-label, features
    first — e.g. ["Featuring OsamaSon", "Produced by CXO"]."""
    parts = []
    if features:
        parts.append("Featuring " + ", ".join(features))
    if producers:
        parts.append("Produced by " + ", ".join(producers))
    return parts


def build_search_index():
    artist_entries = []
    producer_entries = []
    track_single_entries = []

    for a in database.get_artists():
        artist_entries.append({
            "type": "artist",
            "title": a["name"],
            "sub": ("AKA / FKA: " + ", ".join(a["aliases"])) if a["aliases"] else "Artist",
            "url": url_for("artist", slug=a["slug"]),
        })
        canonical = database.build_canonical_track_map(a)
        for p in a["projects"]:
            for t in p["tracks"]:
                if not database._is_canonical_track(canonical, t["title"], p["slug"], t["index"]):
                    continue
                sub = " · ".join([a["name"], p["title"]] + _credit_suffix(t["features"], t["producers"]))
                track_single_entries.append({
                    "type": "track",
                    "title": t["title"],
                    "sub": sub,
                    "url": url_for("track", slug=a["slug"], project_slug=p["slug"], track_slug=t["slug"]),
                })
        for s in a["singles"]:
            if not database._is_canonical_single(canonical, s["title"], s["slug"]):
                continue
            sub = " · ".join([a["name"], "Single"] + _credit_suffix(s["features"], s["producers"]))
            track_single_entries.append({
                "type": "single",
                "title": s["title"],
                "sub": sub,
                "url": url_for("single", slug=a["slug"], single_slug=s["slug"]),
            })

    for entry in database.build_producer_index().values():
        count = len(entry["credits"])
        if entry["artist_match"]:
            link = url_for("artist", slug=entry["artist_match"]["slug"]) + "?mode=producer"
        else:
            link = url_for("producer", slug=entry["slug"])
        producer_entries.append({
            "type": "producer",
            "title": entry["name"],
            "sub": f"Producer · {count} credit{'' if count == 1 else 's'}",
            "url": link,
        })

    # Artists first, then producers, then tracks/singles — matches search
    # results are grouped in this order rather than interleaved.
    return artist_entries + producer_entries + track_single_entries


def build_artist_track_index(person, featured_singles=None, collab_projects=None):
    entries = []
    canonical = database.build_canonical_track_map(person)
    for p in person["projects"]:
        for t in p["tracks"]:
            if not database._is_canonical_track(canonical, t["title"], p["slug"], t["index"]):
                continue
            entries.append({
                "type": "track",
                "title": t["title"],
                "sub": p["title"],
                "url": url_for("track", slug=person["slug"], project_slug=p["slug"], track_slug=t["slug"]),
            })
    for s in person["singles"]:
        if not database._is_canonical_single(canonical, s["title"], s["slug"]):
            continue
        entries.append({
            "type": "single",
            "title": s["title"],
            "sub": "Single",
            "url": url_for("single", slug=person["slug"], single_slug=s["slug"]),
        })
    for s in (featured_singles or []):
        entries.append({
            "type": "single",
            "title": s["title"],
            "sub": "featured on " + s["owner_name"],
            "url": url_for("single", slug=s["owner_slug"], single_slug=s["slug"]),
        })
    for p in (collab_projects or []):
        for t in p["tracks"]:
            entries.append({
                "type": "track",
                "title": t["title"],
                "sub": "collab on " + p["owner_name"] + "'s " + p["title"],
                "url": url_for("track", slug=p["owner_slug"], project_slug=p["slug"], track_slug=t["slug"]),
            })
    return entries


def build_newest_releases():
    items = database.get_newest_releases(limit=3)
    for item in items:
        if item["is_single"]:
            item["url"] = url_for("single", slug=item["artist_slug"], single_slug=item["slug"])
        else:
            item["url"] = url_for("project", slug=item["artist_slug"], project_slug=item["slug"])
    return items


def build_top_producers():
    entries = database.get_top_producers(limit=5)
    results = []
    for entry in entries:
        if entry["artist_match"]:
            url = url_for("artist", slug=entry["artist_match"]["slug"]) + "?mode=producer"
        else:
            url = url_for("producer", slug=entry["slug"])
        results.append({
            "name": entry["name"],
            "url": url,
            "credit_count": len(entry["credits"]),
        })
    return results


# ---------------------------------------------------------------- routes

@app.route("/")
def index():
    return render_template(
        "index.html",
        artists=database.get_artists(),
        track_count=database.get_total_track_count(),
        search_index=_safe_json(build_search_index()),
        newest_releases=build_newest_releases(),
        top_producers=build_top_producers(),
    )


def sort_by_date(items):
    """Oldest-first by "year" (handles a bare year or a full date, however
    it's typed — see database.year_sort_key)."""
    return sorted(items, key=lambda i: database.year_sort_key(i.get("year")))


@app.route("/random-song")
def random_song():
    # Use the same canonical track/single list as search, so duplicate
    # album/single listings do not make the same song appear multiple times.
    # Singles Only is a browser setting, so the random endpoint reads the
    # setting from a query parameter supplied by the random-song button.
    singles_only = request.args.get("singles_only") == "1"
    if singles_only:
        songs = [entry for entry in build_search_index() if entry["type"] == "single"]
    else:
        songs = [entry for entry in build_search_index() if entry["type"] in ("track", "single")]
    if not songs:
        abort(404)
    return redirect(random.choice(songs)["url"])


def build_playable_songs():
    """Every canonical track/single that has a SoundCloud link, keyed by its
    site page. The player uses this to name queued songs, decorate tracklists
    with queue buttons, and pick something to play next."""
    songs = []
    for a in database.get_artists():
        canonical = database.build_canonical_track_map(a)
        for p in a["projects"]:
            for t in p["tracks"]:
                if not is_soundcloud(t.get("url")):
                    continue
                if not database._is_canonical_track(canonical, t["title"], p["slug"], t["index"]):
                    continue
                songs.append({
                    "cover": url_for("image", filename=p["cover"]) if has_image(p.get("cover")) else "",
                    "href": url_for("track", slug=a["slug"], project_slug=p["slug"], track_slug=t["slug"]),
                    "url": t["url"], "title": t["title"],
                    "sub": a["name"] + " \u00b7 " + p["title"], "artist_slug": a["slug"],
                })
        for sg in a["singles"]:
            if not is_soundcloud(sg.get("url")):
                continue
            if not database._is_canonical_single(canonical, sg["title"], sg["slug"]):
                continue
            songs.append({
                "cover": url_for("image", filename=sg["cover"]) if has_image(sg.get("cover")) else "",
                "href": url_for("single", slug=a["slug"], single_slug=sg["slug"]),
                "url": sg["url"], "title": sg["title"],
                "sub": a["name"] + " \u00b7 Single", "artist_slug": a["slug"],
            })
    return songs


@app.route("/api/playable")
def api_playable():
    return {"songs": build_playable_songs()}


@app.route("/artist/<slug>")
def artist(slug):
    person = database.get_artist(slug)
    if person is None:
        abort(404)
    producer_credits = database.get_producer_credits_for_artist(person)
    featured_singles = database.get_featured_singles(person)
    collab_projects = database.get_collab_projects(person)
    start_mode = "producer" if request.args.get("mode") == "producer" and producer_credits else "artist"

    sorted_projects = sort_by_date(list(person["projects"]) + list(collab_projects))
    sorted_singles = sort_by_date(list(person["singles"]) + list(featured_singles))

    return render_template(
        "artist.html",
        artist=person,
        producer_credits=producer_credits,
        featured_singles=featured_singles,
        collab_projects=collab_projects,
        sorted_projects=sorted_projects,
        sorted_singles=sorted_singles,
        start_mode=start_mode,
        track_index=_safe_json(build_artist_track_index(person, featured_singles, collab_projects)),
        track_hrefs=build_track_hrefs(person, collab_projects),
    )


@app.route("/artist/<slug>/<project_slug>")
def project(slug, project_slug):
    person = database.get_artist(slug)
    if person is None:
        abort(404)
    record = database.get_project(person, project_slug)
    if record is None:
        abort(404)
    return render_template(
        "project.html", artist=person, project=record, track_hrefs=build_track_hrefs(person)
    )


@app.route("/artist/<slug>/<project_slug>/<track_slug>")
def track(slug, project_slug, track_slug):
    person = database.get_artist(slug)
    if person is None:
        abort(404)
    record = database.get_project(person, project_slug)
    if record is None:
        abort(404)
    the_track = next((t for t in record["tracks"] if t["slug"] == track_slug), None)
    if the_track is None:
        abort(404)
    return render_template(
        "track.html", artist=person, project=record, track=the_track,
    )


@app.route("/artist/<slug>/single/<single_slug>")
def single(slug, single_slug):
    person = database.get_artist(slug)
    if person is None:
        abort(404)
    record = database.get_single(person, single_slug)
    if record is None:
        abort(404)
    return render_template(
        "single.html", artist=person, single=record,
    )



@app.route("/collective/<slug>")
def collective(slug):
    record = database.get_collective(slug)
    if record is None:
        abort(404)
    return render_template("collective.html", collective=record)


@app.route("/producer/<slug>")
def producer(slug):
    record = database.get_producer(slug)
    if record is None:
        abort(404)
    return render_template("producer.html", producer=record)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/content-warning")
def content_warning():
    return render_template("content-warning.html")


@app.errorhandler(404)
def not_found(_):
    return render_template("404.html"), 404


# ---------------------------------------------------------------- templates

LAYOUT = """
<!doctype html>
<html lang="en">
<head><script src="https://cdn.tailwindcss.com"></script>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="color-scheme" content="light dark">
<meta name="theme-color" content="#EDE7DC">
<script>
  (function(){
    try {
      var savedTheme = localStorage.getItem('undergroundCatalogTheme');
      document.documentElement.classList.toggle('dark', savedTheme === 'dark');
      document.documentElement.classList.toggle('light', savedTheme !== 'dark');
    } catch(e) {
      document.documentElement.classList.add('light');
    }
  })();
</script>
<title>{% block title %}Underground Catalog{% endblock %}</title>
<link rel="icon" type="image/x-icon" href="{{url_for('static', filename='wtf do u think dis is.ico')}}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Archivo:wght@400;500;600&family=Archivo+Black&display=swap" rel="stylesheet">
<style>
:root{
  --paper:#EDE7DC;
  --ink:#16130F;
  --red:#E1341E;
  --blue:#1B4AA0;
  --mute:#8A8275;
  --rule:rgba(22,19,15,.18);
  --button-bg:#16130F;
  --button-fg:#EDE7DC;
  --radius-2xl:1rem;
  --shadow-deep:0 25px 50px -12px rgba(22,19,15,.28),0 12px 24px -10px rgba(22,19,15,.14);
  --shadow-card:0 20px 40px -18px rgba(22,19,15,.22),0 8px 16px -8px rgba(22,19,15,.12);
  --shadow-float:0 16px 32px -12px rgba(22,19,15,.2);
  --border-soft:rgba(22,19,15,.1);
  --surface:rgba(255,255,255,.42);
  --surface-focus:rgba(255,255,255,.62);
}
html{
  color-scheme:light;
  --paper:#EDE7DC;
  --ink:#16130F;
  --red:#E1341E;
  --blue:#1B4AA0;
  --mute:#8A8275;
  --rule:rgba(22,19,15,.18);
  --button-bg:#16130F;
  --button-fg:#EDE7DC;
}
html.light{
  color-scheme:light;
  --paper:#EDE7DC !important;
  --ink:#16130F !important;
  --red:#E1341E !important;
  --blue:#1B4AA0 !important;
  --mute:#8A8275 !important;
  --rule:rgba(22,19,15,.18) !important;
  --button-bg:#16130F !important;
  --button-fg:#EDE7DC !important;
}
html.dark{
  color-scheme:dark;
  --paper:#11110F !important;
  --ink:#F2EEE5 !important;
  --red:#FF4A32 !important;
  --blue:#5D8CFF !important;
  --mute:#AAA49A !important;
  --rule:rgba(242,238,229,.20) !important;
  --button-bg:#F2EEE5 !important;
  --button-fg:#11110F !important;
  --shadow-deep:0 28px 56px -14px rgba(0,0,0,.55),0 14px 28px -12px rgba(0,0,0,.35);
  --shadow-card:0 22px 44px -20px rgba(0,0,0,.5),0 10px 20px -10px rgba(0,0,0,.35);
  --shadow-float:0 18px 36px -14px rgba(0,0,0,.45);
  --border-soft:rgba(242,238,229,.12);
  --surface:rgba(255,255,255,.06);
  --surface-focus:rgba(255,255,255,.1);
}
*{box-sizing:border-box}
html{-webkit-text-size-adjust:100%;}
body{
  margin:0;
  min-height:100vh;
  display:flex;
  flex-direction:column;
  background-color:var(--paper) !important;
  background:var(--paper) !important;
  color:var(--ink) !important;
  font-family:Archivo,"Helvetica Neue",Arial,sans-serif;
  font-size:17px;
  line-height:1.55;
  transition:background-color .3s ease,color .3s ease;
}
body::before{
  content:"";position:fixed;inset:0;pointer-events:none;z-index:0;
  background:
    radial-gradient(ellipse 80% 50% at 20% -10%,rgba(27,74,160,.08),transparent 55%),
    radial-gradient(ellipse 60% 40% at 100% 0%,rgba(225,52,30,.06),transparent 50%);
  opacity:1;
  transition:opacity .3s ease;
}
html.dark body::before{
  background:
    radial-gradient(ellipse 80% 50% at 20% -10%,rgba(93,140,255,.12),transparent 55%),
    radial-gradient(ellipse 60% 40% at 100% 0%,rgba(255,74,50,.08),transparent 50%);
}
.page{position:relative;z-index:1;max-width:1040px;width:100%;margin:0 auto;padding:0 28px 96px;flex:1}
a{color:inherit}
.site-footer{
  position:relative;z-index:1;
  width:100%;
  padding:0 28px 24px;
  text-align:center;
  font-size:13px;
}
.site-footer a{
  color:var(--mute);
  text-decoration:none;
  border-bottom:1px solid transparent;
  margin:0 7px;
}
.site-footer a:hover{color:var(--blue);border-color:var(--blue)}
.site-footer .footer-separator{color:var(--mute)}
.info-page{max-width:760px}
.info-page h1{font-size:clamp(36px,6vw,58px);margin-bottom:26px}
.info-page h2{font-size:clamp(24px,4vw,34px);margin:28px 0 12px}
.info-page p{max-width:72ch;margin:0 0 18px}
.info-page .warning-note{border:1px solid var(--border-soft);border-radius:var(--radius-2xl);padding:24px 26px;margin-top:8px;background:var(--surface);box-shadow:var(--shadow-card);transition:all .3s ease}
.info-page .warning-note p:last-child{margin-bottom:0}
h1,h2,h3{font-family:"Archivo Black",Archivo,sans-serif;font-weight:400;letter-spacing:-.02em;margin:0}

/* light / dark mode */
.theme-toggle{
  position:fixed;
  top:14px;
  left:14px;
  z-index:1000;
  width:44px;
  height:44px;
  padding:0;
  display:flex;
  align-items:center;
  justify-content:center;
  border:1px solid var(--border-soft);
  border-radius:var(--radius-2xl);
  background:var(--button-bg);
  color:var(--button-fg);
  font-family:Arial,sans-serif;
  font-size:23px;
  line-height:1;
  cursor:pointer;
  box-shadow:var(--shadow-float);
  transition:all .3s ease;
}
.theme-toggle:hover{transform:translateY(-2px);box-shadow:var(--shadow-deep)}
.theme-toggle:active{transform:translateY(0);box-shadow:var(--shadow-card)}
.theme-toggle:focus-visible{outline:3px solid var(--blue);outline-offset:3px}
.theme-toggle .sun{display:none}
html.dark .theme-toggle .moon{display:none}
html.dark .theme-toggle .sun{display:inline}


.random-song-button{
  position:fixed;
  top:68px;
  left:14px;
  z-index:1000;
  width:44px;
  height:44px;
  padding:0;
  display:flex;
  align-items:center;
  justify-content:center;
  border:1px solid var(--border-soft);
  border-radius:var(--radius-2xl);
  background:var(--button-bg);
  color:var(--button-fg);
  font-family:Arial,sans-serif;
  font-size:23px;
  line-height:1;
  cursor:pointer;
  box-shadow:var(--shadow-float);
  text-decoration:none;
  transition:all .3s ease;
}
.random-song-button:hover{transform:translateY(-2px);box-shadow:var(--shadow-deep)}
.random-song-button:active{transform:translateY(0);box-shadow:var(--shadow-card)}
.random-song-button:focus-visible{outline:3px solid var(--blue);outline-offset:3px}

.settings-button{
  position:fixed;top:122px;left:14px;z-index:1000;width:44px;height:44px;
  padding:0;display:flex;align-items:center;justify-content:center;
  border:1px solid var(--border-soft);border-radius:var(--radius-2xl);
  background:var(--button-bg);color:var(--button-fg);
  font-family:Arial,sans-serif;font-size:23px;line-height:1;cursor:pointer;
  box-shadow:var(--shadow-float);
  transition:all .3s ease;
}
.settings-button:hover{transform:translateY(-2px);box-shadow:var(--shadow-deep)}
.settings-button:active{transform:translateY(0);box-shadow:var(--shadow-card)}
.settings-button:focus-visible{outline:3px solid var(--blue);outline-offset:3px}
.settings-backdrop{position:fixed;inset:0;z-index:1090;background:rgba(0,0,0,.45);backdrop-filter:blur(4px);transition:all .3s ease}
.settings-backdrop[hidden]{display:none}
.settings-menu{
  position:fixed;top:122px;left:68px;z-index:1100;
  width:min(390px,calc(100vw - 84px));border:1px solid var(--border-soft);
  border-radius:var(--radius-2xl);
  background:var(--paper);color:var(--ink);box-shadow:var(--shadow-deep);padding:22px;
  transition:all .3s ease;
}
.settings-menu[hidden]{display:none}
.settings-head{display:flex;align-items:center;justify-content:space-between;gap:16px;margin-bottom:18px}
.settings-head h2{font-size:24px}
.settings-close{border:0;background:transparent;color:var(--ink);font-size:26px;line-height:1;cursor:pointer;padding:0 2px}
.settings-close:focus-visible{outline:3px solid var(--blue);outline-offset:3px}
.setting{padding:16px 0;border-top:1px solid var(--rule)}
.setting:first-of-type{border-top:0;padding-top:0}
.setting-title{font-weight:600;font-size:15px;margin:0 0 10px}
.setting-options{display:inline-flex;border:1px solid var(--border-soft);border-radius:var(--radius-2xl);overflow:hidden;box-shadow:var(--shadow-card);transition:all .3s ease}
.setting-options button{font:inherit;font-weight:600;font-size:13px;padding:9px 14px;border:0;border-right:1px solid var(--border-soft);background:var(--surface);color:var(--ink);cursor:pointer;transition:all .3s ease}
.setting-options button:last-child{border-right:0}
.setting-options button.active{background:var(--button-bg);color:var(--button-fg)}
.setting-options button:hover:not(.active){background:var(--surface-focus)}
.setting-options button:focus-visible{outline:3px solid var(--blue);outline-offset:-3px}
.checkbox-setting{display:flex;align-items:center;justify-content:space-between;gap:16px}
.checkbox-setting label{display:flex;align-items:center;gap:10px;font-weight:600;font-size:15px;cursor:pointer}
.checkbox-setting input{width:20px;height:20px;accent-color:var(--blue);cursor:pointer;border-radius:6px;transition:all .3s ease}

/* masthead */
.masthead{display:flex;align-items:baseline;gap:18px;flex-wrap:wrap;
  padding:26px 0 20px;border-bottom:1px solid var(--border-soft);margin-bottom:34px}
.masthead a.wordmark{font-family:"Archivo Black",sans-serif;font-size:22px;
  text-decoration:none;letter-spacing:-.03em}
.masthead .count{color:var(--mute);font-size:14px}
.backlink{margin-left:auto;font-size:14px;color:var(--blue);text-decoration:none;
  border-bottom:1px solid var(--blue);padding-bottom:1px}
.backlink:hover{color:var(--red);border-color:var(--red)}

/* shared bits */
.cover{display:block;width:100%;aspect-ratio:1;object-fit:cover;
  border:1px solid var(--border-soft);border-radius:var(--radius-2xl);
  box-shadow:var(--shadow-card),0 0 0 1px rgba(225,52,30,.08);background:var(--paper);
  transition:all .3s ease}
.cover.blue{box-shadow:var(--shadow-card),0 0 0 1px rgba(27,74,160,.12)}
.cover:hover{transform:translateY(-3px);box-shadow:var(--shadow-deep)}
.placeholder{display:flex;align-items:center;justify-content:center;
  font-family:"Archivo Black",sans-serif;font-size:13%;color:var(--mute);
  background:repeating-linear-gradient(45deg,rgba(22,19,15,.05) 0 8px,transparent 8px 16px)}
.placeholder span{font-size:1.6rem;letter-spacing:.04em}
.meta{color:var(--mute);font-size:14px}

/* index */
.index-top{margin-bottom:6px}
.lede{max-width:56ch;margin:0 0 30px;color:var(--mute)}
.filter{width:100%;max-width:420px;padding:14px 18px;font:inherit;color:var(--ink);
  background:var(--surface);border:1px solid var(--border-soft);border-radius:var(--radius-2xl);
  margin-bottom:34px;box-shadow:var(--shadow-card);
  transition:all .3s ease}
.filter::placeholder{color:var(--mute);opacity:.85}
.filter:hover{background:var(--surface-focus);border-color:rgba(27,74,160,.22)}
.filter:focus{outline:none;border-color:rgba(27,74,160,.45);
  background:var(--surface-focus);box-shadow:var(--shadow-deep),0 0 0 3px rgba(27,74,160,.14)}

/* side panels: newest releases + top producers */
.side-panels{float:right;width:320px;margin-left:32px}
body.hide-home-sidebar .side-panels{display:none}

/* When the home sidebar is visible, keep roster/search result rows out from underneath it. */
body:not(.hide-home-sidebar) #roster-view,
body:not(.hide-home-sidebar) #search-results{margin-right:352px}

html.singles-only #album-releases,
html.singles-only #album-release-heading,
html.singles-only .album-track-credit{display:none}

.newest-panel,.top-producers-panel{
  border:1px solid var(--border-soft);border-radius:var(--radius-2xl);
  padding:18px;background:var(--surface);color:var(--ink);
  box-shadow:var(--shadow-card);transition:all .3s ease;
}
.newest-panel:hover,.top-producers-panel:hover{box-shadow:var(--shadow-deep)}
.newest-panel{margin-bottom:24px}
.newest-panel h2,.top-producers-panel h2{font-size:14px;text-transform:uppercase;letter-spacing:.03em;
  margin:0 0 12px;padding-bottom:10px;border-bottom:1px solid var(--border-soft)}
.newest-item{display:grid;grid-template-columns:52px 1fr;gap:12px;
  padding:10px 0;border-bottom:1px solid var(--rule);text-decoration:none}
.newest-item:last-child{border-bottom:0;padding-bottom:0}
.newest-item .cover{width:52px;height:52px;box-shadow:var(--shadow-card);border-width:1px}
.newest-item .cover.placeholder span{font-size:9px}
.newest-title{font-family:"Archivo Black",sans-serif;font-size:14px;line-height:1.2;margin:0 0 3px}
.newest-item:hover .newest-title{color:var(--red)}
.newest-meta{font-size:12px;color:var(--mute);margin:0;line-height:1.4}


.top-producers-list{list-style:none;margin:0;padding:0}
.top-producers-list li{border-bottom:1px solid var(--rule)}
.top-producers-list li:last-child{border-bottom:0}
.top-producers-list a{display:flex;align-items:baseline;gap:8px;padding:9px 0;text-decoration:none}
.top-producers-list .rank{font-family:"Archivo Black",sans-serif;color:var(--blue);font-size:13px;min-width:20px}
.top-producers-list .pname{font-weight:600;font-size:14px;flex:1}
.top-producers-list .pcount{color:var(--mute);font-size:12px;white-space:nowrap}
.top-producers-list a:hover .pname{color:var(--red)}

.roster{list-style:none;margin:0;padding:0;border-top:1px solid var(--rule);display:flow-root}
.roster li{border-bottom:1px solid var(--rule)}
.roster a{display:grid;grid-template-columns:76px 1fr auto;gap:20px;align-items:center;
  padding:16px 10px;text-decoration:none;border-radius:var(--radius-2xl);transition:all .3s ease}
.roster a:hover{background:rgba(27,74,160,.08);box-shadow:var(--shadow-card)}
.roster a:focus-visible{outline:3px solid var(--blue);outline-offset:-3px}
.roster .thumb{width:76px;height:76px;object-fit:cover;border:1px solid var(--border-soft);border-radius:var(--radius-2xl);box-shadow:var(--shadow-card);transition:all .3s ease}
.roster .name{font-family:"Archivo Black",sans-serif;font-size:26px;line-height:1.1}
.roster .alias{color:var(--mute);font-size:14px}
.roster .tally{color:var(--blue);font-size:14px;text-align:right}

/* artist header */
.hero{display:grid;grid-template-columns:300px 1fr;gap:38px;align-items:start;margin-bottom:40px}
.portrait{width:100%;aspect-ratio:4/5;object-fit:cover;border:1px solid var(--border-soft);
  border-radius:var(--radius-2xl);box-shadow:var(--shadow-deep);transition:all .3s ease}
.hero h1{font-size:clamp(40px,7vw,72px);line-height:.94;margin-bottom:16px}
.facts{list-style:none;margin:0 0 22px;padding:0;font-size:15px}
.facts li{display:flex;gap:12px;padding:7px 0;border-bottom:1px solid var(--rule)}
.facts b{font-weight:600;min-width:104px;color:var(--mute)}
.facts a{color:var(--blue);text-decoration:none;border-bottom:1px solid var(--blue)}
.facts a:hover{color:var(--red);border-color:var(--red)}
.artist-rip{display:flex;align-items:center;gap:14px;margin:0 0 24px;padding:10px 0}
.artist-rip img{width:58px;height:58px;object-fit:cover;border:1px solid var(--border-soft);border-radius:var(--radius-2xl);box-shadow:var(--shadow-card);flex:0 0 auto;transition:all .3s ease}
.artist-rip span{font-weight:600;line-height:1.25}

/* mode toggle */
.modetoggle{display:inline-flex;align-items:center;border:1px solid var(--border-soft);
  border-radius:var(--radius-2xl);margin:22px 0 0;overflow:hidden;box-shadow:var(--shadow-card);transition:all .3s ease}
.modetoggle button{font:inherit;font-weight:600;font-size:14px;padding:10px 18px;
  background:var(--surface);color:var(--ink);border:0;cursor:pointer;transition:all .3s ease}
.modetoggle button.active{background:var(--ink);color:var(--paper)}
.modetoggle button:not(.active):hover{background:var(--surface-focus)}
.mode-panel{display:none}
.mode-panel.active{display:block}
.sortlabel{font-size:13px;font-weight:600;color:var(--mute)}
.sorttoggle-row{display:flex;align-items:center;gap:12px;flex-wrap:wrap;margin:22px 0 0}
.sorttoggle-row .modetoggle{margin:0}
.sorttoggle button{padding:9px 14px}

/* pager */
.pager{display:flex;flex-wrap:wrap;gap:8px;margin-top:24px}
.pagebtn{font:inherit;font-weight:600;font-size:14px;min-width:38px;padding:9px 12px;
  border:1px solid var(--border-soft);border-radius:var(--radius-2xl);
  background:var(--surface);color:var(--ink);cursor:pointer;box-shadow:var(--shadow-card);
  transition:all .3s ease}
.pagebtn.active{background:var(--ink);color:var(--paper);box-shadow:var(--shadow-deep)}
.pagebtn:not(.active):hover{background:var(--surface-focus);transform:translateY(-1px);box-shadow:var(--shadow-deep)}

/* producer credits */
.prodlist{list-style:none;margin:0;padding:0;border-top:1px solid var(--rule)}
.prodlist li{border-bottom:1px solid var(--rule)}
.prodlist a.row{display:grid;grid-template-columns:1fr auto auto;gap:14px;
  padding:12px 10px;text-decoration:none;align-items:baseline;border-radius:var(--radius-2xl);transition:all .3s ease}
.prodlist a.row:hover{background:rgba(225,52,30,.1);box-shadow:var(--shadow-card)}
.prodlist .who{color:var(--mute);font-size:14px}
.prodlist .kind{color:var(--blue);font-size:13px;text-transform:uppercase;letter-spacing:.04em}

/* collective / roster */
.members{list-style:none;margin:0;padding:0}
.members li{padding:8px 0;border-bottom:1px solid var(--rule)}
.members a{color:var(--blue);text-decoration:none;border-bottom:1px solid var(--blue)}
.members a:hover{color:var(--red);border-color:var(--red)}

/* platform links */
.platforms{display:flex;gap:12px;flex-wrap:wrap;margin-top:22px}
.platform{display:inline-flex;align-items:center;gap:9px;padding:11px 16px;
  border:1px solid var(--border-soft);border-radius:var(--radius-2xl);
  background:var(--surface);text-decoration:none;font-size:14px;font-weight:600;
  box-shadow:var(--shadow-card);transition:all .3s ease}
.platform svg{width:22px;height:22px}
a.platform:hover{background:var(--ink);color:var(--paper);transform:translateY(-2px);box-shadow:var(--shadow-deep)}
a.platform:focus-visible{outline:3px solid var(--blue);outline-offset:2px}
.platform.off{border-color:var(--rule);color:var(--mute);filter:grayscale(1);opacity:.5;cursor:default}

/* projects */
.section-head{display:flex;align-items:baseline;gap:14px;
  border-bottom:1px solid var(--border-soft);padding-bottom:10px;margin:52px 0 26px}
.section-head h2{font-size:26px}
.section-head span{color:var(--mute);font-size:14px}
.release{display:grid;grid-template-columns:280px 1fr;gap:38px;
  padding-bottom:44px;margin-bottom:44px;border-bottom:1px solid var(--rule)}
.release:last-child{border-bottom:0;margin-bottom:0;padding-bottom:0}
.release h3{font-size:32px;line-height:1.05}
.release h3 a{text-decoration:none}
.release h3 a:hover{color:var(--red)}
.kindline{margin:6px 0 16px;font-size:14px;color:var(--blue);font-weight:600}
.kindline a{text-decoration:none;border-bottom:1px solid var(--blue)}
.kindline a:hover{color:var(--red);border-color:var(--red)}
.tracklist{list-style:none;margin:20px 0 0;padding:0;border-top:1px solid var(--rule)}
.tracklist li{border-bottom:1px solid var(--rule)}
.track-row{display:grid;grid-template-columns:34px 1fr;gap:12px;padding:10px 8px;align-items:baseline;border-radius:calc(var(--radius-2xl) - 4px);transition:all .3s ease}
.track-row:hover{background:rgba(225,52,30,.1);box-shadow:var(--shadow-card)}
.track-main{text-decoration:none}
.track-main:hover{color:var(--red)}
.track-main:focus-visible{outline:3px solid var(--blue);outline-offset:2px}
.tracklist .num{color:var(--blue);font-variant-numeric:tabular-nums;font-size:14px}
.tracklist .feat{color:var(--mute)}
.tracklist .feat a,.tracklist .credit-hover > a{color:var(--blue) !important;text-decoration:none;border-bottom:1px solid var(--blue)}
.tracklist .feat a:hover,.tracklist .credit-hover > a:hover{color:var(--red) !important;border-color:var(--red)}

/* artist/producer hover cards */
.credit-hover{position:relative;display:inline-block}
.credit-hover > a{position:relative;z-index:2;color:var(--blue);text-decoration:none;border-bottom:1px solid var(--blue)}
.credit-hover > a:hover{color:var(--red);border-color:var(--red)}
.artist-hover-card{position:absolute;z-index:1000;left:50%;bottom:calc(100% + 12px);transform:translateX(-50%) translateY(5px);width:230px;padding:14px;background:var(--paper);color:var(--ink);border:1px solid var(--border-soft);border-radius:var(--radius-2xl);box-shadow:var(--shadow-deep);opacity:0;visibility:hidden;pointer-events:none;transition:all .3s ease}
.credit-hover:hover .artist-hover-card,.credit-hover:focus-within .artist-hover-card{opacity:1;visibility:visible;transform:translateX(-50%) translateY(0)}
.artist-hover-name{font-family:'Archivo Black',Archivo,sans-serif;font-size:20px;line-height:1.05;margin:0 0 4px;overflow-wrap:anywhere}
.artist-hover-stats{display:block;font-size:12px;color:var(--mute);margin:0 0 10px}
.artist-hover-image{display:block;width:100%;aspect-ratio:1/1;object-fit:cover;border:1px solid var(--border-soft);border-radius:calc(var(--radius-2xl) - 4px);background:var(--rule);transition:all .3s ease}
.artist-hover-placeholder{display:flex;align-items:center;justify-content:center;font-family:'Archivo Black',Archivo,sans-serif;font-size:38px;color:var(--mute)}

/* singles grid */
.singles{display:grid;grid-template-columns:repeat(auto-fill,minmax(180px,1fr));gap:30px}
.singles a{text-decoration:none;display:block}
.singles .cover{box-shadow:var(--shadow-card),0 0 0 1px rgba(27,74,160,.12)}
.singles a:hover .cover{box-shadow:var(--shadow-deep),0 0 0 1px rgba(225,52,30,.15)}
.singles h3{font-family:'Inter',sans-serif;font-weight:900;font-size:18px;margin-top:14px;letter-spacing:-0.01em;}

/* detail pages */

.detail{display:grid;grid-template-columns:320px 1fr;gap:42px;align-items:start}
.detail h1{font-size:clamp(34px,5.5vw,56px);line-height:1;margin-bottom:12px}
.credits{list-style:none;margin:20px 0 0;padding:0;font-size:15px}
.credits li{display:flex;gap:12px;padding:7px 0;border-bottom:1px solid var(--rule)}
.credits b{font-weight:600;min-width:104px;color:var(--mute)}
.credits a{color:var(--blue);text-decoration:none;border-bottom:1px solid var(--blue)}
.credits a:hover{color:var(--red);border-color:var(--red)}
.listen{display:inline-block;margin-top:24px;padding:13px 20px;background:var(--ink);
  color:var(--paper);text-decoration:none;font-weight:600;border-radius:var(--radius-2xl);
  box-shadow:var(--shadow-deep);transition:all .3s ease}
.listen:hover{background:var(--red);transform:translateY(-2px);box-shadow:var(--shadow-card)}
.embed{margin-top:24px;max-width:480px;border-radius:var(--radius-2xl);overflow:hidden;box-shadow:var(--shadow-card);transition:all .3s ease}
.embed iframe{display:block;width:100%;border:0}
.embed.video{max-width:640px}
.embed.video iframe{aspect-ratio:16/9;height:auto}
.empty{color:var(--mute);max-width:52ch}

@media (max-width:760px){
  .hero,.release,.detail{grid-template-columns:1fr;gap:24px}
  .portrait{max-width:280px}
  .cover{max-width:320px}
  .roster a{grid-template-columns:60px 1fr;row-gap:4px}
  .roster .thumb{width:60px;height:60px}
  .roster .tally{grid-column:2;text-align:left}
  .side-panels{float:none;width:auto;margin-left:0;margin-top:24px}
}
@media (prefers-reduced-motion:reduce){*{transition:none!important;animation:none!important}}


/* persistent player */
body.sp-active{padding-bottom:96px}
.sp-bar{position:fixed;left:50%;bottom:14px;transform:translateX(-50%);z-index:900;
  width:min(760px,calc(100% - 24px));display:flex;align-items:center;gap:14px;
  padding:10px 14px;background:var(--ink);color:var(--paper);
  border-radius:var(--radius-2xl);box-shadow:var(--shadow-deep);
  font:500 13px Archivo,"Helvetica Neue",Arial,sans-serif}
.sp-bar[hidden]{display:none}
.sp-bar button{appearance:none;border:0;background:transparent;color:inherit;cursor:pointer;font:inherit;padding:6px 8px;border-radius:10px}
.sp-bar button:hover{background:rgba(255,255,255,.14)}
.sp-bar button:focus-visible,.sp-bar input:focus-visible{outline:2px solid var(--paper);outline-offset:2px}
.sp-toggle{font-size:16px;width:34px;flex:none}
.sp-info{min-width:0;flex:1 1 auto;display:flex;flex-direction:column;gap:2px}
.sp-title{color:inherit;text-decoration:none;font-weight:600;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.sp-title:hover{text-decoration:underline}
.sp-sub{opacity:.7;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;font-size:12px}
.sp-seek{width:100%;margin-top:3px;height:4px;accent-color:var(--red)}
.sp-plays{flex:none;opacity:.85;font-variant-numeric:tabular-nums}
.sp-vol{flex:none;display:flex;align-items:center;gap:6px}
.sp-vol input{width:90px;accent-color:var(--red)}
.sp-vol output{min-width:38px;text-align:right;font-variant-numeric:tabular-nums}
.sp-close{flex:none;font-size:16px}
.sp-frame{position:absolute;width:1px;height:1px;opacity:0;pointer-events:none;border:0}
.sp-popout{display:inline-block;margin-top:12px;padding:9px 14px;border:1px solid var(--border-soft);
  border-radius:var(--radius-2xl);background:var(--surface);color:var(--ink);cursor:pointer;
  font:600 13px Archivo,"Helvetica Neue",Arial,sans-serif;box-shadow:var(--shadow-card);transition:all .3s ease}
.sp-popout:hover{background:var(--ink);color:var(--paper);transform:translateY(-2px)}
@media (max-width:640px){
  .sp-bar{flex-wrap:wrap;gap:8px 10px;bottom:8px}
  .sp-info{flex-basis:calc(100% - 100px)}
  .sp-vol input{width:110px}
  body.sp-active{padding-bottom:150px}
}

/* queue + extras */
.sp-queue{position:absolute;left:0;right:0;bottom:calc(100% + 10px);max-height:min(50vh,360px);overflow:auto;
  background:var(--ink);color:var(--paper);border-radius:var(--radius-2xl);box-shadow:var(--shadow-deep);padding:12px 14px}
.sp-queue[hidden]{display:none}
.sp-queue-head{display:flex;align-items:center;justify-content:space-between;margin-bottom:6px}
.sp-queue-head b{font-family:'Archivo Black',Archivo,sans-serif;font-size:15px;font-weight:400}
.sp-queue-now{opacity:.7;font-size:12px;margin-bottom:8px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.sp-queue-list{list-style:none;margin:0;padding:0}
.sp-queue-list li{display:flex;align-items:center;gap:6px;border-top:1px solid rgba(255,255,255,.14)}
.sp-queue-list .sp-q-main{flex:1 1 auto;min-width:0;text-align:left;display:flex;flex-direction:column;gap:1px;padding:8px}
.sp-q-title{font-weight:600;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.sp-q-sub{opacity:.65;font-size:12px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.sp-q-tag{flex:none;font-size:11px;opacity:.7;border:1px solid rgba(255,255,255,.35);border-radius:999px;padding:1px 7px}
.sp-q-move{flex:none;display:inline-flex;flex-direction:column;gap:2px;margin-right:2px}
.sp-q-move button{width:26px;height:22px;padding:0;border:1px solid rgba(255,255,255,.28);background:transparent;color:var(--paper);
  border-radius:5px;font:700 13px/20px Arial,sans-serif;cursor:pointer;display:block}
.sp-q-move button:hover:not(:disabled){background:var(--paper);color:var(--ink)}
.sp-q-move button:disabled{opacity:.28;color:#777;border-color:rgba(255,255,255,.12);cursor:default}
.sp-queue-empty{opacity:.7;padding:8px 0;font-size:13px}
.sp-badge{display:inline-block;min-width:16px;margin-left:5px;padding:0 5px;border-radius:999px;background:var(--red);color:#fff;font-size:11px;line-height:16px;text-align:center}
.sp-badge:empty{display:none}
.sp-mute{font-size:15px;padding:4px 6px !important}
.sp-actions{display:flex;flex-wrap:wrap;gap:10px;margin-top:12px}
.sp-actions .sp-popout{margin-top:0}
.sp-rowbtns{display:inline-flex;gap:4px;margin-left:10px;vertical-align:baseline}
.sp-rowbtns button{border:1px solid var(--border-soft);background:var(--surface);color:var(--mute);border-radius:8px;
  font:600 11px Archivo,"Helvetica Neue",Arial,sans-serif;padding:1px 7px;cursor:pointer;line-height:1.5}
.sp-rowbtns button:hover{background:var(--ink);color:var(--paper)}
@media (max-width:640px){ .sp-vol input{width:80px} }
.sp-cover-link{flex:none;display:block;width:50px;height:50px;border-radius:10px;overflow:hidden;background:rgba(255,255,255,.12);box-shadow:0 0 0 1px rgba(255,255,255,.18)}
.sp-cover-link[hidden]{display:none}
.sp-cover-link img{display:block;width:100%;height:100%;object-fit:cover}
.sp-q-thumb{flex:none;width:36px;height:36px;border-radius:8px;object-fit:cover;background:rgba(255,255,255,.12)}
/* dark mode: the bar is light there, so hovers/borders darken instead of lighten */
.sp-bar button:active{background:rgba(255,255,255,.22)}
html.dark .sp-bar button:hover{background:rgba(0,0,0,.13)}
html.dark .sp-bar button:active{background:rgba(0,0,0,.22)}
html.dark .sp-queue-list li{border-top-color:rgba(0,0,0,.14)}
html.dark .sp-q-tag{border-color:rgba(0,0,0,.35)}
html.dark .sp-q-move button{border-color:rgba(0,0,0,.28)}
html.dark .sp-q-move button:disabled{color:#8a857c;border-color:rgba(0,0,0,.14)}
html.dark .sp-cover-link{background:rgba(0,0,0,.08);box-shadow:0 0 0 1px rgba(0,0,0,.18)}
html.dark .sp-q-thumb{background:rgba(0,0,0,.08)}
.sp-toast{position:absolute;left:0;right:0;bottom:calc(100% + 10px);text-align:center;background:var(--red);color:#fff;border-radius:var(--radius-2xl);padding:9px 14px;box-shadow:var(--shadow-deep);font-weight:600}
.sp-toast[hidden]{display:none}
</style>
</head>
<body class="antialiased font-sans transition-all duration-300">
<button class="theme-toggle rounded-2xl shadow-2xl transition-all duration-300" id="theme-toggle" type="button"
        aria-label="Switch to dark mode" title="Switch to dark mode">
  <span class="moon" aria-hidden="true">☾</span>
  <span class="sun" aria-hidden="true">☀</span>
</button>
<a class="random-song-button rounded-2xl shadow-2xl transition-all duration-300" href="{{ url_for('random_song') }}" id="random-song-button" aria-label="Go to a random song" title="Random song">⚄</a>
<button class="settings-button rounded-2xl shadow-2xl transition-all duration-300" id="settings-button" type="button" aria-label="Open settings" title="Settings" aria-expanded="false">⚙</button>
<div class="settings-backdrop" id="settings-backdrop" hidden></div>
<section class="settings-menu rounded-2xl shadow-2xl transition-all duration-300" id="settings-menu" hidden aria-label="Settings">
  <div class="settings-head">
    <h2>Settings</h2>
    <button class="settings-close" id="settings-close" type="button" aria-label="Close settings">×</button>
  </div>
  <div class="setting">
    <p class="setting-title">Default Sort by Date:</p>
    <div class="setting-options" role="group" aria-label="Default sort by date">
      <button type="button" data-default-sort="oldest">Oldest First</button>
      <button type="button" data-default-sort="newest">Newest First</button>
    </div>
  </div>
  <div class="setting checkbox-setting">
    <label for="sidebar-visibility">
      <input id="sidebar-visibility" type="checkbox" checked>
      <span>Sidebar Visibility</span>
    </label>
  </div>
  <div class="setting checkbox-setting">
    <label for="click-sound">
      <input id="click-sound" type="checkbox">
      <span>Click Sound</span>
    </label>
  </div>
  <div class="setting checkbox-setting">
    <label for="singles-only">
      <input id="singles-only" type="checkbox">
      <span>Singles Only</span>
    </label>
  </div>
</section>
<div class="page">
  <header class="masthead">
    <a class="wordmark" href="{{ url_for('index') }}">Underground Catalog</a>
    {% block masthead %}{% endblock %}
  </header>
  {% block content %}{% endblock %}
</div>
<footer class="site-footer">
  <a href="{{ url_for('about') }}">About</a>
  <span class="footer-separator">·</span>
  <a href="{{ url_for('content_warning') }}">Content Warning</a>
</footer>
<div class="sp-bar" id="sp-bar" hidden role="region" aria-label="Music player">
  <div class="sp-toast" id="sp-toast" hidden role="status"></div>
  <section class="sp-queue" id="sp-queue" hidden aria-label="Up next">
    <div class="sp-queue-head"><b>Up next</b><button id="sp-queue-clear" type="button">Clear queue</button></div>
    <div class="sp-queue-now" id="sp-queue-now"></div>
    <ol class="sp-queue-list" id="sp-queue-list"></ol>
  </section>
  <a class="sp-cover-link" id="sp-cover-link" data-spa hidden aria-label="Open this song's page"><img id="sp-cover" alt=""></a>
  <button class="sp-toggle" id="sp-toggle" type="button" aria-label="Play or pause (space)" title="Play / pause (space)">&#9654;</button>
  <button class="sp-next" id="sp-next" type="button" aria-label="Next song" title="Next song">&#9197;&#65038;</button>
  <div class="sp-info">
    <a class="sp-title" id="sp-title" href="#" target="_blank" rel="noopener">Loading&hellip;</a>
    <span class="sp-sub" id="sp-sub"></span>
    <input class="sp-seek" id="sp-seek" type="range" min="0" max="1000" value="0" aria-label="Seek">
  </div>
  <span class="sp-plays" id="sp-plays" hidden></span>
  <div class="sp-vol">
    <button class="sp-mute" id="sp-mute" type="button" aria-label="Mute (m)" title="Mute (m)">&#128266;</button>
    <input id="sp-volume" type="range" min="0" max="100" step="1" value="50" aria-label="Volume">
    <output id="sp-volume-out">50%</output>
  </div>
  <button id="sp-queue-btn" type="button" aria-expanded="false" title="Show what's coming up">Queue<span class="sp-badge" id="sp-qcount"></span></button>
  <button id="sp-share" type="button" title="Share this on SoundCloud">Share</button>
  <button class="sp-close" id="sp-close" type="button" aria-label="Close player">&#10005;</button>
</div>
<script src="https://w.soundcloud.com/player/api.js"></script>
<script>
(function(){
  var toggle = document.getElementById('theme-toggle');
  if (!toggle) return;

  function applyTheme(dark){
    document.documentElement.classList.toggle('dark', dark);
    document.documentElement.classList.toggle('light', !dark);
    document.documentElement.style.colorScheme = dark ? 'dark' : 'light';
  }

  function updateThemeButton(){
    var dark = document.documentElement.classList.contains('dark');
    toggle.setAttribute('aria-label', dark ? 'Switch to light mode' : 'Switch to dark mode');
    toggle.setAttribute('title', dark ? 'Switch to light mode' : 'Switch to dark mode');
  }

  var initialDark = document.documentElement.classList.contains('dark');
  applyTheme(initialDark);
  updateThemeButton();

  toggle.addEventListener('click', function(){
    var dark = !document.documentElement.classList.contains('dark');
    applyTheme(dark);
    try {
      localStorage.setItem('undergroundCatalogTheme', dark ? 'dark' : 'light');
    } catch(e) {}
    updateThemeButton();
  });
})();

(function(){
  var button = document.getElementById('settings-button');
  var menu = document.getElementById('settings-menu');
  var backdrop = document.getElementById('settings-backdrop');
  var close = document.getElementById('settings-close');
  var sortButtons = document.querySelectorAll('[data-default-sort]');
  var sidebar = document.getElementById('sidebar-visibility');
  var clickSound = document.getElementById('click-sound');
  var singlesOnly = document.getElementById('singles-only');

  if (!button || !menu || !backdrop) return;

  function getSetting(key, fallback){
    try { return localStorage.getItem(key) || fallback; } catch(e) { return fallback; }
  }
  function saveSetting(key, value){
    try { localStorage.setItem(key, value); } catch(e) {}
  }
  function applySidebarVisibility(visible){
    document.body.classList.toggle('hide-home-sidebar', !visible);
    if (sidebar) sidebar.checked = visible;
  }
  function applyDefaultSort(order){
    sortButtons.forEach(function(btn){
      btn.classList.toggle('active', btn.dataset.defaultSort === order);
    });
    if (window.setReleaseOrder) {
      window.setReleaseOrder(order);
    } else {
      setTimeout(function(){
        if (window.setReleaseOrder) window.setReleaseOrder(order);
      }, 0);
    }
  }
  function openSettings(){
    menu.hidden = false;
    backdrop.hidden = false;
    button.setAttribute('aria-expanded', 'true');
    if (close) close.focus();
  }
  function closeSettings(){
    menu.hidden = true;
    backdrop.hidden = true;
    button.setAttribute('aria-expanded', 'false');
  }

  button.addEventListener('click', openSettings);
  if (close) close.addEventListener('click', closeSettings);
  backdrop.addEventListener('click', closeSettings);
  document.addEventListener('keydown', function(e){
    if (e.key === 'Escape' && !menu.hidden) closeSettings();
  });

  var savedSort = getSetting('undergroundCatalogDefaultSort', 'oldest');
  applyDefaultSort(savedSort === 'newest' ? 'newest' : 'oldest');

  sortButtons.forEach(function(btn){
    btn.addEventListener('click', function(){
      var order = btn.dataset.defaultSort === 'newest' ? 'newest' : 'oldest';
      saveSetting('undergroundCatalogDefaultSort', order);
      applyDefaultSort(order);
    });
  });

  var savedSidebar = getSetting('undergroundCatalogSidebarVisibility', 'visible');
  applySidebarVisibility(savedSidebar !== 'hidden');

  if (sidebar){
    sidebar.addEventListener('change', function(){
      var visible = sidebar.checked;
      saveSetting('undergroundCatalogSidebarVisibility', visible ? 'visible' : 'hidden');
      applySidebarVisibility(visible);
    });
  }

  function applyClickSound(enabled){
    if (clickSound) clickSound.checked = enabled;
  }

  var savedClickSound = getSetting('undergroundCatalogClickSound', 'off');
  applyClickSound(savedClickSound === 'on');

  if (clickSound){
    clickSound.addEventListener('change', function(){
      saveSetting('undergroundCatalogClickSound', clickSound.checked ? 'on' : 'off');
      applyClickSound(clickSound.checked);
    });
  }

  function applySinglesOnly(enabled){
    document.documentElement.classList.toggle('singles-only', enabled);
    if (singlesOnly) singlesOnly.checked = enabled;
    var randomButton = document.getElementById('random-song-button');
    if (randomButton){
      var baseHref = randomButton.getAttribute('data-random-base') || randomButton.getAttribute('href').split('?')[0];
      randomButton.setAttribute('data-random-base', baseHref);
      randomButton.setAttribute('href', baseHref + (enabled ? '?singles_only=1' : ''));
    }
    if (typeof window.applySinglesOnlyToSearch === 'function') {
      window.applySinglesOnlyToSearch();
    }
  }

  var savedSinglesOnly = getSetting('undergroundCatalogSinglesOnly', 'off');
  applySinglesOnly(savedSinglesOnly === 'on');

  if (singlesOnly){
    singlesOnly.addEventListener('change', function(){
      saveSetting('undergroundCatalogSinglesOnly', singlesOnly.checked ? 'on' : 'off');
      applySinglesOnly(singlesOnly.checked);
    });
  }
})();

function setMode(mode){
  document.querySelectorAll('.modetoggle button[data-mode]').forEach(function(btn){
    btn.classList.toggle('active', btn.dataset.mode === mode);
  });
  document.querySelectorAll('.mode-panel').forEach(function(panel){
    panel.classList.toggle('active', panel.dataset.mode === mode);
  });
}
(function(){
  function captureOrder(id){
    var el = document.getElementById(id);
    return el ? { el: el, items: Array.prototype.slice.call(el.children) } : null;
  }
  var releaseGroups = [];
  window.captureReleaseGroups = function(){
    releaseGroups = [captureOrder('projects-list'), captureOrder('singles-grid')].filter(Boolean);
  };
  window.captureReleaseGroups();
  window.setReleaseOrder = function(order){
    releaseGroups.forEach(function(g){
      var ordered = order === 'newest' ? g.items.slice().reverse() : g.items.slice();
      ordered.forEach(function(item){ g.el.appendChild(item); });
    });
    document.querySelectorAll('.sorttoggle button').forEach(function(btn){
      btn.classList.toggle('active', btn.dataset.order === order);
    });
  };
})();
function escapeHtml(s){
  var div = document.createElement('div');
  div.textContent = s == null ? '' : s;
  return div.innerHTML;
}
function renderSearchResults(matches, listEl, emptyEl, typeLabels){
  listEl.innerHTML = '';
  matches.forEach(function(entry){
    var li = document.createElement('li');
    var a = document.createElement('a');
    a.className = 'row';
    a.href = entry.url;
    var tag = typeLabels && entry.type ? '<span class="kind">' + escapeHtml(typeLabels[entry.type] || entry.type) + '</span>' : '';
    a.innerHTML = '<span>' + escapeHtml(entry.title) + '</span>' +
                  '<span class="who">' + escapeHtml(entry.sub || '') + '</span>' + tag;
    li.appendChild(a);
    listEl.appendChild(li);
  });
  if (emptyEl) emptyEl.hidden = matches.length > 0;
}
function renderPager(container, totalItems, pageSize, currentPage, onSelect){
  if (!container) return;
  container.innerHTML = '';
  var totalPages = Math.max(1, Math.ceil(totalItems / pageSize));
  if (totalPages <= 1) return;
  for (var p = 1; p <= totalPages; p++){
    var btn = document.createElement('button');
    btn.type = 'button';
    btn.textContent = String(p);
    btn.className = 'pagebtn' + (p === currentPage ? ' active' : '');
    btn.addEventListener('click', (function(pp){ return function(){ onSelect(pp); }; })(p));
    container.appendChild(btn);
  }
}
</script>
<script>
(function(){
  var bar = document.getElementById('sp-bar');
  if (!bar) return;
  function $(id){ return document.getElementById(id); }
  var btnToggle = $('sp-toggle'), btnNext = $('sp-next'), elTitle = $('sp-title'), elSub = $('sp-sub'),
      elPlays = $('sp-plays'), elSeek = $('sp-seek'), elVol = $('sp-volume'), elVolOut = $('sp-volume-out'),
      btnMute = $('sp-mute'), btnShare = $('sp-share'), btnClose = $('sp-close'), btnQueue = $('sp-queue-btn'),
      elQCount = $('sp-qcount'), panel = $('sp-queue'), qNow = $('sp-queue-now'), qList = $('sp-queue-list'),
      qClear = $('sp-queue-clear'), elCoverLink = $('sp-cover-link'), elCover = $('sp-cover');

  var widget = null, frame = null, barPlaying = false, startPos = 0, startIdx = 0, lastIdx = 0;
  var shareUrl = '', shareTitle = '';
  var current = null, queue = [], recent = [], playable = [], byHref = {}, byUrl = {};
  var VOL_KEY = 'undergroundCatalogPlayerVolume';
  var vol = 50, muted = false;
  var wantPlay = false, lastProgress = 0, lastPos = -1, failStreak = 0, toastTimer = null;
  var gotPlay = false, checking = false;
  try { var sv = parseInt(localStorage.getItem(VOL_KEY), 10); if (sv >= 0 && sv <= 100) vol = sv; } catch(e) {}
  elVol.value = vol;

  /* ---------------------------------------------------------- helpers */
  function ukey(u){
    u = String(u || '').split('?')[0].split('#')[0].toLowerCase();
    while (u.charAt(u.length - 1) === '/') u = u.slice(0, -1);
    return u;
  }
  function niceName(url){
    var last = String(url || '').split('?')[0].split('/').filter(Boolean).pop() || 'SoundCloud';
    try { last = decodeURIComponent(last); } catch(e) {}
    return last.split('-').join(' ');
  }
  function itemFor(url, fallbackTitle){
    var m = byUrl[ukey(url)];
    if (m) return { url: url, title: m.title, sub: m.sub, href: m.href, artist_slug: m.artist_slug, cover: m.cover || '' };
    return { url: url, title: fallbackTitle || '', sub: '', href: '', artist_slug: '', cover: '' };
  }
  function withApi(cb){
    if (window.SC && SC.Widget) return cb();
    var t = setInterval(function(){ if (window.SC && SC.Widget){ clearInterval(t); cb(); } }, 100);
  }
  function embedSrc(url){
    return 'https://w.soundcloud.com/player/?url=' + encodeURIComponent(url) +
      '&auto_play=true&hide_related=true&show_comments=false&show_user=true&show_reposts=false&show_teaser=false&visual=false';
  }
  function fmtCount(n){
    if (n == null) return '';
    if (n >= 1000000) return (n / 1000000).toFixed(n >= 10000000 ? 0 : 1).replace('.0', '') + 'M';
    if (n >= 1000) return (n / 1000).toFixed(n >= 10000 ? 0 : 1).replace('.0', '') + 'K';
    return String(n);
  }
  function setIcon(playing){
    barPlaying = playing;
    btnToggle.innerHTML = playing ? '&#10074;&#10074;' : '&#9654;';
  }

  /* ---------------------------------------------------------- volume / mute */
  function applyVolume(){
    if (widget){ try { widget.setVolume(muted ? 0 : vol); } catch(e) {} }
    elVolOut.textContent = muted ? 'Muted' : vol + '%';
    btnMute.innerHTML = (muted || vol === 0) ? '&#128263;' : '&#128266;';
    btnMute.setAttribute('aria-pressed', muted ? 'true' : 'false');
  }
  function toggleMute(){ muted = !muted; applyVolume(); }
  applyVolume();

  /* ---------------------------------------------------------- stall watchdog: skip songs that won't play */
  var elToast = $('sp-toast');
  function toast(msg){
    elToast.textContent = msg;
    elToast.hidden = false;
    clearTimeout(toastTimer);
    toastTimer = setTimeout(function(){ elToast.hidden = true; }, 5000);
  }
  function resetWidget(){
    if (widget){ try { widget.pause(); } catch(e) {} }
    widget = null;
    frame = null;
    var f = $('sp-frame');
    if (f && f.parentNode) f.parentNode.removeChild(f);
  }
  function skipStuck(){
    var w = widget;
    if (!w || !wantPlay || bar.hidden) return;
    var name = (current && current.title) || niceName(current ? current.url : '');
    failStreak++;
    lastProgress = Date.now(); lastPos = -1;
    if (failStreak >= 5){
      wantPlay = false;
      setIcon(false);
      resetWidget();
      toast('Several songs in a row wouldn\u2019t play, so the autoplay stopped. Press play to try again.');
      return;
    }
    toast('Couldn\u2019t play \u201C' + name + '\u201D, skipping to the next song');
    var handled = false;
    function goNext(){
      if (handled) return;
      handled = true;
      resetWidget();       /* a stuck iframe may not answer, so start the next song in a fresh one */
      advance();
    }
    w.getSounds(function(list){
      if (handled || w !== widget) return;
      if (list && list.length > 1 && lastIdx < list.length - 1){ handled = true; w.next(); return; }
      goNext();
    });
    setTimeout(function(){ if (w === widget) goNext(); }, 1500);
  }
  /* Only skip after double-checking that the song really is stuck:
     a paused song, a throttled background tab, or a slow resume must never count. */
  function confirmStuck(){
    var w = widget;
    if (!w || checking) return;
    checking = true;
    var done = false;
    function finish(stuck){
      if (done) return;
      done = true;
      checking = false;
      clearTimeout(giveUp);
      if (w !== widget || !wantPlay) return;
      if (stuck) skipStuck(); else lastProgress = Date.now();
    }
    var giveUp = setTimeout(function(){ finish(true); }, 7000);   /* iframe not answering at all */
    w.isPaused(function(paused){
      if (done) return;
      if (paused && gotPlay){
        /* it had been playing and is now paused: that is a pause, not a failure */
        done = true; checking = false; clearTimeout(giveUp);
        if (w === widget){ wantPlay = false; setIcon(false); }
        return;
      }
      w.getPosition(function(p1){
        if (done) return;
        setTimeout(function(){
          if (done) return;
          w.getPosition(function(p2){ finish(!(p2 > p1 + 300)); });
        }, 2500);
      });
    });
  }
  setInterval(function(){
    if (!widget || !wantPlay || bar.hidden || checking) return;
    var limit = lastPos < 0 ? 15000 : 10000;
    if (Date.now() - lastProgress > limit) confirmStuck();
  }, 1000);
  document.addEventListener('visibilitychange', function(){ lastProgress = Date.now(); });
  function togglePlay(){
    if (!widget) return;
    if (wantPlay){ wantPlay = false; try { widget.pause(); } catch(e) {} setIcon(false); }
    else { wantPlay = true; lastProgress = Date.now(); lastPos = 0; try { widget.play(); } catch(e) {} }
  }

  /* ---------------------------------------------------------- now-playing info */
  function showCurrent(item){
    elTitle.textContent = item.title || niceName(item.url);
    elTitle.href = item.url || '#';
    elSub.textContent = item.sub || '';
    elPlays.hidden = true;
    elSeek.value = 0;
    shareUrl = item.url || '';
    shareTitle = item.title || '';
    if (item.cover){
      elCover.src = item.cover;
      elCoverLink.hidden = false;
      if (item.href) elCoverLink.setAttribute('href', item.href); else elCoverLink.removeAttribute('href');
    } else {
      elCover.removeAttribute('src');
      elCoverLink.hidden = true;
    }
  }
  function refreshSound(tries){
    var w = widget;
    if (!w) return;
    tries = tries || 0;
    w.getCurrentSound(function(snd){
      if (w !== widget) return;
      if (!snd){
        if (tries < 10) setTimeout(function(){ refreshSound(tries + 1); }, 600);
        return;
      }
      elTitle.textContent = snd.title || elTitle.textContent;
      if (snd.permalink_url) elTitle.href = snd.permalink_url;
      if (snd.user && snd.user.username && !(current && current.sub)) elSub.textContent = snd.user.username;
      shareUrl = snd.permalink_url || shareUrl;
      shareTitle = snd.title || shareTitle;
      if (snd.playback_count != null){ elPlays.textContent = '\u25B6 ' + fmtCount(snd.playback_count); elPlays.hidden = false; }
      else if (tries < 4){ setTimeout(function(){ refreshSound(tries + 1); }, 800); }
    });
  }

  /* ---------------------------------------------------------- the widget (fresh iframe every time the bar starts) */
  function makeFrame(url){
    var old = $('sp-frame');
    if (old && old.parentNode) old.parentNode.removeChild(old);
    var f = document.createElement('iframe');
    f.id = 'sp-frame';
    f.className = 'sp-frame';
    f.setAttribute('allow', 'autoplay');
    f.setAttribute('title', 'SoundCloud player');
    f.src = embedSrc(url);
    bar.appendChild(f);
    return f;
  }
  function bindBarWidget(w){
    w.bind(SC.Widget.Events.READY, function(){ if (w !== widget) return; applyVolume(); refreshSound(); });
    w.bind(SC.Widget.Events.PLAY, function(){
      if (w !== widget) return;
      wantPlay = true; gotPlay = true; lastProgress = Date.now();
      setIcon(true);
      applyVolume();
      refreshSound();
      w.getCurrentSoundIndex(function(i){ lastIdx = i || 0; });
      if (startIdx > 0){ var i2 = startIdx; startIdx = 0; w.skip(i2); return; }
      if (startPos > 0){ var p = startPos; startPos = 0; w.seekTo(p); }
    });
    w.bind(SC.Widget.Events.PAUSE, function(){
      if (w !== widget) return;
      setIcon(false);
      /* paused from a media key, headphones, the OS, etc: leave it paused, do not skip */
      if (gotPlay && !checking) wantPlay = false;
    });
    w.bind(SC.Widget.Events.FINISH, function(){
      if (w !== widget) return;
      setIcon(false);
      w.getSounds(function(list){
        if (w !== widget) return;
        /* inside an album/set embed, let it roll on to its own next track first */
        if (list && list.length > 1 && lastIdx < list.length - 1) return;
        advance();
      });
    });
    w.bind(SC.Widget.Events.PLAY_PROGRESS, function(e){
      if (w !== widget) return;
      if (e.currentPosition !== lastPos){
        lastPos = e.currentPosition;
        lastProgress = Date.now();
        if (e.currentPosition > 3000) failStreak = 0;
      }
      if (!elSeek.dataset.drag) elSeek.value = Math.round(e.relativePosition * 1000);
    });
    if (SC.Widget.Events.ERROR){
      w.bind(SC.Widget.Events.ERROR, function(){ if (w === widget) skipStuck(); });
    }
  }

  function playItem(item, pos, idx){
    withApi(function(){
      startPos = pos || 0; startIdx = idx || 0; lastIdx = 0;
      wantPlay = true; gotPlay = false; lastProgress = Date.now(); lastPos = -1;
      current = item;
      recent.push(ukey(item.url)); if (recent.length > 40) recent.shift();
      bar.hidden = false;
      document.body.classList.add('sp-active');
      showCurrent(item);
      if (!widget){
        frame = makeFrame(item.url);
        widget = SC.Widget(frame);
        bindBarWidget(widget);
      } else {
        widget.load(item.url, { auto_play: true, hide_related: true, show_comments: false, show_user: true,
          show_reposts: false, show_teaser: false, visual: false,
          callback: function(){ applyVolume(); refreshSound(); } });
      }
      ensureAuto();
      render();
    });
  }
  function playInBar(url, pos, idx){ playItem(itemFor(url, ''), pos, idx); }
  window.undergroundPlayer = { play: playInBar, enqueue: function(url){ enqueue(itemFor(url, '')); } };

  /* ---------------------------------------------------------- queue */
  function pickAuto(){
    if (!playable.length) return null;
    var cur = current ? ukey(current.url) : '';
    var fresh = playable.filter(function(m){ var k = ukey(m.url); return k !== cur && recent.indexOf(k) < 0 && !queueHas(k); });
    if (!fresh.length) fresh = playable.filter(function(m){ return ukey(m.url) !== cur && !queueHas(ukey(m.url)); });
    if (!fresh.length) return null;
    var same = current && current.artist_slug ? fresh.filter(function(m){ return m.artist_slug === current.artist_slug; }) : [];
    var pool = same.length ? same : fresh;
    var m = pool[Math.floor(Math.random() * pool.length)];
    return { url: m.url, title: m.title, sub: m.sub, href: m.href, artist_slug: m.artist_slug, cover: m.cover || '', auto: true };
  }
  function queueHas(k){ return queue.some(function(q){ return ukey(q.url) === k; }); }
  function ensureAuto(){
    if (!current || queue.length) return;
    var p = pickAuto();
    if (p) queue.push(p);
  }
  function enqueue(item){
    if (!current){ playItem(item); return true; }
    queue = queue.filter(function(q){ return !q.auto; });
    if (queue.length >= 100) {
      render();
      return false;
    }
    queue.push(item);
    ensureAuto();
    render();
    return true;
  }
  function advance(){
    if (!queue.length) ensureAuto();
    var nxt = queue.shift();
    if (!nxt){ render(); return; }
    playItem(nxt);
  }
  function removeAt(i){
    queue.splice(i, 1);
    ensureAuto();
    render();
  }
  function moveQueueItem(i, direction){
    var target = i + direction;
    if (target < 0 || target >= queue.length) return;
    var item = queue.splice(i, 1)[0];
    queue.splice(target, 0, item);
    render();
  }
  function jumpTo(i){
    var it = queue.splice(i, 1)[0];
    if (it) playItem(it);
  }
  function render(){
    var manual = queue.filter(function(q){ return !q.auto; }).length;
    elQCount.textContent = manual ? String(manual) : '';
    qNow.textContent = current ? 'Now playing: ' + (current.title || niceName(current.url)) + (current.sub ? ' \u2014 ' + current.sub : '') : '';
    qList.innerHTML = '';
    if (!queue.length){
      var e = document.createElement('li'); e.className = 'sp-queue-empty'; e.textContent = 'Nothing queued yet.'; qList.appendChild(e);
      return;
    }
    queue.forEach(function(it, i){
      var li = document.createElement('li');
      if (it.cover){ var th = document.createElement('img'); th.className = 'sp-q-thumb'; th.alt = ''; th.src = it.cover; li.appendChild(th); }
      var main = document.createElement('button');
      main.type = 'button'; main.className = 'sp-q-main'; main.title = 'Play this now';
      var t = document.createElement('span'); t.className = 'sp-q-title'; t.textContent = it.title || niceName(it.url);
      var sub = document.createElement('span'); sub.className = 'sp-q-sub'; sub.textContent = it.sub || '';
      main.appendChild(t); main.appendChild(sub);
      main.addEventListener('click', function(){ jumpTo(i); });
      li.appendChild(main);
      if (it.auto){ var tag = document.createElement('span'); tag.className = 'sp-q-tag'; tag.textContent = 'suggested'; li.appendChild(tag); }

      var move = document.createElement('span');
      move.className = 'sp-q-move';

      var up = document.createElement('button');
      up.type = 'button';
      up.innerHTML = '&#9650;';
      up.title = i === 0 ? 'Already at the top' : 'Move up';
      up.setAttribute('aria-label', i === 0 ? 'Already at the top' : 'Move up');
      up.disabled = i === 0;
      up.addEventListener('click', function(e){ e.stopPropagation(); moveQueueItem(i, -1); });

      var down = document.createElement('button');
      down.type = 'button';
      down.innerHTML = '&#9660;';
      down.title = i === queue.length - 1 ? 'Already at the bottom' : 'Move down';
      down.setAttribute('aria-label', i === queue.length - 1 ? 'Already at the bottom' : 'Move down');
      down.disabled = i === queue.length - 1;
      down.addEventListener('click', function(e){ e.stopPropagation(); moveQueueItem(i, 1); });

      move.appendChild(up);
      move.appendChild(down);
      li.appendChild(move);

      var rm = document.createElement('button');
      rm.type = 'button'; rm.setAttribute('aria-label', 'Remove from queue'); rm.title = 'Remove'; rm.innerHTML = '&#10005;';
      rm.addEventListener('click', function(){ removeAt(i); });
      li.appendChild(rm);
      qList.appendChild(li);
    });
  }
  function setPanel(open){
    panel.hidden = !open;
    btnQueue.setAttribute('aria-expanded', open ? 'true' : 'false');
    if (open) render();
  }
  btnQueue.addEventListener('click', function(){ setPanel(panel.hidden); });
  qClear.addEventListener('click', function(){ queue = []; ensureAuto(); render(); });
  btnNext.addEventListener('click', function(){ advance(); });

  /* ---------------------------------------------------------- bar controls */
  btnToggle.addEventListener('click', togglePlay);
  btnMute.addEventListener('click', toggleMute);
  elVol.addEventListener('input', function(){
    vol = parseInt(elVol.value, 10) || 0;
    muted = false;
    applyVolume();
    try { localStorage.setItem(VOL_KEY, String(vol)); } catch(e) {}
  });
  elSeek.addEventListener('input', function(){ elSeek.dataset.drag = '1'; });
  elSeek.addEventListener('change', function(){
    delete elSeek.dataset.drag;
    if (!widget) return;
    var frac = parseInt(elSeek.value, 10) / 1000;
    widget.getDuration(function(d){ widget.seekTo(d * frac); });
  });
  btnClose.addEventListener('click', function(){
    wantPlay = false; failStreak = 0;
    resetWidget();
    current = null; queue = [];
    setIcon(false);
    setPanel(false);
    render();
    bar.hidden = true;
    document.body.classList.remove('sp-active');
  });
  btnShare.addEventListener('click', function(){
    if (!shareUrl) return;
    if (navigator.share){
      navigator.share({ title: shareTitle, url: shareUrl }).catch(function(){});
      return;
    }
    var done = function(){ var old = btnShare.textContent; btnShare.textContent = 'Copied'; setTimeout(function(){ btnShare.textContent = old; }, 1500); };
    if (navigator.clipboard && navigator.clipboard.writeText){ navigator.clipboard.writeText(shareUrl).then(done, function(){ window.open(shareUrl, '_blank', 'noopener'); }); }
    else { window.open(shareUrl, '_blank', 'noopener'); }
  });

  /* ---------------------------------------------------------- keyboard: space = play/pause, m = mute */
  function typing(t){
    if (!t || !t.tagName) return false;
    var n = t.tagName;
    if (n === 'TEXTAREA' || n === 'SELECT' || t.isContentEditable) return true;
    if (n === 'INPUT') return (t.type || '').toLowerCase() !== 'range';
    return false;
  }
  document.addEventListener('keydown', function(e){
    if (e.ctrlKey || e.metaKey || e.altKey) return;
    if (e.key === 'Escape' && !panel.hidden){ setPanel(false); return; }
    if (!widget || bar.hidden || typing(e.target)) return;
    if (e.code === 'Space' || e.key === ' '){
      e.preventDefault();
      if (!e.repeat) togglePlay();
    } else if (e.key === 'm' || e.key === 'M'){
      e.preventDefault();
      if (!e.repeat) toggleMute();
    }
  });
  document.addEventListener('keyup', function(e){
    if ((e.code === 'Space' || e.key === ' ') && widget && !bar.hidden && !typing(e.target)) e.preventDefault();
  });

  /* ---------------------------------------------------------- the catalog's playable songs */
  function decorateTracks(){
    if (!playable.length) return;
    document.querySelectorAll('.page a.track-main').forEach(function(a){
      if (a.dataset.spDec) return;
      a.dataset.spDec = '1';
      var m = byHref[a.pathname];
      if (!m) return;
      var wrap = document.createElement('span');
      wrap.className = 'sp-rowbtns';
      var play = document.createElement('button');
      play.type = 'button'; play.textContent = '\u25B6'; play.title = 'Play in the Underground Catalog player';
      play.addEventListener('click', function(e){ e.preventDefault(); e.stopPropagation(); playItem(itemFor(m.url, m.title)); });
      var add = document.createElement('button');
      add.type = 'button'; add.textContent = '+ Queue'; add.title = 'Add to the queue';
      add.addEventListener('click', function(e){
        e.preventDefault(); e.stopPropagation();
        if (enqueue(itemFor(m.url, m.title))) {
          add.textContent = 'Added';
        } else {
          add.textContent = 'Queue Full';
        }
        setTimeout(function(){ add.textContent = '+ Queue'; }, 1200);
      });
      wrap.appendChild(play); wrap.appendChild(add);
      a.insertAdjacentElement('afterend', wrap);
    });
  }
  fetch("{{ url_for('api_playable') }}", { credentials: 'same-origin' })
    .then(function(r){ return r.json(); })
    .then(function(data){
      playable = (data && data.songs) || [];
      playable.forEach(function(m){ byHref[m.href] = m; byUrl[ukey(m.url)] = m; });
      if (current && !current.artist_slug){
        var m = byUrl[ukey(current.url)];
        if (m){ current.title = current.title || m.title; current.sub = current.sub || m.sub; current.artist_slug = m.artist_slug; current.cover = current.cover || m.cover || ''; current.href = current.href || m.href; showCurrent(current); }
      }
      ensureAuto();
      render();
      decorateTracks();
    })
    .catch(function(){});

  /* ---------------------------------------------------------- on-page embeds keep working */
  function embedUrl(f){
    try { return new URL(f.src).searchParams.get('url'); } catch(e) { return null; }
  }
  function embedItem(f){
    var h = document.querySelector('.page h1');
    var it = itemFor(embedUrl(f), h ? h.textContent.trim() : '');
    if (!it.cover){ var im = document.querySelector('.page img.cover'); if (im) it.cover = im.getAttribute('src') || ''; }
    if (!it.href) it.href = location.pathname;
    return it;
  }
  function handoff(f){
    var url = embedUrl(f);
    if (!url || !f._w) return;
    f._w.getCurrentSoundIndex(function(i){
      f._w.getPosition(function(ms){
        f._w.pause();
        playItem(embedItem(f), ms, i || 0);
      });
    });
  }
  function mkBtn(label, cls, fn){
    var b = document.createElement('button');
    b.type = 'button'; b.className = cls; b.textContent = label;
    b.addEventListener('click', function(){ fn(b); });
    return b;
  }
  function bindPageEmbeds(){
    if (!(window.SC && SC.Widget)) return;
    document.querySelectorAll('.page .embed iframe').forEach(function(f){
      if (f.dataset.spBound || (f.src || '').indexOf('w.soundcloud.com') < 0) return;
      f.dataset.spBound = '1';
      f._w = SC.Widget(f);
      f._playing = false;
      f._w.bind(SC.Widget.Events.PLAY, function(){
        f._playing = true;
        if (widget){ wantPlay = false; if (barPlaying) widget.pause(); }
      });
      f._w.bind(SC.Widget.Events.PAUSE, function(){ f._playing = false; });
      f._w.bind(SC.Widget.Events.FINISH, function(){ f._playing = false; });
      var wrap = f.closest('.embed');
      if (wrap && embedUrl(f)){
        var box = document.createElement('div');
        box.className = 'sp-actions';
        box.appendChild(mkBtn('\u25B6 Play in the Underground Catalog player', 'sp-popout', function(){ handoff(f); }));
        box.appendChild(mkBtn('+ Add to queue', 'sp-popout', function(b){
          if (enqueue(embedItem(f))) {
            b.textContent = 'Added to queue';
          } else {
            b.textContent = 'Queue Full';
          }
          setTimeout(function(){ b.textContent = '+ Add to queue'; }, 1400);
        }));
        wrap.parentNode.insertBefore(box, wrap.nextSibling);
      }
    });
  }
  function handoffPlayingEmbeds(){
    document.querySelectorAll('.page .embed iframe').forEach(function(f){
      if (f._playing) handoff(f);
    });
  }

  /* ---------------------------------------------------------- page-swap click sound */
  var clickAudio = null;

  function playClickSound(){
    try {
      var enabled = localStorage.getItem('undergroundCatalogClickSound') === 'on';
      if (!enabled) return;

      if (!clickAudio) {
        clickAudio = new Audio('/images/click-sound.mp3');
        clickAudio.preload = 'auto';
      }

      clickAudio.currentTime = 0;
      var promise = clickAudio.play();
      if (promise && promise.catch) promise.catch(function(){});
    } catch(e) {}
  }

  /* ---------------------------------------------------------- page-swap navigation */
  var pageEl = document.querySelector('.page');
  var navToken = 0;
  function rerunScripts(root){
    root.querySelectorAll('script').forEach(function(old){
      var n = document.createElement('script');
      for (var i = 0; i < old.attributes.length; i++) n.setAttribute(old.attributes[i].name, old.attributes[i].value);
      n.text = old.textContent;
      old.parentNode.replaceChild(n, old);
    });
  }
  function afterSwap(){
    rerunScripts(pageEl);
    if (window.captureReleaseGroups) window.captureReleaseGroups();
    if (window.setReleaseOrder){
      var order = 'oldest';
      try { order = localStorage.getItem('undergroundCatalogDefaultSort') === 'newest' ? 'newest' : 'oldest'; } catch(e) {}
      window.setReleaseOrder(order);
    }
    bindPageEmbeds();
    decorateTracks();
  }
  function go(url, push){
    var token = ++navToken;
    handoffPlayingEmbeds();
    fetch(url, { headers: { 'X-Requested-With': 'page-swap' }, credentials: 'same-origin' })
      .then(function(r){
        var ct = r.headers.get('content-type') || '';
        if (ct.indexOf('text/html') < 0) throw new Error('not html');
        return r.text().then(function(t){ return { url: r.url, text: t }; });
      })
      .then(function(res){
        if (token !== navToken) return;
        var doc = new DOMParser().parseFromString(res.text, 'text/html');
        var next = doc.querySelector('.page');
        if (!next) throw new Error('no page');
        pageEl.innerHTML = next.innerHTML;
        document.title = doc.title || document.title;
        if (push) history.pushState({ sp: 1 }, '', res.url);
        window.scrollTo(0, 0);
        afterSwap();
      })
      .catch(function(){ window.location.href = url; });
  }
  document.addEventListener('click', function(e){
    if (e.defaultPrevented || e.button !== 0 || e.metaKey || e.ctrlKey || e.shiftKey || e.altKey) return;
    var a = e.target.closest ? e.target.closest('a[href]') : null;
    if (!a || !pageEl) return;
    var inPage = pageEl.contains(a);
    var inChrome = a.hasAttribute('data-spa') || a.classList.contains('random-song-button') || !!a.closest('.site-footer');
    if (!inPage && !inChrome) return;
    if (a.target && a.target !== '_self') return;
    if (a.hasAttribute('download')) return;
    var u;
    try { u = new URL(a.href, location.href); } catch(err) { return; }
    if (u.origin !== location.origin) return;
    if (u.pathname.indexOf('/images/') === 0 || u.pathname.indexOf('/static/') === 0) return;
    if (u.pathname === location.pathname && u.search === location.search && u.hash) return;
    e.preventDefault();
    playClickSound();
    go(u.href, true);
  });
  window.addEventListener('popstate', function(){ go(location.href, false); });
  window.addEventListener('load', bindPageEmbeds);
  if (document.readyState === 'complete') bindPageEmbeds();
})();
</script>
</body>
</html>
"""

# Small inline marks for the three services. Greyed out when there's no link.
LOGOS = """
{% macro spotify() %}
<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="11" fill="currentColor"/>
<g stroke="var(--paper)" stroke-width="1.9" fill="none" stroke-linecap="round">
<path d="M6.4 9.1c3.7-1.1 7.9-.7 11 1.2"/><path d="M7.3 12.3c3.1-.9 6.6-.5 9.2 1"/>
<path d="M8.2 15.4c2.5-.7 5.2-.4 7.2.8"/></g></svg>
{% endmacro %}
{% macro youtube() %}
<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="11" fill="currentColor"/>
<path d="M10 8.2l6 3.8-6 3.8z" fill="var(--paper)"/></svg>
{% endmacro %}
{% macro soundcloud() %}
<svg viewBox="0 0 24 24" aria-hidden="true" fill="currentColor">
<rect x="1.5" y="13" width="1.7" height="5" rx=".85"/>
<rect x="4.6" y="11" width="1.7" height="7" rx=".85"/>
<rect x="7.7" y="9.4" width="1.7" height="8.6" rx=".85"/>
<path d="M11.4 18V9.3c.9-1.7 2.7-2.8 4.7-2.8 2.9 0 5.2 2.2 5.4 5 1.4.4 2.3 1.6 2.3 3 0 1.9-1.5 3.5-3.4 3.5z"/></svg>
{% endmacro %}
"""

PLATFORM_ROW = """
{% import "logos.html" as logos %}
{% macro platforms(links) %}
<div class="platforms">
  {% set services = [
      ('spotify', 'Spotify', logos.spotify()),
      ('youtube_music', 'YouTube Music', logos.youtube()),
      ('soundcloud', 'SoundCloud', logos.soundcloud())
  ] %}
  {% for key, label, mark in services %}
    {% if links.get(key) %}
      <a class="platform rounded-2xl shadow-lg transition-all duration-300" href="{{ links[key] }}" target="_blank" rel="noopener">{{ mark }}{{ label }}</a>
    {% else %}
      <span class="platform off rounded-2xl shadow-md transition-all duration-300" title="No {{ label }} link yet">{{ mark }}{{ label }}</span>
    {% endif %}
  {% endfor %}
</div>
{% endmacro %}
"""

COVER_BLOCK = """
{% macro cover(filename, alt, shadow='') %}
  {% if has_image(filename) %}
    <img class="cover rounded-2xl shadow-2xl transition-all duration-300 {{ shadow }}" src="{{ url_for('image', filename=filename) }}" alt="{{ alt }}">
  {% else %}
    <div class="cover placeholder rounded-2xl shadow-xl transition-all duration-300 {{ shadow }}" role="img" aria-label="No cover art for {{ alt }}">
      <span>No cover yet</span>
    </div>
  {% endif %}
{% endmacro %}
"""

LISTEN_BLOCK = """
{% macro listen(url) %}
  {% if url %}
    {% if is_soundcloud(url) %}
      <div class="embed">
        <iframe width="100%" height="177" scrolling="no" frameborder="no" allow="autoplay"
                loading="lazy" title="SoundCloud player"
                src="{{ soundcloud_embed_src(url) }}"></iframe>
      </div>
    {% else %}
      <a class="listen rounded-2xl shadow-xl transition-all duration-300" href="{{ url }}" target="_blank" rel="noopener">Play now</a>
    {% endif %}
  {% endif %}
{% endmacro %}
"""

VIDEO_BLOCK = """
{% macro video(value) %}
  {% for v in split_music_videos(value) %}
    {% set vid = youtube_video_id(v) %}
    {% if vid %}
      <div class="embed video">
        <iframe width="560" height="315" src="{{ youtube_embed_src(v) }}"
                title="YouTube video player"
                allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
                allowfullscreen loading="lazy"></iframe>
      </div>
    {% else %}
      <a class="listen rounded-2xl shadow-xl transition-all duration-300" href="{{ v }}" target="_blank" rel="noopener">Watch music video</a>
    {% endif %}
  {% endfor %}
{% endmacro %}
"""

INDEX = """
{% extends "layout.html" %}
{% import "cover.html" as art %}
{% block title %}Underground Catalog{% endblock %}
{% block masthead %}<span class="count">{{ artists|length }} Underground Rappers · {{ track_count }} Tracks</span>{% endblock %}
{% block content %}
<div class="index-top">
  <div>
    <p class="lede">Underground Rappers, Tracks, Singles, Producers, Collectives.</p>

    <label class="visually-hidden" for="filter" hidden>Search artists, producers, or tracks</label>
    <input class="filter rounded-2xl shadow-lg transition-all duration-300 focus:ring-2 focus:ring-blue-500/30" id="filter" type="search" placeholder="Search artists, producers, or tracks"
           autocomplete="off" oninput="runHomeSearch(this.value)">
  </div>

  {% if newest_releases or top_producers %}
  <aside class="side-panels">
    {% if newest_releases %}
    <div class="newest-panel rounded-2xl shadow-xl transition-all duration-300">
      <h2>Newest Underground Rap Releases:</h2>
      {% for item in newest_releases %}
      <a class="newest-item" href="{{ item.url }}">
        {{ art.cover(item.cover, item.title ~ ' cover') }}
        <div>
          <p class="newest-title">{{ item.title }}</p>
          <p class="newest-meta">{{ item.artist_name }} · {{ item.kind_label }}{% if item.year %} · {{ item.year }}{% endif %}</p>
          {% if item.track_count %}<p class="newest-meta">{{ item.track_count }} track{{ '' if item.track_count == 1 else 's' }}</p>{% endif %}
          {% if item.features %}<p class="newest-meta">Featuring {{ item.features|join(', ') }}</p>{% endif %}
          {% if item.producers %}<p class="newest-meta">Produced by {{ item.producers|join(', ') }}</p>{% endif %}
        </div>
      </a>
      {% endfor %}
    </div>
    {% endif %}


    {% if top_producers %}
    <div class="top-producers-panel rounded-2xl shadow-xl transition-all duration-300">
      <h2>Top 5 Producers</h2>
      <ol class="top-producers-list">
        {% for p in top_producers %}
        <li><a href="{{ p.url }}">
          <span class="rank">#{{ loop.index }}</span>
          <span class="pname">{{ p.name }}</span>
          <span class="pcount">{{ p.credit_count }} credit{{ '' if p.credit_count == 1 else 's' }}</span>
        </a></li>
        {% endfor %}
      </ol>
    </div>
    {% endif %}
  </aside>
  {% endif %}
</div>

<div id="roster-view">
<ul class="roster" id="roster">
{% for a in artists %}
  <li>
    <a href="{{ url_for('artist', slug=a.slug) }}">
      {% if has_image(a.image) %}
        <img class="thumb" src="{{ url_for('image', filename=a.image) }}" alt="">
      {% else %}
        <div class="thumb placeholder"><span>{{ a.initials }}</span></div>
      {% endif %}
      <span>
        <span class="name">{{ a.name }}</span>
        {% if a.aliases %}<br><span class="alias">AKA / FKA: {{ a.aliases|join(', ') }}</span>{% endif %}
      </span>
      <span class="tally">
        {{ a.projects|length }} release{{ '' if a.projects|length == 1 else 's' }}
        {%- if a.singles %} · {{ a.singles|length }} single{{ '' if a.singles|length == 1 else 's' }}{% endif %}
      </span>
    </a>
  </li>
{% else %}
  <li><p class="empty" style="padding:22px 0">No artists yet.</p></li>
{% endfor %}
</ul>
</div>

<div id="search-results" hidden>
  <ul class="prodlist" id="results-list"></ul>
  <p class="empty" id="no-results" hidden>No matches.</p>
  <div class="pager" id="results-pager"></div>
</div>

<script type="application/json" id="search-index">{{ search_index|safe }}</script>
<script>
var HOME_SEARCH_INDEX = JSON.parse(document.getElementById('search-index').textContent);
var HOME_TYPE_LABELS = {artist: 'Artist', producer: 'Producer', track: 'Track', single: 'Single'};
var HOME_PAGE_SIZE = 30;
var homeSearch = { matches: [], page: 1 };

window.applySinglesOnlyToSearch = function(){
  var filter = document.getElementById('filter');
  if (filter && filter.value) runHomeSearch(filter.value);
};

function runHomeSearch(term){
  term = term.trim().toLowerCase();
  var rosterView = document.getElementById('roster-view');
  var resultsView = document.getElementById('search-results');

  if (!term){
    rosterView.hidden = false;
    resultsView.hidden = true;
    return;
  }
  rosterView.hidden = true;
  resultsView.hidden = false;

  homeSearch.matches = HOME_SEARCH_INDEX.filter(function(e){
    if (document.documentElement.classList.contains('singles-only') &&
        e.type !== 'single' && e.type !== 'artist' && e.type !== 'producer') return false;
    return e.title.toLowerCase().includes(term) || (e.sub || '').toLowerCase().includes(term);
  });
  homeSearch.page = 1;
  renderHomeSearchPage();
}

function renderHomeSearchPage(){
  var start = (homeSearch.page - 1) * HOME_PAGE_SIZE;
  var pageItems = homeSearch.matches.slice(start, start + HOME_PAGE_SIZE);
  renderSearchResults(pageItems, document.getElementById('results-list'),
                       document.getElementById('no-results'), HOME_TYPE_LABELS);
  renderPager(document.getElementById('results-pager'), homeSearch.matches.length, HOME_PAGE_SIZE,
              homeSearch.page, function(page){
    homeSearch.page = page;
    renderHomeSearchPage();
  });
}
</script>

{% endblock %}
"""

ARTIST = """
{% extends "layout.html" %}
{% import "platforms.html" as ui %}
{% import "cover.html" as art %}
{% import "credit-hover.html" as credit %}
{% block title %}{{ artist.name }}{% endblock %}
{% block masthead %}<a class="backlink" href="{{ url_for('index') }}">All Underground Rappers</a>{% endblock %}
{% block content %}

<div class="hero">
  {% if has_image(artist.image) %}
    <img class="portrait" src="{{ url_for('image', filename=artist.image) }}" alt="{{ artist.name }}">
  {% else %}
    <div class="portrait placeholder" role="img" aria-label="No photo of {{ artist.name }}">
      <span>{{ artist.initials }}</span></div>
  {% endif %}

  <div>
    <h1>{{ artist.name }}</h1>
    <ul class="facts">
      {% if artist.aliases %}<li><b>Also known as</b><span>{{ artist.aliases|join(', ') }}</span></li>{% endif %}
      {% if artist.dob %}<li><b>Born</b><span>{{ artist.dob }}</span></li>{% endif %}
      {% if artist.collectives %}
      <li><b>Collective</b><span>
        {% for name in artist.collectives %}
          {% set link = collective_link(name) %}
          {% if link %}<a href="{{ link }}">{{ name }}</a>{% else %}{{ name }}{% endif -%}
          {%- if not loop.last %}, {% endif %}
        {% endfor %}
      </span></li>
      {% endif %}
    </ul>

    {% if artist.dead %}
    <div class="artist-rip">
      <img src="{{ url_for('image', filename='rip.jpg') }}" alt="RIP">
      <span>This artist has unfortunately passed away</span>
    </div>
    {% endif %}

    {{ ui.platforms(artist.links) }}

    {% if producer_credits %}
    <div class="modetoggle rounded-2xl shadow-lg transition-all duration-300">
      <button type="button" data-mode="artist" class="{{ 'active' if start_mode == 'artist' }}"
              onclick="setMode('artist')">Artist</button>
      <button type="button" data-mode="producer" class="{{ 'active' if start_mode == 'producer' }}"
              onclick="setMode('producer')">Producer</button>
    </div>
    {% endif %}
  </div>
</div>

<div class="mode-panel {{ 'active' if start_mode == 'artist' }}" data-mode="artist">

{% if artist.projects or artist.singles or featured_singles %}
<label class="visually-hidden" for="track-filter" hidden>Search {{ artist.name }}'s tracks</label>
<input class="filter rounded-2xl shadow-lg transition-all duration-300 focus:ring-2 focus:ring-blue-500/30" id="track-filter" type="search" placeholder="Search {{ artist.name }}'s tracks"
       autocomplete="off" oninput="runArtistTrackSearch(this.value)">
{% endif %}

{% if sorted_projects or sorted_singles %}
<div class="sorttoggle-row">
  <span class="sortlabel">Sort by date:</span>
  <div class="modetoggle sorttoggle rounded-2xl shadow-lg transition-all duration-300">
    <button type="button" data-order="oldest" class="active" onclick="setReleaseOrder('oldest')">Oldest first</button>
    <button type="button" data-order="newest" onclick="setReleaseOrder('newest')">Newest first</button>
  </div>
</div>
{% endif %}

<div id="releases-view">
<div class="section-head" id="album-release-heading">
  <h2>Albums &amp; EPs</h2>
  <span>{{ sorted_projects|length }} release{{ '' if sorted_projects|length == 1 else 's' }}</span>
</div>

<div id="album-releases">
<div id="projects-list">
{% for p in sorted_projects %}
<article class="release">
  <div>{{ art.cover(p.cover, p.title ~ ' cover') }}</div>
  <div>
    <h3><a href="{{ url_for('project', slug=p.owner_slug or artist.slug, project_slug=p.slug) }}">{{ p.title }}</a></h3>
    <p class="kindline">{{ p.kind }}{% if p.year %} · {{ p.year }}{% endif %}
      {%- if p.tracks %} · {{ p.tracks|length }} tracks{% endif -%}
      {%- if p.owner_slug %} · with {% set owner_link = url_for('artist', slug=p.owner_slug) %}{{ credit.artist(p.owner_name, owner_link) }}{% endif %}</p>

    {% if p.tracks %}
    <ol class="tracklist">
      {% for t in p.tracks %}
      <li>
        <div class="track-row">
          <span class="num">{{ '%02d' % t.number }}</span>
          <span>
            <a class="track-main" href="{{ track_hrefs['track:' ~ p.slug ~ ':' ~ t.index] }}">{{ t.title }}</a>
            {% if t.features %}<span class="feat"> with {% for f in t.features %}{% set link = artist_link(f) %}{% if link %}{{ credit.artist(f, link) }}{% else %}{{ f }}{% endif %}{% if not loop.last %}, {% endif %}{% endfor %}</span>{% endif %}
          </span>
        </div>
      </li>
      {% endfor %}
    </ol>
    {% else %}
    <p class="empty">Tracklist not added yet.</p>
    {% endif %}
  </div>
</article>
{% else %}
<p class="empty">No albums or EPs logged yet.</p>
{% endfor %}
</div>
</div>

{% if sorted_singles %}
<div class="section-head"><h2>Singles</h2>
  <span>{{ sorted_singles|length }} track{{ '' if sorted_singles|length == 1 else 's' }}</span></div>
<div class="singles" id="singles-grid">
  {% for s in sorted_singles %}
  {% if s.owner_slug %}
  <a href="{{ url_for('single', slug=s.owner_slug, single_slug=s.slug) }}">
    {{ art.cover(s.cover, s.title ~ ' cover', 'blue') }}
    <h3>{{ s.title }}</h3>
    <p class="meta">{% if s.year %}{{ s.year }} · {% endif %}featured on {{ s.owner_name }}</p>
  </a>
  {% else %}
  <a href="{{ url_for('single', slug=artist.slug, single_slug=s.slug) }}">
    {{ art.cover(s.cover, s.title ~ ' cover', 'blue') }}
    <h3>{{ s.title }}</h3>
    {% if s.year %}<p class="meta">{{ s.year }}</p>{% endif %}
  </a>
  {% endif %}
  {% endfor %}
</div>
{% endif %}

</div>{# /releases-view #}

<div id="track-search-results" hidden>
  <ul class="prodlist" id="track-results-list"></ul>
  <p class="empty" id="no-track-results" hidden>No matching tracks.</p>
</div>

<script type="application/json" id="track-index">{{ track_index|safe }}</script>
<script>
(function(){
  var el = document.getElementById('track-index');
  if (!el) return;
  var ARTIST_TRACK_INDEX = JSON.parse(el.textContent);
  window.applySinglesOnlyToSearch = function(){
    var filter = document.getElementById('track-filter');
    if (filter && filter.value) window.runArtistTrackSearch(filter.value);
  };
  window.runArtistTrackSearch = function(term){
    term = term.trim().toLowerCase();
    var releasesView = document.getElementById('releases-view');
    var resultsView = document.getElementById('track-search-results');

    if (!term){
      releasesView.hidden = false;
      resultsView.hidden = true;
      return;
    }
    releasesView.hidden = true;
    resultsView.hidden = false;

    var matches = ARTIST_TRACK_INDEX.filter(function(e){
      if (document.documentElement.classList.contains('singles-only') && e.type !== 'single') return false;
      return e.title.toLowerCase().includes(term);
    });

    renderSearchResults(matches, document.getElementById('track-results-list'),
                         document.getElementById('no-track-results'), null);
  };
})();
</script>

</div>{# /mode-panel artist #}

{% if producer_credits %}
<div class="mode-panel {{ 'active' if start_mode == 'producer' }}" data-mode="producer">
<div class="section-head">
  <h2>Produced</h2>
  <span>{{ producer_credits|length }} credit{{ '' if producer_credits|length == 1 else 's' }}</span>
</div>
<ul class="prodlist">
  {% for c in producer_credits %}
  <li{% if c.kind == 'track' %} class="album-track-credit"{% endif %}>
    {% if c.kind == 'track' %}
    <a class="row" href="{{ url_for('track', slug=c.artist_slug, project_slug=c.project_slug, track_slug=c.track_slug) }}">
      <span>{{ c.track_title }}</span>
      <span class="who">{{ c.artist_name }} · {{ c.project_title }}</span>
      <span class="kind">Track{% if c.year %} · {{ c.year }}{% endif %}</span>
    </a>
    {% else %}
    <a class="row" href="{{ url_for('single', slug=c.artist_slug, single_slug=c.single_slug) }}">
      <span>{{ c.single_title }}</span>
      <span class="who">{{ c.artist_name }}</span>
      <span class="kind">Single{% if c.year %} · {{ c.year }}{% endif %}</span>
    </a>
    {% endif %}
  </li>
  {% endfor %}
</ul>
</div>
{% endif %}
{% endblock %}
"""

CREDIT_HOVER = """
{% macro artist(name, link) %}
{% set info = artist_hover_info(name) %}
{% if info and link %}
<span class="credit-hover">
  <a href="{{ link }}">{{ name }}</a>
  <span class="artist-hover-card" aria-hidden="true">
    <span class="artist-hover-name">{{ info.name }}</span>
    <span class="artist-hover-stats">{{ info.projects }} project{{ '' if info.projects == 1 else 's' }} · {{ info.songs }} song{{ '' if info.songs == 1 else 's' }}</span>
    {% if has_image(info.image) %}
      <img class="artist-hover-image" src="{{ url_for('image', filename=info.image) }}" alt="">
    {% else %}
      <span class="artist-hover-image artist-hover-placeholder">{{ info.name[:2]|upper }}</span>
    {% endif %}
  </span>
</span>
{% else %}
{{ name }}
{% endif %}
{% endmacro %}
"""

PROJECT = """
{% extends "layout.html" %}
{% import "cover.html" as art %}
{% import "platforms.html" as ui %}
{% import "listen.html" as play %}
{% import "video.html" as mv %}
{% import "credit-hover.html" as credit %}
{% block title %}{{ project.title }} — {{ artist.name }}{% endblock %}
{% block masthead %}<a class="backlink" href="{{ url_for('artist', slug=artist.slug) }}">Back to {{ artist.name }}</a>{% endblock %}
{% block content %}
<div class="detail">
  <div>{{ art.cover(project.cover, project.title ~ ' cover') }}</div>
  <div>
    <h1>{{ project.title }}</h1>
    <p class="kindline">{{ project.kind }}{% if project.year %} · {{ project.year }}{% endif %}
      · {{ artist.name }}
      {%- if project.collab %} · with {% for c in project.collab %}{% set link = artist_link(c) %}{% if link %}{{ credit.artist(c, link) }}{% else %}{{ c }}{% endif %}{% if not loop.last %}, {% endif %}{% endfor %}{% endif %}</p>
    {{ play.listen(project.url) }}

    {% if project.tracks %}
    <ol class="tracklist">
      {% for t in project.tracks %}
      <li>
        <div class="track-row">
          <span class="num">{{ '%02d' % t.number }}</span>
          <span>
            <a class="track-main" href="{{ track_hrefs['track:' ~ project.slug ~ ':' ~ t.index] }}">{{ t.title }}</a>
            {% if t.features %}<span class="feat"> with {% for f in t.features %}{% set link = artist_link(f) %}{% if link %}{{ credit.artist(f, link) }}{% else %}{{ f }}{% endif %}{% if not loop.last %}, {% endif %}{% endfor %}</span>{% endif %}
          </span>
        </div>
      </li>
      {% endfor %}
    </ol>
    {% endif %}

    {{ mv.video(project.music_video) }}
    {{ ui.platforms(artist.links) }}
  </div>
</div>
{% endblock %}
"""

TRACK = """
{% extends "layout.html" %}
{% import "cover.html" as art %}
{% import "listen.html" as play %}
{% import "credit-hover.html" as credit %}
{% block title %}{{ track.title }} — {{ artist.name }}{% endblock %}
{% block masthead %}<a class="backlink" href="{{ url_for('project', slug=artist.slug, project_slug=project.slug) }}">Back to {{ project.title }}</a>{% endblock %}
{% block content %}
<div class="detail">
  <div>{{ art.cover(project.cover, project.title ~ ' cover', 'blue') }}</div>
  <div>
    <h1>{{ track.title }}</h1>
    <p class="kindline">Track {{ '%02d' % track.number }} on
      <a href="{{ url_for('project', slug=artist.slug, project_slug=project.slug) }}">{{ project.title }}</a></p>
    <ul class="credits">
      <li><b>Artist</b><span>{{ artist.name }}</span></li>
      {% if track.features %}<li><b>Features</b><span>{% for f in track.features %}{% set link = artist_link(f) %}{% if link %}{{ credit.artist(f, link) }}{% else %}{{ f }}{% endif %}{% if not loop.last %}, {% endif %}{% endfor %}</span></li>{% endif %}
      {% if track.producers %}<li><b>Produced by</b><span>
        {% for p in track.producers %}{% set link = artist_link(p) %}{% if link %}{{ credit.artist(p, link ~ '?mode=producer') }}{% else %}<a href="{{ producer_link(p) }}">{{ p }}</a>{% endif %}{% if not loop.last %}, {% endif %}{% endfor %}
      </span></li>{% endif %}
      {% if project.year %}<li><b>Released</b><span>{{ project.year }}</span></li>{% endif %}
    </ul>
    {{ play.listen(track.url) }}
  </div>
</div>
{% endblock %}
"""

SINGLE = """
{% extends "layout.html" %}
{% import "cover.html" as art %}
{% import "listen.html" as play %}
{% import "video.html" as mv %}
{% import "credit-hover.html" as credit %}
{% block title %}{{ single.title }} — {{ artist.name }}{% endblock %}
{% block masthead %}<a class="backlink" href="{{ url_for('artist', slug=artist.slug) }}">Back to {{ artist.name }}</a>{% endblock %}
{% block content %}
<div class="detail">
  <div>{{ art.cover(single.cover, single.title ~ ' cover', 'blue') }}</div>
  <div>
    <h1>{{ single.title }}</h1>
    <p class="kindline">Single{% if single.year %} · {{ single.year }}{% endif %} · {{ artist.name }}</p>
    <ul class="credits">
      {% if single.features %}<li><b>Features</b><span>{% for f in single.features %}{% set link = artist_link(f) %}{% if link %}{{ credit.artist(f, link) }}{% else %}{{ f }}{% endif %}{% if not loop.last %}, {% endif %}{% endfor %}</span></li>{% endif %}
      {% if single.producers %}<li><b>Produced by</b><span>
        {% for p in single.producers %}{% set link = artist_link(p) %}{% if link %}{{ credit.artist(p, link ~ '?mode=producer') }}{% else %}<a href="{{ producer_link(p) }}">{{ p }}</a>{% endif %}{% if not loop.last %}, {% endif %}{% endfor %}
      </span></li>{% endif %}
    </ul>
    {{ play.listen(single.url) }}
    {{ mv.video(single.music_video) }}
  </div>
</div>
{% endblock %}
"""

COLLECTIVE = """
{% extends "layout.html" %}
{% block title %}{{ collective.name }}{% endblock %}
{% block masthead %}<a class="backlink" href="{{ url_for('index') }}">All Underground Rappers</a>{% endblock %}
{% block content %}
<div class="hero">
  {% if has_image(collective.image) %}
    <img class="portrait" src="{{ url_for('image', filename=collective.image) }}" alt="{{ collective.name }}">
  {% else %}
    <div class="portrait placeholder" role="img" aria-label="No image for {{ collective.name }}">
      <span>{{ collective.name[:2]|upper }}</span></div>
  {% endif %}
  <div>
    <h1>{{ collective.name }}</h1>
  </div>
</div>

<div class="section-head"><h2>Current members</h2>
  <span>{{ collective.current_members|length }}</span></div>
{% if collective.current_members %}
<ul class="members">
  {% for m in collective.current_members %}
    {% set link = member_link(m) %}
    <li>{% if link %}<a href="{{ link }}">{{ m }}</a>{% else %}{{ m }}{% endif %}</li>
  {% endfor %}
</ul>
{% else %}
<p class="empty">No current members added yet.</p>
{% endif %}

{% if collective.former_members %}
<div class="section-head"><h2>Former members</h2>
  <span>{{ collective.former_members|length }}</span></div>
<ul class="members">
  {% for m in collective.former_members %}
    {% set link = member_link(m) %}
    <li>{% if link %}<a href="{{ link }}">{{ m }}</a>{% else %}{{ m }}{% endif %}</li>
  {% endfor %}
</ul>
{% endif %}
{% endblock %}
"""

PRODUCER = """
{% extends "layout.html" %}
{% block title %}{{ producer.name }}{% endblock %}
{% block masthead %}<a class="backlink" href="{{ url_for('index') }}">All Underground Rappers</a>{% endblock %}
{% block content %}
<h1 style="font-size:clamp(34px,5.5vw,56px);margin-bottom:8px">{{ producer.name }}</h1>
<p class="meta" style="margin-bottom:30px">{{ producer.credits|length }}
  credit{{ '' if producer.credits|length == 1 else 's' }} in the catalog</p>

<ul class="prodlist">
  {% for c in producer.credits %}
  <li>
    {% if c.kind == 'track' %}
    <a class="row" href="{{ url_for('track', slug=c.artist_slug, project_slug=c.project_slug, track_slug=c.track_slug) }}">
      <span>{{ c.track_title }}</span>
      <span class="who">{{ c.artist_name }} · {{ c.project_title }}</span>
      <span class="kind">Track{% if c.year %} · {{ c.year }}{% endif %}</span>
    </a>
    {% else %}
    <a class="row" href="{{ url_for('single', slug=c.artist_slug, single_slug=c.single_slug) }}">
      <span>{{ c.single_title }}</span>
      <span class="who">{{ c.artist_name }}</span>
      <span class="kind">Single{% if c.year %} · {{ c.year }}{% endif %}</span>
    </a>
    {% endif %}
  </li>
  {% endfor %}
</ul>
{% endblock %}
"""

ABOUT = """
{% extends "layout.html" %}
{% block title %}About Underground Catalog{% endblock %}
{% block masthead %}<a class="backlink" href="{{ url_for('index') }}">All Underground Rappers</a>{% endblock %}
{% block content %}
<main class="info-page">
  <div class="warning-note rounded-2xl shadow-xl transition-all duration-300">
  <h1>About Underground Catalog</h1>

  <h2>What is Underground Catalog?</h2>
  <p>Underground Catalog is an archive for underground rap with all the tracks, projects, and everything being written and added to the Catalog by one single person.</p>

  <h2>What does Underground Catalog have?</h2>
  <p>Underground Rappers, a search bar for rappers, producers, and tracks. A button for light mode / dark mode. A dice button below the light mode / dark mode button that takes the user to a random track. A settings button with the available settings:</p>
  <p><strong>Default Sort by Date:</strong> the options for this setting is “Oldest First” and “Newest First” this just means when you click on an artist page should it show the songs and projects from newest release date or oldest release date, this is set it “Oldest First” by default.</p>
  <p><strong>Sidebar Visibility:</strong> This is checked by default, on the homepage, to the right of the artist list, there is a “Newest Underground Rap Releases” and a “Top 5 Producers”, if you uncheck the Sidebar Visibility setting then those will no longer show on the homepage.</p>
  <p><strong>Singles Only:</strong> This is off by default. When enabled, the catalog hides album/EP tracks and only shows singles (including tracks that are also released as singles), and the Random Song button only picks from singles.</p>
</main>
{% endblock %}
"""

CONTENT_WARNING = """
{% extends "layout.html" %}
{% block title %}Content Warning{% endblock %}
{% block masthead %}<a class="backlink" href="{{ url_for('index') }}">All Underground Rappers</a>{% endblock %}
{% block content %}
<main class="info-page">
  <div class="warning-note rounded-2xl shadow-xl transition-all duration-300">
    <h1>Content Warning</h1>
    <p>Underground Catalog is just a place to look up producers, tracks, and where to listen to underground rap tracks. All track and project titles are artistic expressions. This site does not host any mp3s or downloads for copyrighted music, only SoundCloud or YouTube embeds or other links like Spotify and YouTube Music to listen to the tracks.</p>
    <p>If you or someone you know is in distress or needs support, free and confidential help is available 24/7. Please connect with your local crisis lifeline or text HOME to 741741.</p>
  </div>
</main>
{% endblock %}
"""

NOT_FOUND = """
{% extends "layout.html" %}
{% block title %}Nothing here{% endblock %}
{% block content %}
<h1 style="font-size:48px;margin-bottom:14px">Nothing at this address</h1>
<p class="empty">That underground rapper, release or track isn't in the database.
<a href="{{ url_for('index') }}">Go back to the roster</a>.</p>
{% endblock %}
"""

app.jinja_loader = DictLoader({
    "layout.html": LAYOUT,
    "logos.html": LOGOS,
    "platforms.html": PLATFORM_ROW,
    "cover.html": COVER_BLOCK,
    "listen.html": LISTEN_BLOCK,
    "video.html": VIDEO_BLOCK,
    "credit-hover.html": CREDIT_HOVER,
    "index.html": INDEX,
    "artist.html": ARTIST,
    "project.html": PROJECT,
    "track.html": TRACK,
    "single.html": SINGLE,
    "collective.html": COLLECTIVE,
    "producer.html": PRODUCER,
    "about.html": ABOUT,
    "content-warning.html": CONTENT_WARNING,
    "404.html": NOT_FOUND,
})


if __name__ == "__main__":
    os.makedirs(IMAGES_DIR, exist_ok=True)
    app.run()