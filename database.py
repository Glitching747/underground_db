import re
from datetime import datetime


# ---------------------------------------------------------------- template
#
# Copy everything between the braces into ARTISTS below.
#
# {
#     "name": "",
#     "image": "",                      # file name inside images/
#     "aliases": [],                    # ["Other Name", "Old Tag"]
#     "dob": "",                        # "1996-03-04" or "March 4, 1996"
#     "dead": "yes",                     # "yes" to show the RIP notice on the artist page
#     "links": {
#         "spotify": "",
#         "youtube_music": "",
#         "soundcloud": "",
#     },
#     "projects": [
#         {
#             "title": "",
#             "kind": "Album",          # Album / EP / Mixtape
#             "year": "",
#             "cover": "",              # file name inside images/
#             "url": "",                # YouTube playlist, YouTube Music album, or
#                                        # SoundCloud set link — SoundCloud shows as a
#                                        # playable embed, anything else as a Play now link
#             "music_video": "",        # one or more YouTube links (or the full <iframe>
#                                        # embed code), separated by spaces if there's more
#                                        # than one — each shows as its own embedded video
#                                        # under the url block
#             "collab": "",             # another artist's name (or several, separated by
#                                        # commas) this whole project is a collab with — it
#                                        # shows up on their page too, sorted in with their
#                                        # own releases, linking back to this same page
#             "tracks": [
#                 "",
#             ],
#         },
#     ],
#     "singles": [
#         {
#             "title": "",
#             "year": "",
#             "cover": "",
#             "url": "",                # a SoundCloud link shows as a playable embed;
#                                        # anything else (YouTube Music, etc.) shows as
#                                        # a Play now link
#             "music_video": "",        # same as above — one or more YouTube links (or
#                                        # <iframe> embed codes) separated by spaces
#         },
#     ],
#     "collectives": [],                # ["Slime Krew"] — must match a name in COLLECTIVES below
# },


# ---------------------------------------------------------------- collectives
#
# A group, crew, or label roster. Members are just names — if a name matches
# an artist's name or alias (case-insensitive), it becomes a clickable link
# to that artist's page automatically. If it doesn't match anyone, it just
# shows as plain text, so you can list a member before you've built their page.
#
# {
#     "name": "",
#     "image": "",                      # file name inside images/
#     "current_members": [],            # ["OsamaSon", "wildkarduno"]
#     "former_members": [],
# },

COLLECTIVES = [
{
    "name": "Slime Krew",
    "image": "Slime Krew.jpg",
    "current_members": ["OsamaSon", "1oneam", "Okaymar", "wildkarduno", "Smokingskul", "ohsxnta", "elijxhwtf", "boolymon", "19thou", "tdf", "perc40"],
},
{
    "name": "iGore",
    "image": "iGore.jpg",
    "current_members": ["bleood", "zai", "yoi", "yrsci", "invel", "spellscasted", "dluxx", "conjuraxxion"],
    "former_members": ["yuke"],    
},
{
    "name": "odd squad",
    "image": "odd squad.jpg",
    "current_members": ["19thou", "1i1an1", "20MOP", "boolymon", "dbglokk", "dxrop", "Jugnino", "kashmustdie", "KRBY", "lilodmv", "Perubaby", "SkellyShiest", "tali", "twovrt", "tyr9ll", "uunitzz", "Wise", "yunin"],
},
{
    "name": "najma",
    "image": "najma-collective.jpg",
    "current_members": ["yuke", "jaydes", "kushbabykeys", "aeter", "zai", "suban", "Ja66", "ivvys", "october"],
    "former_members": ["kiltmymood", "tah"],
},
{
    "name": "TooManyStrikers",
    "image": "TooManyStrikers.jpg",
    "current_members": ["kuru", "Dragnutz", "SJR", "Jaeychino", "SlimeGetEm", "ST7 JodyBoof", "tovi", "killjae",],
},
{
    "name": "ØWAY",
    "image": "oway.jpg",
    "current_members": ["Tezzus", "diamond*", "10KDunkin", "billi0n", "Boofinese", "EA TJ", "Lil Righteous", "Lilkixkdor", "Percaso", "Pz'", "REEZY X", "ShawtyRokk", "Sk8star", "Southsidesilhouette", "XA (Xavier Anthony)", "Yung Fazo",]
},
]


# ---------------------------------------------------------------- the catalog

ARTISTS = [
 {
     "name": "OsamaSon",
     "image": "OsamaSon.gif",                      # file name inside images/
     "aliases": ["Lil O", "Damn 4K", "PradaUMari", "Flxr", "younotsupposedtobehere", "PFKSosa"],                    # ["Other Name", "Old Tag"]
     "dob": "May 20, 2003",                        # "1996-03-04" or "March 4, 1996"
     "collectives": ["Slime Krew"],
     "links": {
         "spotify": "https://open.spotify.com/artist/0uj6QiPsPfK8ywLC7uwBE1",
         "youtube_music": "https://music.youtube.com/channel/UCh_YNYvD3VX1wepTg1ydUaA",
         "soundcloud": "https://soundcloud.com/osamason",
     },
     "projects": [
         {
             "title": "Osama Season",
             "kind": "Album",          # Album / EP / Mixtape
             "year": "July 21, 2023",
             "cover": "Osama Season.png",             # file name inside images/
             "url": "https://music.youtube.com/playlist?list=OLAK5uy_n9N4c_soGxH8q_FMfMkPLvp3MuUbUPOc4",
             "music_video": "https://www.youtube.com/watch?v=8L13483CU9Y https://www.youtube.com/watch?v=Wdjlyg_9Rw8 https://www.youtube.com/watch?v=Ehipu4TYdnM https://www.youtube.com/watch?v=y5mBL8-fpaI",
             "tracks": [
                 "Leh Go (prod. ok)",
                 "Werkin (prod. Wise, lukeveretti)",
                 "Vlone (prod. perc40)",
                 "Summer Sixteen (prod. Thrty)",
                 "Anti (prod. Nine9, OsamaSon)",
                 "Lil O (prod. legion, bart how)",
                 "X & Sex (prod. Rok, legion, JCOnTheTrack)",
                 "Kutta (prod. Thrty)",
                 "Lambtruck (prod. ok)",
                 "Dont Let Looks Fool (prod. Rok, Roxie)",
                 "Pipeup (prod. boolymon, Marrgielaa)",
                 "Troops (prod. ok)"
             ],
         },
         {
             "title": "Flex Musix",
             "kind": "Mixtape",          # Album / EP / Mixtape
             "year": "December 8, 2023",
             "cover": "OsamaSon - Flex Musix.png",              # file name inside images/
             "url": "https://music.youtube.com/playlist?list=OLAK5uy_mEjZsgkDLuUyi7oE1iwDkGU7-tHc5CYZY",
             "music_video": "https://www.youtube.com/watch?v=EYTYG-u9seY https://www.youtube.com/watch?v=2Cp27sg-3Ss",
             "tracks": [
                 "Blonde (prod. ok, Otwreg)",
                 "Baghdad (prod. ok, Rok)",
                 "All Star (prod. legion, skai)",
                 "For Da Flex (prod. gyro)",
                 "Worst Part (prod. perc40)",
                 "Trenches (prod. legion)",
                 "Nothing (prod. skai)",
                 "3x (prod. Rok, Warren Hunter)",
                 "Boss Up (prod. Rok, OsamaSon)",
                 "Kills (prod. Rok, legion, skai, gyro)",
                 "Kome Thru (prod. Rok, legion)",
                 "Me When (prod. legion, skai)",
                 "Uno (prod. legion)",
                 "St8 Flexin (prod. Rok)",
                 "Congrats (prod. ok)",
                 "Pop (prod. ok)",
                 "Talking 2 A Ghost (prod. thr6x, saintracks, lymarmax)"
             ],
         },
         {
             "title": "Flex Musix (FLXTRA)",
             "kind": "Deluxe",          # Album / EP / Mixtape
             "year": "February 16, 2024",
             "cover": "OsamaSon - Flex Musix (FLXTRA).png",              # file name inside images/
             "url": "https://music.youtube.com/playlist?list=OLAK5uy_mixm5vBbF7aqYam7Roc4IEqmvkFBX0zsU",
             "music_video": "https://www.youtube.com/watch?v=pEWB_PqmNpE https://www.youtube.com/watch?v=aE-9hFktH40",
             "tracks": [
                 "Cartel (prod. gyro)",
                 "Rehhab (prod. gyro, skai, Warren Hunter)",
                 "Need It (prod. boolymon, Thrty)",
                 "Alot (prod. Warren Hunter)",
                 "Flxr (prod. Rok, skai, Warren Hunter, RUNAWAY)",
                 "Freestyle (prod. gyro)",
                 "Blonde (prod. ok, Otwreg)",
                 "Baghdad (prod. ok, Rok)",
                 "All Star (prod. legion, skai)",
                 "For Da Flex (prod. gyro)",
                 "Worst Part (prod. perc40)",
                 "Trenches (prod. legion)",
                 "Nothing (prod. skai)",
                 "3x (prod. Rok, Warren Hunter)",
                 "Boss Up (prod. Rok, OsamaSon)",
                 "Kills (prod. Rok, legion, skai, gyro)",
                 "Kome Thru (prod. Rok, legion)",
                 "Me When (prod. legion, skai)",
                 "Uno (prod. legion)",
                 "St8 Flexin (prod. Rok)",
                 "Congrats (prod. ok)",
                 "Pop (prod. ok)",
                 "Talking 2 A Ghost (prod. thr6x, saintracks, lymarmax)"
             ],
         },
         {
             "title": "3vil Reflection",
             "kind": "Collab Mixtape (OsamaSon & Glokk40Spaz)",          # Album / EP / Mixtape
             "year": "May 11, 2024",
             "cover": "OsamaSon - 3vil Reflection.jpg",              # file name inside images/
             "url": "https://music.youtube.com/playlist?list=OLAK5uy_ki1iZ-YlCd8vwvgjiZHTaXgMkAJTpnOpI",
             "tracks": [
                       "2X (prod. Chris Clay)",
	                   "Movie (prod. Al Chapo, legion)",
	                   "Blame Dem Drugz (prod. Ryobabylove, K4nji, 1jae)",
                       "Bankroll (prod. Al Chapo)",
                       "No Rules (prod. Ryobabylove, Tritri)",
	                   "ADHD (prod. Chris Clay)",
	                   "Jungle (prod. Rok)",
                       "Wicked (prod. Kat Lightning)",
                       "Vixen (prod. Rok)"
             ],
         },
         {
             "title": "Leaks Tape (Vol. 1)",
             "kind": "Album",          # Album / EP / Mixtape
             "year": "December 13, 2024",
             "cover": "OsamaSon - Leaks Tape Vol 1.png",              # file name inside images/
             "url": "https://music.youtube.com/playlist?list=PLbme6n8cqKiqLy9s6bjtn10uaPOQX-Uoz",
             "tracks": [
                       "My bad (prod. gyro, skai, Warren Hunter)",
	                   "100 blues (prod. Rok, gyro, skai, Warren Hunter)",
	                   "All day (prod. Devstacks)",
                       "Licks (prod. cargo, RUNAWAY)",
                       "Hitech Demon (prod. azure)",
	                   "Wanna go to war (prod. perc40)",
	                   "Hope (prod. gyro)",
                       "Fine Wit It (prod. gyro)",
                       "Feels (prod. legion, skai)",
                       "street cred xxx (prod. skai)",
             ],
         },
         {
             "title": "Leaks Tape (Vol. 2)",
             "kind": "Album",          # Album / EP / Mixtape
             "year": "December 20, 2024",
             "cover": "OsamaSon - Leaks Tape Vol 2.png",              # file name inside images/
             "url": "https://music.youtube.com/playlist?list=PLbme6n8cqKirfCb-UBtGtVrpC3lQGyMqA",
             "tracks": [
                       "do sum 4 urself (prod. legion, skai)",
	                   "or what (prod. legion, skai)",
	                   "5.6 (prod. gyro)",
                       "kkutup (prod. gyro)",
                       "Pain is beautiful (prod. Rok, bart how)",
	                   "Roster (prod. legion)",
	                   "Flex rule da world (prod. gyro)",
                       "1300 (prod. skai, Warren Hunter)",
                       "Patna (prod. skai)",
                       "Catch me if u can (prod. gyro)",
             ],
         },

         {
             "title": "Jump Out",
             "kind": "Mixtape",          # Album / EP / Mixtape
             "year": "January 24, 2025",
             "cover": "OsamaSon - Jump Out.jpg",              # file name inside images/
             "url": "https://music.youtube.com/playlist?list=OLAK5uy_mQsIcxGeXx5PM1mwcPJRUxI0tyvXJt3oA",
             "music_video": "https://www.youtube.com/watch?v=K5R59EIEXLA",
             "tracks": [
                       "Southside (prod. ok)",
	                   "Fool (prod. ok)",
	                   "GTFO The Room (prod. ok)",
                       "Made Sum Plans (prod. ok)",
                       "Break Da News (prod. ok)",
	                   "Room 156 (prod. ok)",
	                   "Jumpout (prod. gyro, OsamaSon)",
                       "Going Dumbo (prod. legion, Warren Hunter)",
                       "She Need A Ride (prod. ok)",
                       "New Tune (prod. skai)",
                       "I Got The Fye (prod. ok)",
                       "Insta (prod. ok)",
                       "Frontin (prod. ok)",
                       "Mufasa (prod. ok)",
                       "Ref (prod. Jay Trench)",
                       "The Whole World Is Free (prod. ok, OsamaSon)",
                       "Round Of Applause (prod. ok)",
             ],
         },
         {
             "title": "grails",
             "kind": "Single",          # Album / EP / Mixtape
             "year": "May 21, 2025",
             "cover": "OsamaSon - grails.jpg",              # file name inside images/
             "url": "https://music.youtube.com/playlist?list=OLAK5uy_mJOTt0AN8wtgZZcnVfe6tH8Q2kBbslntM",
             "tracks": [
                       "Lil O The Impaler (prod. gyro)",
	                   "Slime U Out (prod. Rok, gyro)",
	                   "Horses (prod. Marrgielaa, OsamaSon)",
             ],
         },
         {
             "title": "psykotic",
             "kind": "Mixtape",          # Album / EP / Mixtape
             "year": "October 10, 2025",
             "cover": "OsamaSon - psykotic.jpg",              # file name inside images/
             "url": "https://music.youtube.com/playlist?list=OLAK5uy_md-hljAHitLyFHz_f5ylrGoFeAhYdok6A",
             "music_video": "https://www.youtube.com/watch?v=JWHDhiwJNOs https://www.youtube.com/watch?v=2krpk-j_Kx4",
             "tracks": [
                       "Habits (prod. Warren Hunter)",
	                   "Worldwide (prod. gyro)",
	                   "Addicted (prod. gyro, OsamaSon)",
                       "Get Away (prod. Warren Hunter, Roxie)",
                       "Maag Dump (prod. Warren Hunter)",
	                   "T193 (prod. Warren Hunter)",
	                   "FMJ (feat. Che) (prod. Warren Hunter)",
                       "Inferno (prod. Rok, OsamaSon)",
                       "She woke Up (prod. ok)",
                       "Function (prod. legion)",
                       "In It (prod. Rok, warren Hunter)",
                       "yea i kno (prod. Rok, gyro)",
                       "Whats Happening (prod. gyro)",
                       "Its A Party (prod. rok, legion, skai, Warren Hunter)", 
                       "Gintama (prod. gyro, OsamaSon)",
                       "Guap Man (prod. ok)",
                       "Victory Lap (prod. Rok, OsamaSon)",
             ],
         },
         {
             "title": "still slime",
             "kind": "Collab Album (OsamaSon & boolymon)",          # Album / EP / Mixtape
             "year": "March 12, 2024",
             "cover": "OsamaSon - still slime.jpg",              # file name inside images/
	         "url": "https://archive.org/details/still-slime",
             "collab": "boolymon",
             "tracks": [
                       "yslime (prod. boolymon, Marrgielaa)",
	                   "killstreak (prod. boolymon, Thrty)",
	                   "thorns (prod. boolymon, Thrty)",
                       "way 2 easy (prod. twovrt, boolymon, Thrty)",
                       "catch me outside (prod. boolymon, Marrgielaa)",
	                   "rooftop (prod. boolymon, Marrgielaa)",
	                   "fto (prod. boolymon)",
                       "nun from me (prod. boolymon)",
                       "spin @ noon (prod. boolymon, Marrgielaa, Painting Demons)",
                       "red moon (prod. boolymon, Marrgielaa)",
                       "no smoke (prod. boolymon, Marrgielaa, OsamaSon)",
                       "still inna trap (feat. Hunnitmill) (prod. boolymon, Thrty)",
                       "cross dat street (prod. boolymon)",
                       "trees (prod. boolymon, Marrgielaa, OsamaSon)",
                       "creek (prod. boolymon, Marrgielaa, OsamaSon)",
             ],
         },
         
     ],
     "singles": [
         {
             "title": "High as shit (prod. Babyben)",
             "year": "January 14, 2022",
             "cover": "OsamaSon - High as shit.jpg",
             "url": "https://soundcloud.com/tatzuu/osamason-high-as-shit",
             "music_video": "https://www.youtube.com/watch?v=DxdvEldKsqs",},
     {
             "title": "MeVsWorld (prod. OsamaSon)",
             "year": "April 3, 2022",
             "cover": "OsamaSon - MeVsWorld.jpg",
             "url": "https://soundcloud.com/osamason-archive/mevsworld",
         },
         {
             "title": "girl of my dreams (prod. OsamaSon)",
             "year": "April 25, 2022",
             "cover": "OsamaSon - girl of my dreams.png",
             "url": "https://soundcloud.com/osamason/girl-of-my-dreams-prod-osama",},
     {
             "title": "gotohell (prod. OsamaSon, XanGang)",
             "year": "May 9, 2022",
             "cover": "OsamaSon - gotohell.jpg",
             "url": "https://soundcloud.com/osamason/slime-prod-osamason-xangang",
             "music_video": "https://www.youtube.com/watch?v=5DCeJ8LJR4c",
         },
         {
             "title": "catch em (prod. perc40)",
             "year": "September 17, 2022",
             "cover": "OsamaSon - catch em.jpg",
             "url": "https://soundcloud.com/osamason/catch-em-perc40-1",},
     {
             "title": "DEFEAT (prod. Jahsters)",
             "year": "July 7, 2022",
             "cover": "OsamaSon - DEFEAT.jpg",
             "url": "https://soundcloud.com/osamason/defeat-p-jahsters-1",
         },
         {
             "title": "tony (prod. Jahsters, 19thou)",
             "year": "October 9, 2022",
             "cover": "OsamaSon - tony.jpg",
             "url": "https://soundcloud.com/osamason/tony-jah-19thou",},
     {
             "title": "on me (prod. lilodmv)",
             "year": "October 31, 2022",
             "cover": "OsamaSon - on me.jpg",
             "url": "https://soundcloud.com/osamason/on-me-lilo",
         },
         {
             "title": "rehab (prod. perc40)",
             "year": "August 15, 2022",
             "cover": "OsamaSon - rehab.jpg",
             "url": "https://soundcloud.com/osamason/rehab-perc40-1",},
     {
             "title": "jugg in my sleep (prod. perc40)",
             "year": "July 7, 2022",
             "cover": "OsamaSon - jugg in my sleep.jpg",
             "url": "https://soundcloud.com/osamason/jugg-in-my-sleep-prodperc40",
         },
         {
             "title": "frontrow (prod. SouljaSpirits, Gxmini)",
             "year": "November 22, 2022",
             "cover": "OsamaSon - frontrow.jpg",
             "url": "https://soundcloud.com/osamason/frontrow-prod-souljaspirits-gxmini",
         },
         {
             "title": "in dat cut (prod. boolymon)",
             "year": "December 4, 2022",
             "cover": "OsamaSon - in dat cut.jpg",
             "url": "https://soundcloud.com/osamason/in-dat-cut-boolymon",
         },
         {
             "title": "garfield (prod. boolymon, Marrgielaa)",
             "year": "December 16, 2022",
             "cover": "OsamaSon - garfield.jpg",
             "url": "https://soundcloud.com/osamason/garfield-boolymon-marrgielaa",
         },
         {
             "title": "back from dead (prod. boolymon, twovrt, Thrty)",
             "year": "February 11, 2023",
             "cover": "OsamaSon - back from dead.jpg",
             "url": "https://soundcloud.com/osamason/back-from-dead-boolymon-twovrt-thrty-dj-phat-exclusive",
             "music_video": "https://www.youtube.com/watch?v=2ZX5kEe6b5k",
         },
         {
             "title": "draco (feat. ohsxnta) (prod. boolymon, Thrty)",
             "year": "March 7, 2023",
             "cover": "OsamaSon - draco.jpg",
             "url": "https://soundcloud.com/osamason/draco-ft-ohsxnta-prod-boolymon",
         },
          {
             "title": "slime krew (feat. wildkarduno, Smokingskul) (prod. perc40)",
             "year": "March 31, 2023",
             "cover": "OsamaSon - slime krew.jpg",
             "url": "https://soundcloud.com/osamason/slime-krew-ft-wildkaruno",
         },
         {
             "title": "cts-v (prod. Thrty)",
             "year": "April 7, 2023",
             "cover": "OsamaSon - cts-v.jpg",
             "url": "https://soundcloud.com/osamason/cts-v-prod-thrty",
             "music_video": "https://www.youtube.com/watch?v=09l4W21ExiE",
         },
         {
             "title": "Troops (prod. ok)",
             "year": "June 2, 2023",
             "cover": "OsamaSon - Troops.jpg",
             "url": "https://soundcloud.com/osamason/troops-prod-ok",
         },
         {
             "title": "Trenches (prod. legion)",
             "year": "September 8, 2023",
             "cover": "OsamaSon - Trenches.jpg",
             "url": "https://soundcloud.com/osamason/trenches",
             "music_video": "https://www.youtube.com/watch?v=lTQ8k9uysXo",
         },
         {
             "title": "withdrawals (feat. Nettspend) (prod. ok)",
             "year": "June 26, 2024",
             "cover": "OsamaSon - withdrawals.jpg",
             "url": "https://soundcloud.com/osamason/withdrawals-feat-nettspend",
             "music_video": "https://www.youtube.com/watch?v=UQ13LFqaTF8",
         },
         {
             "title": "popstar (prod. gyro)",
             "year": "July 13, 2024",
             "cover": "OsamaSon - popstar.jpg",
             "url": "https://soundcloud.com/osamason/popstar",
             "music_video": "https://www.youtube.com/watch?v=T042NW22osI",
         },
         {
             "title": "ik what you did last summer (prod. ok)",
             "year": "October 2, 2024",
             "cover": "OsamaSon - ik what you did last summer.jpg",
             "url": "https://soundcloud.com/osamason/ik-what-you-did-last-summer",
             "music_video": "https://www.youtube.com/watch?v=4DIQDnu3mr4",
         },
         {
             "title": "just score it (prod. gyro, OsamaSon)",
             "year": "May 1, 2024",
             "cover": "OsamaSon - just score it.jpg",
             "url": "https://soundcloud.com/osamason/just-score-it-prod-gyro-lil-o",
         },
         {
             "title": "The Whole World Is Free (prod. ok, OsamaSon)",
             "year": "November 12, 2024",
             "cover": "OsamaSon - The Whole World Is Free.jpg",
             "url": "https://soundcloud.com/osamason/the-whole-world-is-free",
             "music_video": "https://www.youtube.com/watch?v=Fy7WIdkxwDw",
         },
         {
             "title": "DEMON HOME (prod. Rok, legion, skai)",
             "year": "June 20, 2025",
             "cover": "OsamaSon - DEMON HOME.jpg",
             "url": "https://soundcloud.com/osamason/demon-home",
             "music_video": "https://www.youtube.com/watch?v=cVhPVPRhk2s",
         },
         {
             "title": "off that! (prod. 1st Class, trisstt, dayever)",
             "year": "May 20, 2026",
             "cover": "OsamaSon - off that!.jpg",
             "url": "https://soundcloud.com/osamason/off-that",
             "music_video": "https://www.youtube.com/watch?v=8Zuh44rji24",
         },
        
     ],
    },
 {
     "name": "Che",
     "image": "Che.gif",                      # file name inside images/
     "aliases": ["sipmansion", "bhe", "praiseche", "punkgroupies", "ripmansion", "Murkio!", "fukitche", "cheRomani+", "xenchey", "yafioso", "BASS GOD", "BASS KILLER"],                    # ["Other Name", "Old Tag"]
     "dob": "August 29, 2006",                        # "1996-03-04" or "March 4, 1996"
     "links": {
         "spotify": "https://open.spotify.com/artist/5A7T1LAGJg5NXySBoIKUmF",
         "youtube_music": "https://music.youtube.com/@che1101",
         "soundcloud": "https://soundcloud.com/che",
     },
     "projects": [
         {
             "title": "3",
             "kind": "EP",          # Album / EP / Mixtape
             "year": "May 1, 2022",
             "cover": "Che - 3.jpg",              # file name inside images/
             "url": "https://music.youtube.com/playlist?list=OLAK5uy_mT9rmGdtaUl6uVcabwCXqYEd1Szm70hA8",
             "tracks": [
                 "city (prod. Jdolla)",
	             "hugo (prod. Venexxi, Jdolla)",
	             "007 (feat. Specxfic) (prod. georgi)",
                 "nine (prod. OneVictim)",
             ],
         },     
         {
             "title": "closed captions",
             "kind": "Album",          # Album / EP / Mixtape
             "year": "July 21, 2023",
             "cover": "Che - closed captions.png",              # file name inside images/
             "url": "https://music.youtube.com/playlist?list=OLAK5uy_nBZ2z8XA8xkOHp_3Pt4uFNPM3EGRQMhbY",
             "tracks": [
                 "bluberry bakwood (prod. CXO, Swishrr)",
                 "sativa (prod. CXO)",
                 "fangs (prod. CXO)",
                 "????? (prod. CXO, Swishrr)",
                 "sol (prod. CXO, Swishrr)",
                 "canary (prod. CXO, ZaySkillz)",
                 "blac chyna (Prod. CXO, Swishrr)",
                 "sos (prod. CXO)",
                 "draco draco (prod. CXO)",
                 "frank ocean (Prod. SouljaSpirits)",
                 "flat (prod. CXO)",
             ],
         },
         {
             "title": "Before Crueger",
             "kind": "Single",          # Album / EP / Mixtape
             "year": "October 11, 2023",
             "cover": "Che - Before Crueger.jpg",              # file name inside images/
             "url": "https://music.youtube.com/playlist?list=OLAK5uy_lxO7PY_qicpQg4daxS5DDFFmUzopHGgMc",
             "tracks": [
                       "Japan (prod. CXO)",
	                   "Tony Tony (prod. CXO)",
             ],
         },
         {
             "title": "Crueger",
             "kind": "Mixtape",          # Album / EP / Mixtape
             "year": "October 31, 2023",
             "cover": "Che - Crueger.jpg",              # file name inside images/
             "url": "https://music.youtube.com/playlist?list=OLAK5uy_mhE21Nz0HzX2HiJWCZkNjQqFyecn3-Lug",
             "tracks": [
                       "Ok Den (prod. Che, CXO)",
	                   "Sayso (prod. Che, CXO)",
	                   "Busan (prod. Che, CXO)",
                       "Batman (prod. CXO, Che)",
                       "Gah Damn (prod. Che, CXO)",
	                   "Right Now (prod. Che)",
	                   "That's My Type (prod. Che)",
                       "Badu (prod. CXO, Che)",
                       "Call Me (prod. CXO)",
             ],
         },
         {
             "title": "Sayso Says",
             "kind": "Album",          # Album / EP / Mixtape
             "year": "August 30, 2024",
             "cover": "Che - Sayso Says.jpg",              # file name inside images/
             "url": "https://music.youtube.com/playlist?list=OLAK5uy_nlS-XF-FMuYrIHKePkpNw-wcotQpnIiHI",
             "tracks": [
                       "I Rot, I Rot (prod. Che, CXO, runnaberto)",
	                   "SASKA YOU MADE IT (feat. Saska) (prod. Che, Saska)",
	                   "Pretend We're Sleeping (prod. Che)",
                       "GET NAKED (prod. Che)",
                       "ENJOY YOUR LIFE (prod. Ginseng, MISOGI, Jay Trench)",
	                   "Been There, Done That (prod. Che, CXO)",
	                   "Hex On My Chest, It's Going Down (prod. Che, Dreamz, runnaberto)",
                       "Pissy Coffee (prod. Che, Dreamz, runnaberto)",
                       "Interlude (prod. CXO)",
                       "It's My Party and I'll Die If I Want To (prod. Che, J0se)",
                       "DON'T TELL NO1 (prod. skai)",
                       "NUNCA HACER COCAINA (prod. CXO)",
                       "School Girl Sashimi (prod. Che, J0se)",
                       "YDFWMNM? (prod. Che)",
                       "Children Shouldn't Play With Dead Things (prod. Che)",
                       "CUT OFF YOUR HANDS (prod. Warren Hunter)",
                       "My Favorite Color is Red (prod. Che, CXO)",
             ],
         },
         {
             "title": "REST IN BASS",
             "kind": "Album",          # Album / EP / Mixtape
             "year": "July 18, 2025",
             "cover": "Che - REST IN BASS.jpg",              # file name inside images/
             "url": "https://music.youtube.com/playlist?list=OLAK5uy_nJmf3W-_IBLN0-Md7_isux8NaJel0cngc",
             "tracks": [
                       "SLAM PUNK (prod. Rok)",
	                   "ROLLING STONE (prod. azure)",
	                   "ON FLEEK (prod. CXO)",
                       "LIP FILLER (prod. Rok)",
                       "HOOD FAMOUS (prod. Rok)",
	                   "BOSSUPPPP (prod. azure, Rok, gyro)",
	                   "MARCELINE (prod. Rok)",
                       "DIE YOUNG (prod. gyro)",
                       "HELLRAISER (feat. OsamaSon) (prod. CXO)",
                       "DIOR LEOPARD (prod. azure)",
                       "MANNEQUIN (prod. Che, xaviersobased)",
                       "BLACK SWAN (prod. skai, legion, CXO)",
                       "MDMA (prod. Warren Hunter)",
                       "NEVER TOO YOUNG TO DIE (feat. Chuckyy) (prod. Lucid, repglick)",
                       "EARDRUMMER (prod. Ginseng, legion, love&peace)",
                       "DOE DEER (prod. Rok, CXO)",
                       "STAGEDIVIN (prod. azure)",
                       "BA$$ (prod. CXO)",
             ],
         },
         {
             "title": "REST IN BASS: ENCORE",
             "kind": "Deluxe",          # Album / EP / Mixtape
             "year": "December 25, 2025",
             "cover": "Che - REST IN BASS ENCORE.png",              # file name inside images/
             "url": "https://music.youtube.com/playlist?list=OLAK5uy_kKPEbWs0fdDxxei2O1EppEVlHs6uulQqo",
             "tracks": [
                       "KING OF ROCK (prod. CXO)",
                       "MAKE OUT WITH MY CHOPPA (prod. Che)",
                       "HOLY MOLY (prod. Rok, legion, gyro)",
                       "DIE HARD (prod. legion)",
                       "CUTTHROAT (prod. gyro)",
                       "MONSTER (prod. Che)",
                       "DIRTY SPRITE (prod. Che, CXO)",
                       "SERVE DA BA$$ (prod. Rok, gyro)",
                       "RIRI (prod. gyro)",
                       "WHIPPIN (feat. OsamaSon) (prod. gyro)",
                       "WHATS LOVE (prod. azure)",
                       "FREAK NEEK (prod. azure)",
                       "UAV (prod. CXO, Warren Hunter)",
                       "IM SORRY (prod. Rok, gyro)",                    
                       "SLAM PUNK (prod. Rok)",
	                   "ROLLING STONE (prod. azure)",
	                   "ON FLEEK (prod. CXO)",
                       "LIP FILLER (prod. Rok)",
                       "HOOD FAMOUS (prod. Rok)",
	                   "BOSSUPPPP (prod. azure, Rok, gyro)",
	                   "MARCELINE (prod. Rok)",
                       "DIE YOUNG (prod. gyro)",
                       "HELLRAISER (feat. OsamaSon) (prod. CXO)",
                       "DIOR LEOPARD (prod. azure)",
                       "MANNEQUIN (prod. Che, xaviersobased)",
                       "BLACK SWAN (prod. skai, legion, CXO)",
                       "MDMA (prod. Warren Hunter)",
                       "NEVER TOO YOUNG TO DIE (feat. Chuckyy) (prod. Lucid, repglick)",
                       "EARDRUMMER (prod. Ginseng, legion, love&peace)",
                       "DOE DEER (prod. Rok, CXO)",
                       "STAGEDIVIN (prod. azure)",
                       "BA$$ (prod. CXO)",
             ],
         },
         {
             "title": "Fully Loaded",
             "kind": "EP",          # Album / EP / Mixtape
             "year": "March 27, 2026",
             "cover": "Che - Fully Loaded.png",              # file name inside images/
             "url": "https://music.youtube.com/playlist?list=OLAK5uy_mEst3rO-Ov84DYg6FPBK92edG8N1KZ97o",
             "tracks": [
                       "Million Dollar Mansion (prod. Che)",
	                   "Promoting Violence (prod. Rok)",
	                   "White Folk (prod. Che)",
                       "Tattoos (prod. Che, Rok)",
                       "Kittens (prod. Rok)",
             ],
         },
         {
             "title": "Para'dies",
             "kind": "EP",          # Album / EP / Mixtape
             "year": "April 24, 2026",
             "cover": "Che - Para'dies.png",              # file name inside images/
             "url": "https://music.youtube.com/playlist?list=OLAK5uy_ksNKK87G-7wAYz88jcRlZHolJE19Z7Ff0",
             "tracks": [
                       "Tell U Sum (prod. CXO)",
	                   "Nosferatu (prod. Rok)",
             ],
         },
         {
             "title": "Empty Clip",
             "kind": "EP",          # Album / EP / Mixtape
             "year": "June 19, 2026",
             "cover": "Che - Empty Clip.png",              # file name inside images/
             "url": "https://music.youtube.com/playlist?list=OLAK5uy_n60mA550OcerBfcmpGGeLT3B8aDqlzeBg",
             "tracks": [
                       "Like Lil Mexico (prod. Che)",
	                   "2sday (prod. CXO)",
	                   "Dmx (prod. Che)",
                       "Og Ginobili (prod. Rok)",
                       "Los Santos (prod. CXO)",
             ],
         },
         
     ],
     "singles": [
         {
             "title": "kind (prod. sxprano)",
             "year": "September 17, 2021",
             "cover": "Che - kind.jpg",
             "url": "https://soundcloud.com/blimpwarrior567/che-kind",},
     {
             "title": "#RESIDE (prod. Airbourn Beats)",
             "year": "October 15, 2021",
             "cover": "Che - #RESIDE.png",
             "url": "https://soundcloud.com/che/resideprod-airbournebeats",
         },
     {
             "title": "#hundred (prod. Nick Mira, Infaced, rnzy)",
             "year": "November 15, 2021",
             "cover": "Che - #hundred.png",
             "url": "https://soundcloud.com/killhelis/che-hundred-without",
         },
         {
             "title": "agenda (prod. Che, bryalle)",
             "year": "December 10, 2021",
             "cover": "Che - agenda.jpg",
             "url": "https://soundcloud.com/che/agenda-bryalle",},
     {
             "title": "The Final Agenda (prod. bryalle)",
             "year": "January 15, 2022",
             "cover": "Che - The Final Agenda.jpg",
             "url": "https://soundcloud.com/blimpwarrior567/che-the-final-agenda-bryalle",
         },
         {
             "title": "euphoria (feat. Specxfic) (prod. kimj, SEBii)",
             "year": "February 18, 2022",
             "cover": "Che - euphoria.jpg",
             "url": "https://soundcloud.com/tony-storyteller/cheromani-euphoria-ft-specxfic",
         },
         {
             "title": "wtf (prod. OneVictim)",
             "year": "June 17, 2022",
             "cover": "Che - wtf.png",
             "url": "https://soundcloud.com/che/wtf-p-victim",
             "music_video": "https://www.youtube.com/watch?v=EY410mfu3bY",
         },
         {
             "title": "feel (feat. jssr) (prod. FwThis1Will)",
             "year": "July 16, 2022",
             "cover": "Che - feel.jpg",
             "url": "https://soundcloud.com/sussy-bak/che-feel-feat-jssr",
             "music_video": "https://www.youtube.com/watch?v=AzScAoEojo8",
         },
         {
             "title": "intro (prod. Ccured, malikai)",
             "year": "August 29, 2022",
             "cover": "Che - intro.jpg",
             "url": "https://soundcloud.com/che/ccintro",
         },
         {
             "title": "broke (feat. Glo, jssr) (prod. perc40)",
             "year": "August 12, 2022",
             "cover": "Che - broke.jpg",
             "url": "https://soundcloud.com/glofromda4/broke-ft-jssr-che-perc40",
         },
         {
             "title": "Bae (prod. CXO)",
             "year": "February 14, 2024",
             "cover": "Che - Bae.jpg",
             "url": "https://soundcloud.com/che/bae",
             "music_video": "https://www.youtube.com/watch?v=OZ9b_psvEC8",
         },
         {
             "title": "Miley Cyrus (prod. prettifun)",
             "year": "March 27, 2024",
             "cover": "Che - Miley Cyrus.jpg",
             "url": "https://soundcloud.com/che/miley-cyrus-1",
             "music_video": "https://www.youtube.com/watch?v=yHLxZKLSkvo",
         },
         {
             "title": "Pizza Time (prod. prettifun)",
             "year": "May 29, 2024",
             "cover": "Che - Pizza Time.jpg",
             "url": "https://soundcloud.com/che/pizza-time-1",
             "music_video": "https://www.youtube.com/watch?v=Ew5-ygNHV2g",
         },
         {
             "title": "Pose For The Pic (prod. legion)",
             "year": "January 15, 2025",
             "cover": "Che - Pose For The Pic.jpg",
             "url": "https://soundcloud.com/che/pose-for-the-pic",
             "music_video": "https://www.youtube.com/watch?v=uNIxPwN12m8",
         },
         {
             "title": "Love (MKB) (prod. CXO)",
             "year": "March 16, 2025",
             "cover": "Che - Love (MKB).jpg",
             "url": "https://soundcloud.com/che/love-mkb",
             "music_video": "https://www.youtube.com/watch?v=SlCI0e4b1jc",
         },
         {
             "title": "Green Day (prod. CXO)",
             "year": "May 16, 2025",
             "cover": "Che - Green Day.jpg",
             "url": "https://soundcloud.com/che/af703a0f-0408-4c1a-b298-93de10826b23",
         },
         {
             "title": "KickAss (Pull Up Pls) (feat. Nettspend) (prod. Che)",
             "year": "September 4, 2026",
             "cover": "Che - KickAss (Pull Up Pls).jpg",
             "url": "https://soundcloud.com/aprilzcrucifix/kickass-pull-up-pls",
         },
         
     ],
    },    
 {
     "name": "Nettspend",
     "image": "Nettspend-flexing.gif",                      # file name inside images/
     "aliases": ["Nett", "6unner", "6unnex"],                    # ["Other Name", "Old Tag"]
     "dob": "March 18, 2007",                        # "1996-03-04" or "March 4, 1996"
     "links": {
         "spotify": "https://open.spotify.com/artist/2jl4qd6UbzeCmImT4nWbtA",
         "youtube_music": "https://music.youtube.com/@nettspend",
         "soundcloud": "https://soundcloud.com/nettspend",
     },
     "projects": [
         {
             "title": "BAD ASS F*CKING KID",
             "kind": "Album",          # Album / EP / Mixtape
             "year": "December 6, 2024",
             "cover": "Nettspend - BAD ASS FCKING KID.png",              # file name inside images/
             "url": "https://music.youtube.com/playlist?list=OLAK5uy_kEnp6JfMThBFTnI3g0nzyme6MxNOzlhQs",
             "tracks": [
                 "Growing Up (prod. Rok, Carter Bryson, 3rdup, Nick Souza)",
                 "Leader (prod. ok, Kenny Beats)",
                 "Project Pat (prod. ok)",
                 "Tommy (prod. Rok, Warren Hunter)",
                 "Tyla (prod. ok)",
                 "A$AP (prod. ok)",
                 "F*CK CANCER (prod. reklus1ve)",
                 "Skipping Class (prod. ok)",
                 "Beach leak (prod. evilgiane, Bhristo, Bobby Raps)",
                 "Shut Up (prod. ok)",
                 "Birdbox (prod. ok)",
                 "Drop The Blunt (prod. reklus1ve)",
                 "Perc Soda (prod. ok)",
                 "LAUGHIN (prod. ok)",
                 "Say Please (prod. methboiswag)"
             ],
         },
         {
             "title": "gone too soon",
             "kind": "EP",          # Album / EP / Mixtape
             "year": "August 22, 2025",
             "cover": "Nettspend - gone too soon.png",              # file name inside images/
             "url": "https://music.youtube.com/playlist?list=OLAK5uy_lHiXNlPGFE9jbLJqJXR92WMwZLsqETJF4",
             "tracks": [
                       "stressed (prod. RIOTUSA, GOLDIN)",
	                   "her friends (prod. ss3bby)",
             ],
         },         
         {
             "title": "early life crisis",
             "kind": "Album",          # Album / EP / Mixtape
             "year": "March 6, 2026",
             "cover": "Nettspend - early life crisis.png",              # file name inside images/
             "url": "https://music.youtube.com/playlist?list=OLAK5uy_natFiqgyrgw7AtoSNZp71vrDDOGWFT8n8",
             "tracks": [
                 "you ready? (prod. CXO)",
	             "ce (prod. legion)",
	             "pain talk (feat. OsamaSon) (prod. Rok, gyro, skai, Warren Hunter)",
                 "crack (prod. Rok)",
                 "still standing (prod. Rok)",
	             "who tf is u (prod. CXO)",
	             "trap house 2016 (prod. skai)",
                 "masked up (feat. YoungBoy Never Broke Again) (prod. CXO)",
                 "stab (prod. legion)",
                 "halftime (prod. CXO)",
                 "meet me in richmond (prod. CXO)",
                 "no sleep (prod. cranes)",
                 "<3 me (prod. ok, Otwreg)",
                 "paris hilton (prod. Rok, gyro, CXO)",
                 "sick (prod. CXO)",
                 "cross em out (prod. azure)",
                 "shades on (prod. CXO)",
                 "plan b (prod. gyro)",
                 "make it bleed (prod. ss3bby)",
                 "hey, hello (prod. Rok)",
                 "lil bieber (prod. cranes)",                
             ],
         },
         {
             "title": "HIM",
             "kind": "Compilation Album",          # Album / EP / Mixtape
             "year": "April 30, 2026",
             "cover": "Nettspend - HIM.jpg",              # file name inside images/
             "url": "https://open.spotify.com/album/2hlgpgDCuWqydJkwjBpIgP",
             "tracks": [
                 "shootin (prod. legion, Warren Hunter)",
	             "beep beep (prod. skai)",
	             "mona lisa (prod. Dycemadeit, Flynno)",
                 "maybach (prod. cranes)",
                 "fuck tsa (prod. zoot, ss3bby)",
	             "change on me (prod. skai)",
	             "u not a demon (prod. azure)",
                 "medicine taste like shit (prod. Che)",
                 "high off life (prod. gyro)",
                 "problems (prod. crane, clay10)",
                 "snapchat (prod. reklus1ve)",
                 "strong (prod. legion, Jay Trench)",
                 "10k ona dog (prod. Warren Hunter)",
                 "sumthin different (prod. legion)",
                 "team x (prod. zoot)",
                 "killin (prod. zoot, ss3bby)",
                 "$ mf (prod. mag, 444jet)",
                 "pocket bag (prod. reklus1ve, Warpstr)",
                 "young ho (prod. ss3bby, tamo bell)",
                 "sallys (prod. CXO)",
                 "goin dumb (prod. repglick)",
                 "breesh breesh (prod. Warren Hunter)",
                 "hywds (prod. reklus1ve)",
                 "bliss (prod. cranes, 444jet)",
                 "kriss kross (prod. Rok, Warren Hunter)",
                 "sonder (prod. reklus1ve)",
                 "forever never (prod. cranes)",
             ],
         },
         {
             "title": "KiCKDOOR",
             "kind": "Mixtape",          # Album / EP / Mixtape
             "year": "May 26, 2023",
             "cover": "Nettspend - U Told Us Quit.jpg",              # file name inside images/
	         "url": "https://music.youtube.com/playlist?list=PLbme6n8cqKiqkBe8wVDSAGpCFH-cD9Zne",
             "tracks": [
                       "U Told Us Quit (feat. Yungster Jack) (prod. yk, 444jet)",
	                   "That Sh*t Wont Easy (pord. reklus1ve)",
	                   "4k (prod. occult.14)",
                       "Way Up Front (prod. filthygenes)",
                       "Missing (prod. st47ic)",
	                   "Gen 5 (prod. sophitia)",
	                   "Out the whip (feat. kasper gem) (prod. ss3bby, cranes)",
                       "Smack ya (feat. phreshboyswag) (prod. nyli, XION ORION)",
             ],
         },
         {
             "title": "KiCKDOOR ++++ (Deluxe)",
             "kind": "Deluxe",          # Album / EP / Mixtape
             "year": "June 8, 2023",
             "cover": "Nettspend - KiCKDOOR Deluxe.jpg",              # file name inside images/
	         "url": "https://music.youtube.com/playlist?list=PLbme6n8cqKiocjg_vxEkQ-fvv763C6lDy",
             "tracks": [
                       "Made It Home (prod. yk, heroinsick, exset)",
	                   "Made it work (prod. cranes)",
	                   "Tell Yourself (Now Or Never) (prod. filthygenes, sophitia)",
                       "Theft (I Don't Like You) (prod. origime, sedaku)",
             ],
         },

     ],
     "singles": [
         {
             "title": "What they say (prod. jj1da)",
             "year": "January 11, 2023",
             "cover": "Nettspend - What they say.png",
             "url": "https://soundcloud.com/nettspend/what-they-say-jj1da",},
     {
             "title": "On Me (feat. Yhapojj) (prod. occult.14, mag)",
             "year": "April 22, 2023",
             "cover": "Nettspend - On Me.jpg",
             "url": "https://soundcloud.com/an6uished/nettspend-on-me-feat-yhapojj",
         },
     {
             "title": "GoOd Night (prod. jj1da, Tapie)",
             "year": "May 16, 2023",
             "cover": "Nettspend - GoOd Night.jpg",
             "url": "https://soundcloud.com/m4kk/nettspend-good-night-jj1datapie",
             "music_video": "https://www.youtube.com/watch?v=J-epEyZqP14",
         },
         {
             "title": "Beamerrr (prod. tenkay, $harpboi)",
             "year": "January 31, 2023",
             "cover": "Nettspend - Beamerrr.jpg",
             "url": "https://soundcloud.com/joodsegast/nettspend-beamerrr",},
     {
             "title": "Cryptonite (prod. xaviersobased, CJ808)",
             "year": "June 10, 2023",
             "cover": "Nettspend - Cryptonite.jpg",
             "url": "https://soundcloud.com/user-387529382/nettspend-cryptonite",
         },
         {
             "title": "U gon fall (prod. clay10, miso)",
             "year": "March 22, 2023",
             "cover": "Nettspend - U gon fall.jpg",
             "url": "https://soundcloud.com/nettspend/geo-prod-clay10-miso",
             "music_video": "https://www.youtube.com/watch?v=S_4B6aeMMec",
         },
         {
             "title": "Gen 5 (prod. sophitia)",
             "year": "May 2, 2023",
             "cover": "Nettspend - Gen 5.jpg",
             "url": "https://soundcloud.com/djphat1996/nettspendf1",
             "music_video": "https://www.youtube.com/watch?v=fekiI4Vkt9Y",
         },
         {
             "title": "Section (prod. sophitia)",
             "year": "June 13, 2023",
             "cover": "Nettspend - Section.jpg",
             "url": "https://soundcloud.com/nettspend/tex-prod-sophitia",
         },
         {
             "title": "U Told Us Quit (feat. Yungster Jack) (Prod. yk, 444jet)",
             "year": "May 23, 2023",
             "cover": "Nettspend - U Told Us Quit.jpg",
             "url": "https://soundcloud.com/nettspend/u-told-us-quit-w-yungsterjack",
         },
         {
             "title": "Hollywood (prod. Kyuro, occult.14)",
             "year": "June 16, 2023",
             "cover": "Nettspend - Hollywood.jpg",
             "url": "https://soundcloud.com/m4kk/nettspend-hollywood-kyuro-n-occult14",
         },
         {
             "title": "where the racks at (feat. Zootzie) (prod. zoot, Keyblade)",
             "year": "June 19, 2023",
             "cover": "Nettspend - where the racks at.jpg",
             "url": "https://soundcloud.com/nettspend/wheres-the-loot-w-zootzie-prod",
         },
         {
             "title": "funuhyuh (prod. zoot)",
             "year": "June 24, 2023",
             "cover": "Nettspend - funuhyuh.jpg",
             "url": "https://soundcloud.com/nettspend/backdrop",
             "music_video": "https://www.youtube.com/watch?v=qmfMX6qlK4o",
         },
         {
             "title": "Take You Out (prod. reklus1ve, votekk)",
             "year": "July 11, 2023",
             "cover": "Nettspend - Take You Out.jpg",
             "url": "https://soundcloud.com/nettspend/sip-prod-rek-votek",
             "music_video": "https://www.youtube.com/watch?v=3ryyZDJAgtk",
         },
         {
             "title": "shine n peace (prod. mag, XION ORION)",
             "year": "July 23, 2023",
             "cover": "Nettspend - shine n peace.jpg",
             "url": "https://soundcloud.com/nettspend/2mybrother-mag",
         },
         {
             "title": "Packs (feat. Duwap Kaine) (prod. ok)",
             "year": "August 7, 2023",
             "cover": "Nettspend - Packs.jpg",
             "url": "https://soundcloud.com/nettspend/lagout-ft-duwap-kaine-prod-ok",
         },
         {
             "title": "We not like you (prod. zoot)",
             "year": "August 11, 2023",
             "cover": "Nettspend - We not like you.jpg",
             "url": "https://soundcloud.com/nettspend/off-a-jet-zoot",
             "music_video": "https://www.youtube.com/watch?v=9SrWNGvrtVc",
         },
         {
             "title": "Yooo (prod. zoot)",
             "year": "August 15, 2023",
             "cover": "Nettspend - Yooo.jpg",
             "url": "https://soundcloud.com/nettspend/hey-yo-prod-zoot-mp3",
             "music_video": "https://www.youtube.com/watch?v=FrewziNwxcY",
         },
         {
             "title": "Benihana (prod. ok)",
             "year": "September 2, 2023",
             "cover": "Nettspend - Benihana.jpg",
             "url": "https://soundcloud.com/nettspend/benihana-prod-ok",
             "music_video": "https://www.youtube.com/watch?v=NoQBZUF05k8",
         },
         {
             "title": "Otw (feat. xaviersobased) (prod. ok)",
             "year": "August 24, 2023",
             "cover": "Nettspend - Otw.jpg",
             "url": "https://soundcloud.com/hoodlaundromat/otw-nettspend-feat",
         },
         {
             "title": "Drankdrankdrank (prod. zoot)",
             "year": "September 12, 2023",
             "cover": "Nettspend - Drankdrankdrank.jpg",
             "url": "https://soundcloud.com/nettspend/drank-prod-zoot",
             "music_video": "https://www.youtube.com/watch?v=wC1ho-3CZcg",
         },
         {
             "title": "Feeliinuu (prod. zoot)",
             "year": "September 8, 2023",
             "cover": "Nettspend - Feeliinuu.jpg",
             "url": "https://soundcloud.com/nettspend/im-feellin-uuu-zoot",
         },
         {
             "title": "wake up (feat. OsamaSon) (prod. ok)",
             "year": "September 30, 2023",
             "cover": "Nettspend - wake up.jpg",
             "url": "https://soundcloud.com/nettspend/wake-up-ft-osamason-prod-ok",
             "music_video": "https://www.youtube.com/watch?v=EWixEN65G7Q",
         },
         {
             "title": "Model Sex (prod. zoot)",
             "year": "October 22, 2023",
             "cover": "Nettspend - Model Sex.jpg",
             "url": "https://soundcloud.com/nettspend/model-sex-1",
         },
         {
             "title": "2024 Freestyle (prod. ok)",
             "year": "December 2, 2023",
             "cover": "Nettspend - 2024 Freestyle.jpg",
             "url": "https://soundcloud.com/nettspend/2024-freestyle",
             "music_video": "https://www.youtube.com/watch?v=PvPGEBaXMRs",
         },
         {
             "title": "40 (feat. xaviersobased) (prod. evilgiane)",
             "year": "January 11, 2024",
             "cover": "Nettspend - 40.jpg",
             "music_video": "https://www.youtube.com/watch?v=CVunLmutoJA",
             "url": "https://soundcloud.com/aloevine/40a1",
         },
         {
             "title": "Nothing like uuu (prod. ok)",
             "year": "April 28, 2024",
             "cover": "Nettspend - Nothing like uuu.jpg",
             "url": "https://soundcloud.com/nettspend/nothing-like-uuu",
         },
         {
             "title": "F*CK SWAG (prod. ok)",
             "year": "October 2, 2024",
             "cover": "Nettspend - FCK SWAG.jpg",
             "url": "https://soundcloud.com/nettspend/fck-swag-1",
             "music_video": "https://www.youtube.com/watch?v=BRfZe0mLcpw",
         },
         {
             "title": "Impact (feat. xaviersobased) (prod. ss3bby, 444jet)",
             "year": "March 18, 2025",
             "cover": "Nettspend - Impact.jpg",
             "url": "https://soundcloud.com/nettspend/impact-w-xaviersobased",
             "music_video": "https://www.youtube.com/watch?v=p1Hq68tFR4g",
         },
         {
             "title": "sober (prod. 1Deep)",
             "year": "August 21, 2026",
             "cover": "Nettspend - sober.jpg",
             "url": "https://soundcloud.com/nettspend/sober",
             "music_video": "https://www.youtube.com/watch?v=UoqaVRAF3H4",
         },
         
    ],
    },
 {
     "name": "xaviersobased",
     "image": "xaviersobased.gif",                      
     "aliases": ["34wedabeztbbyyyyy", "reivax", "dj with", "xsb", "Qanaks"],                    
     "dob": "October 23, 2003",                        
     "links": {
         "spotify": "https://open.spotify.com/artist/2oM7LMPFu882oC6jSwEqjd",
         "youtube_music": "https://music.youtube.com/@xavier1c",
         "soundcloud": "https://soundcloud.com/xaviersobased",
     },
     "projects": [
         {
             "title": "store",
             "kind": "Album",          
             "year": "January 8, 2021",
             "cover": "xaviersobased - store.jpg",              
	         "url": "https://music.youtube.com/playlist?list=OLAK5uy_nSV0MXl6mCvQz6g1URMJlZtEj78RblMDY",
             "tracks": [
                       "threat (prod. rodneyy)",
	                   "around (feat. EXODUS1900) (prod. xaviersobased)",
	                   "recording (prod. tdf)",
                       "40 (prod. zee!, Stef)",
                       "higher (feat. clay10) (prod. xaviersobased)",
	                   "flesh (prod. CJ808)",
	                   "adore (feat. st47ic) (prod. 177p, xaviersobased)",
                       "nikes (prod. cranes, CJ808, xaviersobased)",
             ],
         },


     ],
     "singles": [
         {
             "title": "don't let em in (prod. xaviersobased, Bleachdiego)",
             "year": "October 10, 2020",
             "cover": "xaviersobased - don't let em in.jpg",
             "url": "https://soundcloud.com/xaviersobased/dont-let-em-in-me-n-bleach-diego",
             "music_video": "https://www.youtube.com/watch?v=H6G-RdQpPLw",
         },
     ],
 },
    
 {
     "name": "perc40",
     "image": "perc40.jpg",                      
     "aliases": ["808Escobar",],                    
     "dob": "October 11, 2002",                        
     "links": {
         "spotify": "https://open.spotify.com/artist/5NAQeD4ZZVx75VV164Fnuz",
         "youtube_music": "https://music.youtube.com/channel/UCfaiB4VQ1vrc4INnbFrrezQ",
         "soundcloud": "https://soundcloud.com/perc40",
     },
     "projects": [
         {
             "title": "Flesh Wound",
             "kind": "Album",          
             "year": "August 29, 2025",
             "cover": "perc40 - Flesh Wound.jpg",              
	         "url": "https://music.youtube.com/playlist?list=OLAK5uy_l-v6-N78AIIiN2r64SmkIrf1I6wkYEJzo",
             "tracks": [
                       "my way (feat. OsamaSon) (prod. perc40, ohsxnta)",
	                   "a bug's life (feat. thr33) (prod. perc40)",
	                   "wish u well (feat. 1oneam) (prod. perc40, 1oneam)",
                       "another day (feat. Okaymar) (prod. perc40)",
                       "favorite song (feat. ohsxnta, OsamaSon) (prod. perc40)",
	                   "battle scars (feat. BLUEHUNNIDKB) (prod. perc40)",
	                   "jason (feat. 1oneam) (prod. perc40)",
                       "pain (feat. yuke) (prod. perc40)",
                       "tony soprano (feat. luracks) (prod. perc40)",
                       "foreign words (feat. OsamaSon) (prod. perc40)",
                       "wrong one (feat. wildkarduno) (prod. perc40)",
                       "penthouse keys (feat. 1oneam) (prod. perc40)",
                       "never no fraud (feat. Smokingskul) (prod. perc40)",
                       "change (feat. thr33) (prod. perc40)",
                       "right hand (feat. Okaymar) (prod. perc40)",
                       "stoopid (feat. Serane) (prod. perc40)",
                       "get mogged (feat. ohsxnta, OsamaSon) (prod. perc40)",
                       "2 sticks (feat. 1oneam) (prod. perc40, ohsxnta)",
                       "burnt up (feat. OsamaSon) (prod. perc40)",
                       "stay the night (feat. 1oneam, ohsxnta) (prod. perc40)",
             ],
         },

     ],
     "singles": [
         {
             "title": "",
             "year": "",
             "cover": "",
             "url": "",
         },
     ],
 },
 {
     "name": "tdf",
     "image": "tdf.jpg",                      
     "aliases": ["love4you", "onetdf"],                    
     "dob": "June 17, 2003", 
     "collectives": "Slime Krew",
     "links": {
         "spotify": "https://open.spotify.com/artist/1R2vMNz6qxQFMLynRurh3t",
         "youtube_music": "https://music.youtube.com/channel/UCcc0zZbnqDPiVckFQhgZBVQ",
         "soundcloud": "https://soundcloud.com/onetdf",
     },
     "projects": [
         {
             "title": "tdf & friends",
             "kind": "Album",          
             "year": "October 23, 2020",
             "cover": "tdf - tdf and friends.jpg",              
	         "url": "https://archive.org/details/tdf-friends",
             "tracks": [
                       "can't pass (feat. Jace!) (prod. tdf)",
	                   "so long (feat. Okaymar) (prod. tdf)",
	                   "lifestyle (feat. Dcxshy) (prod. tdf)",
                       "toys r us (feat. Flipphoneshwty) (prod. tdf)",
                       "goin up (feat. Samosthated, Nigo Chanel) (prod. tdf, twentywrld)",
	                   "soda (feat. Nerd1k) (prod. tdf, twentywrld)",
	                   "Go (feat. Khalifsb) (prod. tdf)",
                       "crying (feat. 1vory) (prod. tdf)",
             ],
         },
         {
             "title": "TDF & Friends 2",
             "kind": "Album",          
             "year": "April 9, 2021",
             "cover": "tdf - tdf and friends 2.jpg",              
	         "url": "https://music.youtube.com/playlist?list=OLAK5uy_mqAqbAPBwZxYZb0OzGHnF2lhvHELbvz7E",
             "tracks": [
                       "Don't Want Yo Hoe (feat. 1vory) (prod. tdf)",
	                   "Hot Streak (feat. Dcxshy) (prod. tdf)",
	                   "Elegance (feat. Okaymar) (prod. tdf)",
                       "First Class (feat. 4am, sholoh) (prod. tdf)",
                       "Wishing Well (feat. Northxan) (prod. tdf)",
	                   "One Of Da Goats (feat. Jeff Hefner) (prod. tdf)",
	                   "At Da Light (feat. JCapo) (prod. tdf)",
                       "Past Hoes (feat. Coldheartcvleb) (prod. tdf)",
                       "Stain (feat. 1oneam) (prod. tdf)",
                       "My Way (feat. rodneyy) (prod. tdf)",
                       "Area Code (feat. SteezyKai) (prod. tdf)",
                       "Hatin' (feat. 1banboy, BabyGoon, OnGoTaj) (prod. tdf)",
                       "Hashtag (feat. ONE YEAR) (prod. tdf)",
                       "Yeaforsure (feat. d0llywood1) (prod. tdf)",
                       "Stand It (feat. Dcxshy, Okaymar, sholoh) (prod. tdf, twentywrld)",
             ],
         },
         {
             "title": "TDF & Friends 3",
             "kind": "Album",          
             "year": "March 4, 2022",
             "cover": "tdf - tdf and friends 3.jpg",              
	         "url": "https://music.youtube.com/playlist?list=OLAK5uy_myDF47QdkoMLien4oEgxC0kB9OuN1CQ4c",
             "tracks": [
                       "Relapse (feat. Okaymar) (prod. tdf)",
	                   "So Gone (feat. 1oneam) (prod. tdf)",
	                   "Ain't No Lick (feat. froe) (prod. tdf)",
                       "Laces (feat. doxia) (prod. tdf)",
                       "Blitz (feat. 6evermir, bonxpf, ilycider, jssr, Kry4u, lebxanon, omgkeon, vlorich) (prod. tdf)",
	                   "Kickback (feat. Smokingskul) (prod. tdf)",
	                   "Coupe (feat. tana) (prod. tdf)",
                       "Pop Off (feat. BenjiCold) (prod. tdf)",
                       "9 (feat. heygwuapo) (prod. tdf)",
                       "Piccadilly (feat. rodneyy) (prod. tdf)",
                       "Vapors (feat. POLO PERKS ˂3 ˂3 ˂3) (prod. tdf)",
                       "On Sight (feat. Zootzie) (prod. tdf)",
                       "Charlotte Flair (feat. d0llywood1) (prod. tdf)",
                       "Nuh Uh (feat. Ways) (prod. tdf)",
                       "Slimes (feat. emotionals) (prod. tdf)",
                       "#onmymans (feat. tropes) (prod. tdf)",
             ],
         },


     ],
     "singles": [
         {
             "title": "",
             "year": "",
             "cover": "",
             "url": "",
         },
     ],
 },
    
 {
     "name": "bleood",
     "image": "bleood.gif",                      # file name inside images/
     "aliases": ["yung vocaloid", "m4ri", "defficile", "carmilluh", "deffici1e", "oranyan",],                    # ["Other Name", "Old Tag"]
     "dob": " March 17, 2005",                        # "1996-03-04" or "March 4, 1996"
     "collectives": ["iGore"],
     "links": {
         "spotify": "https://open.spotify.com/artist/41GfvEtCZu3KXaThpF01c1",
         "youtube_music": "https://music.youtube.com/channel/UC8CEtaDirOYBKHKWoW62S2A",
         "soundcloud": "https://soundcloud.com/bleoodbath",
     },
     "projects": [
         {
             "title": "seal of memories",
             "kind": "Mixtape",          # Album / EP / Mixtape
             "year": "November 6, 2023",
             "cover": "Bleood - seal of memories.jpg",              # file name inside images/
             "url": "https://music.youtube.com/playlist?list=PLKfEN5sKzhT0",
             "tracks": [
                 "fuhk (prod. slaywitme)",
	             "@bleood (prod. slaywitme)",
	             "annoying (feat. kynlary) (prod. bloomcr4zy)",
                 "kaname (prod. slaywitme)",
                 "blame! (prod. mag, occult.14)",
	             "aughh (prod. slaywitme)",
	             "anemia (feat. yuke) (prod. yuke)",
                 "00712 (prod. miso)",
             ],
         },
         {
             "title": "pain",
             "kind": "Mixtape",          # Album / EP / Mixtape
             "year": "March 11, 2025",
             "cover": "bleood - pain.png",              # file name inside images/
             "url": "https://music.youtube.com/playlist?list=OLAK5uy_nA_NtqtO4sxQS4_014bklwLSJmsWUE2fg",
             "tracks": [
                       "girl u drive me crazy i might crash (prod. zai)",
	                   "happy tree friends (prod. dolba)",
	                   "pain (prod. spellscasted)",
                       "creature (prod. yoi)",
                       "12 oz rasta mouse (prod. di4ary, nnotkeko)",
	                   "yngglu (prod. spellscasted)",
	                   "i kno u kno wat u did (prod. yrsci)",
                       "dont stop the party (prod. yoi)",
                       "rastafarian pill press from the future (prod. dluxx)",
                       "miley cyrus (prod. zai)",
                       "dr who (prod. yoi)",
                       "dumby (prod. spellscasted)",
                       "look everyones dead (prod. yoi, bleood)",
                       "go go (prod. yrsci)",
                       "family guy (prod. yrsci)",
             ],
         },
         {
             "title": "rascal 51",
             "kind": "Mixtape",          # Album / EP / Mixtape
             "year": "October 24, 2025",
             "cover": "bleood - rascal 51.png",              # file name inside images/
             "url": "https://music.youtube.com/playlist?list=OLAK5uy_lfNfqYFtMpCWlVBCWrNhLaDtM0GGWgde4",
             "tracks": [
                       "FUCK U BITCH I WANNA B ALONE (prod. yrsci)",
	                   "smd (prod. ivvys, Deshun)",
	                   "CHARLIE MURDER (prod. yrsci)",
                       "PINK (prod. dulio, fukkem800s)",
                       "lesbian vampire killers (prod. yrsci)",
	                   "sub zero (prod. ivvys, Onetimee)",
	                   "NOGWAPNOLIFE (prod. yrsci)",
                       "ozzy trisbourne (prod. yrsci)",
                       "i shoot shotguns off ecstasy pills (prod. yrsci)",
                       "bpd (prod. yrsci)",
                       "munni blu like rem (prod. vaunt, yrsci)",
             ],
         },
         {
             "title": "how bleood stole Xmas",
             "kind": "EP",          # Album / EP / Mixtape
             "year": "December 25, 2025",
             "cover": "bleood - how bleood stole Xmas.jpg",              # file name inside images/
             "url": "https://music.youtube.com/playlist?list=OLAK5uy_nNeJvIVo5ldovj66ZChiHowZ_1dgZSbjc",
             "tracks": [
                       "SANTA LEFT A BODY (prod. Aquasocks)",
	                   "evergreen (prod. yrsci)",
	                   "moral oral (prod. yrsci)",
                       "the snow melted between us (prod. skai)",
                       "munni & drugs (prod. yrsci, kashcot)",
	                   "NIGHTMARE BEFORE XMAS (prod. yrsci)",
             ],
         },
         {
             "title": "kill or b killd",
             "kind": "EP",          # Album / EP / Mixtape
             "year": "April 13, 2026",
             "cover": "bleood - kill or b killed.png",              # file name inside images/
             "url": "https://music.youtube.com/playlist?list=OLAK5uy_m9jzZ9frjYuSLkIAYIC5uR-_CRconmCx4",
             "tracks": [
                       "omg i really need a maybach limo (feat. Pz') (prod. yrsci)",
	                   "stick (prod. ivvys, chxncex, prodluke)",
	                   "batman (prod. aghast, 1takeshi)",
                       "MEAT (prod. yrsci)",
                       "yung accelerator (prod. ivvys, yrsci, awfultop)",
             ],
         },
         {
             "title": "PROTAGONIST",
             "kind": "Mixtape",          # Album / EP / Mixtape
             "year": "May 14, 2026",
             "cover": "bleood - PROTAGONIST.png",              # file name inside images/
             "url": "https://music.youtube.com/playlist?list=OLAK5uy_mph40CnDO4Ax1xG32WHHyJfyTOGZQ-6BY",
             "tracks": [
                       "maybach key fob (prod. chxncex)",
	                   "chrome dinosaur (prod. Aquasocks)",
	                   "codeine tears (prod. yrsci)",
                       "rub my belly (prod. prodbypatrick, chxncex, dyingtmmr)",
                       "on E (prod. yrsci)",
	                   "push (prod. yrsci)",
	                   "i aint start making money till i started doing drugs (prod. ivvys, awfultop)",
                       "ding dong (prod. Aquasocks)",
                       "friend or foe (prod. yrsci)",
             ],
         },
         {
             "title": "haunted hills",
             "kind": "EP",          # Album / EP / Mixtape
             "year": "September 11, 2026",
             "cover": "bleood - haunted hills.jpg",              # file name inside images/
             "url": "https://music.youtube.com/playlist?list=OLAK5uy_mMfFzJ4YrA_0bH3-tXrGwXszIkrDvTaaw",
             "tracks": [
                       "cryn innis coupe (prod. BenjiCold)",
	                   "fuk 12 (prod. yrsci)",
	                   "yung vocaloid (prod. yrsci)",
                       "shellshocked (prod. Deshun)",
                       "she wanna (prod. chxncex)",
             ],
         },
         {
             "title": "zombie",
             "kind": "Single",          # Album / EP / Mixtape
             "year": "August 31, 2023",
             "cover": "bleood - zombiee.jpg",              # file name inside images/
	         "url": "https://soundcloud.com/stethoscopes/sets/zombie",
             "tracks": [
                       "zombie (prod. slaywitme)",
	                   "two (feat. ZAYGUAPKID) (prod. syrealugly)",
             ],
         },
         {
             "title": "Backology",
             "kind": "EP",          # Album / EP / Mixtape
             "year": "January 3, 2023",
             "cover": "bleood - Backology.png",              # file name inside images/
	         "url": "https://archive.org/details/backology",
             "tracks": [
                       "Backology Intro (prod. xaviersobased)",
	                   "Whip It (prod. xaviersobased, ssh1be)",
	                   "Pastor (prod. ss3bby, 444jet)",
                       "Keys To The Gate (prod. XION ORION)",
                       "Six Mins (prod. xaviersobased)",
             ],
         },
         {
             "title": "ewwwww.co",
             "kind": "EP",          # Album / EP / Mixtape
             "year": "May 30, 2023",
             "cover": "bleood - ew co.png",              # file name inside images/
	         "url": "https://archive.org/details/bleood-ewwwww-co",
             "tracks": [
                       "ignorance is bliss (prod. st47ic)",
	                   "i love whipping (prod. xaviersobased)",
	                   "heart plunder (prod. damian1k)",
                       "we looking rad (feat. Acid Souljah) (prod. yk)",
             ],
         },
         {
             "title": "you dont need your skin",
             "kind": "EP",          
             "year": "May 10, 2024",
             "cover": "bleood - you dont need your skin.jpg",              
	         "url": "https://audiomack.com/bleodleakks/album/you-dont-need-your-skin",
             "tracks": [
                       "i can explain (prod. reklus1ve)",
	                   "we can do anything u want (prod. reklus1ve)",
             ],
         },
         {
             "title": "air gear",
             "kind": "EP",          
             "year": "February 26, 2023",
             "cover": "bleood - air gear.jpg",              
	         "url": "https://soundcloud.com/raveloser/sets/airgear",
             "tracks": [
                       "akito/agito (prod. st47ic)",
	                   "@ who (feat. zombycare) (prod. st47ic)",
	                   "laxatives (feat. jtxpo) (prod. st47ic)",
             ],
         },
         
     ],
     "singles": [
         {
             "title": "depression doesnt explain how i feel (prod. zatru)",
             "year": "December 6, 2023",
             "cover": "bleood - depression doesn't explain how I feel.jpg",
             "url": "https://soundcloud.com/jamarion-byrd/bleood-depression-doesnt",
         },
         {
             "title": "rip the skin off my body (prod. zatru)",
             "year": "March 9, 2024",
             "cover": "bleood - rip the skin off my body.jpg",
             "url": "https://soundcloud.com/antibrows/rip-the-skin-off-my-body",
         },
         {
             "title": "blood and needles (prod. zatru)",
             "year": "March 31, 2024",
             "cover": "bleood - blood and needles.jpg",
             "url": "https://soundcloud.com/ishowmyselfasafruittree/bleood-blood-and-needles-prod-zatru",
         },
         {
             "title": "why lie? (prod. Chase Salvia)",
             "year": "April 3, 2024",
             "cover": "bleood - why lie.png",
             "url": "https://soundcloud.com/bleoodbath/hggg",
             "music_video": "https://www.youtube.com/watch?v=lQCg_FuVkyk",
         },
         {
             "title": "bitch im unpridictable (prod. 19thou)",
             "year": "April 8, 2024",
             "cover": "bleood - bitch im unpridictable.jpg",
             "url": "https://soundcloud.com/bleoodbath/jwiub",
         },
         {
             "title": "omg (prod. gyro)",
             "year": "April 16, 2024",
             "cover": "bleood - omg.jpg",
             "url": "https://soundcloud.com/bleoodbath/gi",
         },
         {
             "title": "what is your purpose (prod. zatru)",
             "year": "April 23, 2024",
             "cover": "bleood - what is your purpose.jpg",
             "url": "https://soundcloud.com/antibrows/what-is-your-purpose-1",
         },
         {
             "title": "as above so below (prod. yuke, dontscrewmeover)",
             "year": "May 4, 2024",
             "cover": "bleood - as above so below.jpg",
             "url": "https://soundcloud.com/bleoodbath/nope-prod-yuke",
         },
         {
             "title": "everyone in the world needs bleood (prod. zatru)",
             "year": "May 6, 2024",
             "cover": "bleood - everyone in the world needs bleood.jpg",
             "url": "https://soundcloud.com/sigq/bleood-everyone-in-the-world",
             "music_video": "https://www.youtube.com/watch?v=SlupXNIBznI",
         },
         {
             "title": "wtf do u think dis is (prod. ivvys, awfultop)",
             "year": "March 28, 2024",
             "cover": "bleood - wtf do u think dis is.jpg",
             "url": "https://soundcloud.com/bleoodbath/wtf-do-u-think-this-is",
         },
         {
             "title": "i glo everyday (prod. yoi)",
             "year": "November 8, 2024",
             "cover": "bleood - i glo everyday.jpg",
             "url": "https://soundcloud.com/bleoodbath/igloeveryday",
         },
         {
             "title": "bugs are crawling under your skin (prod. yoi)",
             "year": "December 28, 2024",
             "cover": "bleood - bugs are crawling under your skin.jpg",
             "url": "https://soundcloud.com/bleoodbath/bugs-are-crawling-under-your-skin",
             "music_video": "https://www.youtube.com/watch?v=WsHSEpVEgbI",
         },
         {
             "title": "dirty coin (prod. dluxx)",
             "year": "January 21, 2025",
             "cover": "bleood - dirty coin.jpg",
             "url": "https://soundcloud.com/bleoodbath/dirty-coin",
         },
         {
             "title": "mhm 2 (prod. ivvys)",
             "year": "May 5, 2025",
             "cover": "bleood - mhm 2.jpg",
             "url": "https://soundcloud.com/drug/mhm2",
         },
         {
             "title": "alucard (prod. yrsci)",
             "year": "May 20, 2025",
             "cover": "bleood - alucard.jpg",
             "url": "https://soundcloud.com/bleoodbath/1b1e85e6-8929-4512-b9ec-2ec773b31390",
             "music_video": "https://www.youtube.com/watch?v=-_7AAffsMRM",
         },
         {
             "title": "cannibal (prod. yrsci)",
             "year": "June 21, 2025",
             "cover": "bleood - cannibal.jpg",
             "url": "https://soundcloud.com/bleoodbath/freebleoood",
         },
         {
             "title": "zombie (2025) (prod. yrsci)",
             "year": "July 25, 2025",
             "cover": "bleood - zombie.jpg",
             "url": "https://soundcloud.com/bleoodbath/zombie",
         },
         {
             "title": "trimmithy turner (prod. yrsci)",
             "year": "August 7, 2025",
             "cover": "bleood - trimmithy turner.jpg",
             "url": "https://soundcloud.com/bleoodbath/trimmithy-turner",
         },
         {
             "title": "TEEN DREAM NIGIRI (prod. yrsci)",
             "year": "November 19, 2025",
             "cover": "bleood - TEEN DREAM NIGIRI.jpg",
             "url": "https://soundcloud.com/bleoodbath/teen-dream-nigiri",
         },
         {
             "title": "nine² (prod. ivvys, prodluke, Onetimee)",
             "year": "February 20, 2026",
             "cover": "bleood - nine.jpg",
             "url": "https://soundcloud.com/bleoodbath/nine",
             "music_video": "https://www.youtube.com/watch?v=dTvI12c-VE8",
         },
         {
             "title": "i ˂3 seals (prod. prodbypatrick, chxncex)",
             "year": "April 24, 2026",
             "cover": "bleood - i love seals.jpg",
             "url": "https://soundcloud.com/bleoodbath/i-3-seals",
             "music_video": "https://www.youtube.com/watch?v=H6qdkfzOG7o",
         },
         {
             "title": "custo a burger (prod. ivvys, Onetimee, prodbypatrick)",
             "year": "July 9, 2026",
             "cover": "bleood - custo a burger.jpg",
             "url": "https://soundcloud.com/bleoodbath/custo-a-burger",
             "music_video": "https://www.youtube.com/watch?v=M3Jg89NSuto",
         },
         {
             "title": "mr. goodman munni (prod. yrsci)",
             "year": "August 6, 2026",
             "cover": "bleood - mr. goodman munni.jpg",
             "url": "https://soundcloud.com/bleoodbath/mr-goodman-munni",
         },
         {
             "title": "gygjfacb (prod. chxncex)",
             "year": "August 14, 2026",
             "cover": "bleood - gygjfacb.jpg",
             "url": "https://soundcloud.com/bleoodbath/gygjfacb",
         },
         {
             "title": "overwatch (feat. ApolloRed1) (prod. chxncex)",
             "year": "August 31, 2026",
             "cover": "bleood - overwatch.jpg",
             "url": "https://soundcloud.com/bleoodbath/overwatch-feat-apollored1",
             "music_video": "https://www.youtube.com/watch?v=Ty_xRBxl5XY",
         },
         {
             "title": "monster mash (prod. st47ic)",
             "year": "December 16, 2025",
             "cover": "bleood - monster mash.jpg",
             "url": "https://soundcloud.com/nova-v3/bleood-monster-mash-nova",
         },
         {
             "title": "ur not (prod. yuke, dontscrewmeover)",
             "year": "May 5, 2024",
             "cover": "bleood - ur not.png",
             "url": "https://soundcloud.com/q67/bleood-ur-not-yuke",
         },
         {
             "title": "xlr8 (prod. CXO, yoi)",
             "year": "September 10, 2025",
             "cover": "bleood - xlr8.jpg",
             "url": "https://soundcloud.com/jayce2525/bleood-sendy-in-the-rave",
         },
         {
             "title": "everythings the same but im different (feat. zai) (prod. dluxx)",
             "year": "November 29, 2024",
             "cover": "bleood - everythings the same but im different.jpg",
             "url": "https://soundcloud.com/maskedmagician/bleood-everythings-the-same",
         },
         {
             "title": "13 reasons u should kill yourself (prod. yoi)",
             "year": "September 26, 2024",
             "cover": "bleood - 13 reasons.png",
             "url": "https://soundcloud.com/srwwy/bleood-13-reasons-u-should-kill-yourself-yeo",
         },
         {
             "title": "dead 2 me (prod. dontscrewmeover, yuke)",
             "year": "November 17, 2024",
             "cover": "bleood - dead 2 me.jpg",
             "url": "https://soundcloud.com/antibrows/dead-2-me",
             "music_video": "https://www.youtube.com/watch?v=avZ5V2OSaE0",
         },
         {
             "title": "2 ceups 1 bleood (prod. gyro)",
             "year": "June 22, 2024",
             "cover": "bleood - 2 ceups 1 bleood.jpg",
             "url": "https://soundcloud.com/bleoodbath/2ceup",
             "music_video": "https://www.youtube.com/watch?v=mSjN9CULv3o",
         },
         {
             "title": "enamored with dread (prod. damian1k)",
             "year": "May 18, 2022",
             "cover": "bleood - enamored with dread.png",
             "url": "https://soundcloud.com/g2ibunnyboy/defficile-enamored-with-dread",
             "music_video": "https://www.youtube.com/watch?v=R799hKudQCM",
         },
         {
             "title": "sunny (prod. eden)",
             "year": "November 15, 2024",
             "cover": "bleood - sunny.jpg",
             "url": "https://soundcloud.com/femhinn/bleood-sunny",
         },
         {
             "title": "ipray2miku (prod. eden)",
             "year": "November 2, 2024",
             "cover": "bleood - ipray2miku.jpg",
             "url": "https://soundcloud.com/packrunnercris/bleood-ipray2miku-eden",
         },
         {
             "title": "its raining just cats (feat. suban) (prod. eden)",
             "year": "November 19, 2024",
             "cover": "bleood - its raining just cats.jpg",
             "url": "https://soundcloud.com/femhinn/bleood-its-raining-just-cats-suban",
         },
         {
             "title": "its raining cats and dogs (feat. zai) (prod. yuke, dontscrewmeover)",
             "year": "2024",
             "cover": "bleood - its raining cats and dogs.jpg",
             "url": "https://soundcloud.com/infect/bleood-its-raining-cats-and",
         },
         
     ],
 },
 {
     "name": "elijxhwtf",
     "image": "elijxhwtf.jpg",                      
     "aliases": ["",],                    
     "dob": "August 12, 2007",
     "collectives": "Slime Krew",
     "links": {
         "spotify": "https://open.spotify.com/artist/5Uawcilahy8UUYUNiO5tL5",
         "youtube_music": "https://music.youtube.com/channel/UCV5A2_fWv9umfiWwTjtqaQg",
         "soundcloud": "https://soundcloud.com/elijxhwtf",
     },
     "projects": [
         {
             "title": "you need people like me",
             "kind": "Album",          
             "year": "March 8, 2024",
             "cover": "elijxhwtf - you need people like me.jpg",              
	         "url": "https://music.youtube.com/playlist?list=OLAK5uy_lZheJMe05YciJYCRR34Wny2n-Wnp4Q0w8",
             "tracks": [
                       "mob (prod. offlxne)",
	                   "x (prod. Xatthew)",
	                   "wrist (prod. Goscow, offlxne)",
                       "chef (prod. 19thou)",
                       "waist (prod. Goscow)",
	                   "hey (prod. offlxne)",
	                   "michael phelps (prod. 19thou)",
                       "script (prod. offlxne)",
                       "act (prod. marques)",
             ],
         },
         {
             "title": "the world is yours",
             "kind": "Album",          
             "year": "June 29, 2023",
             "cover": "elijxhwtf - the world is yours.jpg",              
	         "url": "https://music.youtube.com/playlist?list=OLAK5uy_kqdc6liw_YfxRPm6JmYcuMdomD8UN25xU",
             "tracks": [
                       "mexican (prod. sanctified, Dwsn)",
	                   "taekwondo (prod. Thrty, xanocery, Marrgielaa)",
	                   "show n tell 2 (prod. 19thou)",
                       "shots (feat. OsamaSon) (prod. Thrty, Jahsters)",
                       "slatt (prod. Goscow)",
	                   "trackhawk (prod. Thrty)",
	                   "who (prod. offlxne)",
                       "heart (prod. Luke2k)",
             ],
         },
         {
             "title": "who i trust",
             "kind": "Album",          
             "year": "February 8, 2025",
             "cover": "elijxhwtf - who i trust.jpg",              
	         "url": "https://music.youtube.com/playlist?list=OLAK5uy_mnI-Z44CBHaFnCdqp49Na3rupZ_mV60qQ",
             "tracks": [
                       "savior (prod. offlxne)",
	                   "vision (prod. elijxhwtf, 19thou)",
	                   "shut up (prod. 19thou)",
                       "nun 2 me (prod. elijxhwtf, Goscow)",
                       "raq (prod. Xatthew)",
	                   "birkin (prod. offlxne, Goscow)",
	                   "kill me (feat. killjae) (prod. offlxne)",
                       "hopout (prod. boolymon)",
                       "tupac (prod. tdf)",
                       "all i had 2 ask (prod. elijxhwtf)",
                       "why (prod. elijxhwtf)",
                       "my bad (prod. boolymon)",
                       "xanax (prod. elijxhwtf, twovrt, boolymon)",
                       "purpose (prod. Jahsters)",
                       "said nun (prod. offlxne)",
                       "juggnrock (prod. Jahsters)",
                       "momma (prod. Luke2k)",
             ],
         },


     ],
     "singles": [
         {
             "title": "onnat (prod. 19thou)",
             "year": "July 7, 2022",
             "cover": "elijxhwtf - Onnat.jpg",
             "url": "https://soundcloud.com/elijxhwtf/onnat",
         },
     ],
 },
 
 {
     "name": "ApolloRed1",
     "image": "ApolloRed1.gif",                      # file name inside images/
     "aliases": ["Apollo Red",],                    # ["Other Name", "Old Tag"]
     "dob": "June 5, 2002",                        # "1996-03-04" or "March 4, 1996"
     "links": {
         "spotify": "https://open.spotify.com/artist/6woKompAdi85uFZpAcqPhP",
         "youtube_music": "https://music.youtube.com/@apollored1",
         "soundcloud": "https://soundcloud.com/user-236037367",
     },
     "projects": [
         {
             "title": "The Summer I Turned RED",
             "kind": "Mixtape",          # Album / EP / Mixtape
             "year": "September 9, 2024",
             "cover": "ApolloRed1 - The Summer I Turned RED.jpg",              # file name inside images/
	         "url": "https://music.youtube.com/playlist?list=OLAK5uy_mBSTaLTY6KVLfocVI6EtLluDlT_V8mpZI",
             "tracks": [
                       "1700 (Trip Intro) (prod. Ayelavish!)",
	                   "00President (prod. SouljaSpirits)",
	                   "SwiPe! (prod. Goxan, JDON)",
                       "Phoenix Nights at 20 (prod. Ayelavish!)",
                       "YVL Anthem (prod. Goxan, SouljaSpirits)",
	                   "EMO Thug (prod. JDON)",
	                   "VamPed uP (feat. lilflame29) (prod. Twonine, Goxan)",
                       "Idolize (prod. Clayco, John M Weir)",
                       "Stick Party (prod. SouljaSpirits, Konvict)",
                       "Losin' My Mind (prod. Twonine, Goxan, SouljaSpirits)",
                       "FindAht! (prod. Goxan, SouljaSpirits, Ayelavish!)",
                       "Use to (prod. Clayco, Akachi)",
                       "Feelin' Like Wayne (prod. Ayelavish!)",
                       "Be lik me (prod. JDON, SouljaSpirits)",
                       "Kould've Been (prod. Twonine, Goxan)",
                       "Bury Me in Diamonds (prod. Fuckshiro)",
                       "Blood Angelsn (prod. Ayelavish!)",
             ],
         },
         {
             "title": "Midnight Blassic",
             "kind": "Mixtape",          # Album / EP / Mixtape
             "year": "May 16, 2025",
             "cover": "ApolloRed1 - Midnight Blassic.jpg",              # file name inside images/
	         "url": "https://music.youtube.com/playlist?list=OLAK5uy_nX048jbWjDv4dXbHrpOTzINpE8dSajJ9Q",
             "tracks": [
                       "PBrazY (prod. Clayco, Opm Babi, Nick Spiders, Streo)",
	                   "Beauty Pageant (prod. Ayelavish!)",
	                   "Georgia Boy (prod. F1LTHY, Warpstr)",
                       "Ready2Purge (prod. Bakkwoods, Twonine, Tdogg)",
                       "Hallucinating (prod. 100yrd, Brak3, MAYCRY)",
	                   "Face Tattoos (prod. FILTHY, Lukrative, ssort, Prod. 5$star)",
	                   "Gotta B (prod. KP Beatz, Warpstr, xgiannii)",
                       "XO Tourlyfe (prod. 1st Class, Yougomajor, Senk)",
                       "Rick Addiction (prod. Clayco, BryceUknwn, y2tnb)",
                       "Delta (prod. Clayco, KP Beatz) ",
                       "Tom Holland (prod. Trgc, Bakkwoods, RAFMADE, ATM James)",
                       "Halo (prod. Bakkwoods, Twonine, Tjay)",
                       "Honest (prod. Twonine, Sohi)",
                       "Chanel Shooter (prod. 16yrold, 406ahmad)",
                       "Drug Love Demo 2 (prod. Trgc)",
                       "Back to that (prod. Trgc)",
             ],
         },
         {
             "title": "Demon Heart Radio",
             "kind": "Album",          # Album / EP / Mixtape
             "year": "June 5, 2026",
             "cover": "ApolloRed1 - Demon Heart Radio.jpg",              # file name inside images/
	         "url": "https://music.youtube.com/playlist?list=OLAK5uy_llBaQ7ne-_KaUV0CF6RI3DCL_DxGkTdcQ",
             "tracks": [
                       "#Demon (feat. Bryant Barnes) (prod. Cardo Got Wings, Johnny Juliano, Keymajor)",
	                   "Where im @ (prod. benlywya, Bakkwoods, CXSKET, icedmn)",
	                   "Pink! (prod. Ayelavish!)",
                       "#SRT (prod. ADHD, SouljaSpirits)",
                       "More Time (prod. Trgc, Tjay)",
	                   "Love you > Myself (prod. Opm Babi, Clayco, Streo)",
	                   "Shell (prod. 16yrold, CLOUD 48, plenty, CXL)",
                       "OnYohead! (prod. Bugz Ronin, Leiso, young emphasis)",
                       "Codeine Shower (feat. Destroy Lonely) (prod. ADHD, Cole Igou, MunMadeIt)",
                       "Can't Go (prod. Ayelavish!, Gfelds, skreer)",
                       "Caution (prod. leadbluntt, xgiannii, mental, sean baby)",
                       "Geeked up (feat. OsamaSon) (prod. 1st Class, Bakkwoods, Surcha, Alawais)",
                       "ARP my bitch (prod. southboy, trisstt, hastell)",
                       "Drive uP (prod. F1LTHY, chenzo, Saahil)",
                       "Tight pants (prod. Section 8, Fazi, Franky, Acog, skreer)",
                       "Pullup## (prod. Chris Clay)",
                       "Hood-Made (prod. Zodiac)",
                       "Set you free (prod. Opm Babi, Clayco, Streo, cuvieeeee)",
                       "Machete (prod. 16yrold, Twonine, KRAGER)",
                       "#NoCrash (prod. 16yrold, KRAGER, Juuzi)",
             ],
         },
         {
             "title": "ApolloRed1 vs The World",
             "kind": "Mixtape",          # Album / EP / Mixtape
             "year": "October 1, 2025",
             "cover": "ApolloRed1 - ApolloRed1 vs The World.jpg",              # file name inside images/
	         "url": "https://music.youtube.com/playlist?list=PLyVJWizfqMdLDdqNrDrHuIB0A_aM7LMaZ",
             "tracks": [
                       "No Running (prod. 2C, highsoulja)",
	                   "Benz mf (feat. Protect) (prod. Clayco, Opm Babi, n9ck, fuckperk)",
	                   "Riot (prod. Goxan, JDON)",
                       "Contraband (prod. leadbluntt, Clayco, 16yrold, Bakkwoods)",
                       "Loaded Diper (prod. 1st Class, dayever)",
	                   "#ARP (prod. Ayelavish!, Stuzzy, HARZ)",
	                   "Profit (prod. Goxan, K6WYA)",
                       "Bad Bitch Fetish (feat. Nine Vicious) (prod. 16yrold, 33empathy)",
                       "10:03 (prod. Trgc)",
                       "headed2thesky (prod. Trgc, Bakkwoods, RAFMADE, ATM James)",
                       "Vamp Language (feat. Destroy Lonely) (prod. Bugz Ronin, Leiso)",
             ],
         },

     ],
     "singles": [
         {
             "title": "Off Da Rip (prod. prodbyNAJ$)",
             "year": "February 8, 2023",
             "cover": "ApolloRed1 - Off Da Rip.jpg",
             "url": "https://soundcloud.com/user-236037367/off-da-rip-prodbynaj",
         },

     ],
 },
 
 {
     "name": "2slimey",
     "image": "2slimey.gif",                      # file name inside images/
     "aliases": ["GGS", "King Shrimp"],                    # ["Other Name", "Old Tag"]
     "dob": "January 24, 2006",                        # "1996-03-04" or "March 4, 1996"
     "links": {
         "spotify": "https://open.spotify.com/artist/0ZXbQLu4a7sk3iQ8tlgFy4",
         "youtube_music": "https://music.youtube.com/@2slimeyX",
         "soundcloud": "https://soundcloud.com/2slimey4eva",
     },
     "projects": [
         {
             "title": "SsoMe",
             "kind": "Mixtape",          # Album / EP / Mixtape
             "year": "November 29, 2024",
             "cover": "2slimey - SsoMe.jpg",              # file name inside images/
             "url": "https://music.youtube.com/playlist?list=OLAK5uy_mTK-ojPDtdZydwXHKyvCXNJHj-eiOg7rY",
             "music_video": "https://www.youtube.com/watch?v=hZiygbK-fgQ",
             "tracks": [
                       "MakkUp (prod. ok)",
	                   "SaddestStory (prod. vlor5k)",
	                   "Draco Talk (prod. sorrovw, byt)",
                       "Mexiko (feat. Mikebrokeasf) (prod. vlor5k)",
                       "Bad Hoe (prod. Vlac)",
	                   "What You Doin (feat. Yhapojj) (prod. Tricksterr, CettiWorld, Sleepy)",
	                   "Topp (prod. thr6x)",
                       "So Far (prod. Yakree, Pilgrim)",
                       "Serena (prod. vlor5k)",
                       "shrimp (prod. Vlac)",
             ],
         },
         {
             "title": "High Anxiety",
             "kind": "Album",          # Album / EP / Mixtape
             "year": "November 14, 2025",
             "cover": "2slimey - high anxiety.jpg",              # file name inside images/
             "url": "https://music.youtube.com/playlist?list=OLAK5uy_nYjCzqlKN8p_Y0xtsrEhppwwEJPKWq6Ps",
             "tracks": [
                       "Bring emOut (prod. mental, thr6x)",
	                   "I serve bass (prod. vlor5k)",
	                   "Roc (prod. vlor5k)",
                       "Shoot atU (prod. juceex, xkxx, byt)",
                       "Rolling Off Molly (prod. xkxx, kendal94)",
	                   "Pop alot (prod. fl0wzy, xceff)",
	                   "Race Car (feat. BabyTron) (prod. xkxx, byt)",
                       "redMoon (prod. Noah Mejia, 333synx, pouritupsoda)",
                       "In her Jaw (feat. Izaya Tiji) (prod. vlor5k)",
                       "Linkup (prod. vlor5k)",
                       "oMg (prod. xkxx, byt)",
                       "Lets go home (prod. ok, Malvi)",
                       "Meat (prod. xkxx, byt)",
                       "live in bass (prod. vlor5k)",
                       "Kitgo (prod. vlor5k)",
             ],
         },
         {
             "title": "More Anxiety",
             "kind": "Deluxe",          # Album / EP / Mixtape
             "year": "February 6, 2026",
             "cover": "2slimey - more anxiety.jpg",              # file name inside images/
             "url": "https://music.youtube.com/playlist?list=OLAK5uy_lBFcAJCMjMaIKsU3Fu3nBPQLQuAcSau70",
             "tracks": [
                       "Throw up (prod. 15drtt, mental, Synthetic)",
                       "Dirty bitch (prod. 333synx, tainiykick, Noah Mejia, pouritupsoda)",
                       "Kut up (prod. jetski)",
                       "Power (prod. mental)",
                       "Baby drac (prod. vlor5k)",
                       "Belly (prod. pwfuu, Synthetic)",
                       "punkPunk (prod. vlor5k, Synthetic, bass)",
                       "Legion (prod. fl0wzy, mental)",                     
                       "Bring emOut (prod. mental, thr6x)",
	                   "I serve bass (prod. vlor5k)",
	                   "Roc (prod. vlor5k)",
                       "Shoot atU (prod. juceex, xkxx, byt)",
                       "Rolling Off Molly (prod. xkxx, kendal94)",
	                   "Pop alot (prod. fl0wzy, xceff)",
	                   "Race Car (feat. BabyTron) (prod. xkxx, byt)",
                       "redMoon (prod. Noah Mejia, 333synx, pouritupsoda)",
                       "In her Jaw (feat. Izaya Tiji) (prod. vlor5k)",
                       "Linkup (prod. vlor5k)",
                       "oMg (prod. xkxx, byt)",
                       "Lets go home (prod. ok, Malvi)",
                       "Meat (prod. xkxx, byt)",
                       "live in bass (prod. vlor5k)",
                       "Kitgo (prod. vlor5k)",             
             ],
         },
         {
             "title": "Totalbass",
             "kind": "EP",          # Album / EP / Mixtape
             "year": "June 26, 2026",
             "cover": "2slimey - Totalbass.jpg",              # file name inside images/
	         "url": "https://music.youtube.com/playlist?list=OLAK5uy_n2N7C0DTWAvgKGgmdttdTC39mFtPbRWek",
             "tracks": [
                       "Left Right (prod. xkxx, tainiykick, 333synx)",
	                   "Wine (prod. mental)",
	                   "lobby (prod. vlor5k)",
                       "Bentley & Lambs (prod. Noah Mejia, shinju)",
                       "Ballout (prod. pwfuu)",
	                   "Money Dumb (prod. Noah Mejia, Synthetic)",
             ],
         },
         
     ],
     "singles": [
         {
             "title": "TOPSLIME (feat. BBKnight)",
             "year": "July 17, 2021",
             "cover": "2slimey - TOPSLIME.jpg",
             "url": "https://soundcloud.com/2slimey-sc/topslime-feat-bbknight",
         },
         {
             "title": "TOPSLIME 2.0 (feat. Smoove Dinero)",
             "year": "September 21, 2021",
             "cover": "2slimey - TOPSLIME 2.0.jpg",
             "url": "https://soundcloud.com/2slimey-sc/topslime-2-0-feat-smoove",
         },
         {
             "title": "Kutta (feat. Nutso Thugn)",
             "year": "November 15, 2021",
             "cover": "2slimey - Kutta.jpg",
             "url": "https://soundcloud.com/2slimey-sc/kutta-feat-nutso-thugn",
         },
         {
             "title": "On Glo!",
             "year": "January 24, 2022",
             "cover": "2slimey - On Glo!.jpg",
             "url": "https://soundcloud.com/2slimey-sc/on-glo",
         },
         {
             "title": "2 Wick!",
             "year": "November 8, 2022",
             "cover": "2slimey - 2 Wick!.jpg",
             "url": "https://soundcloud.com/2slimey-sc/2-wick",
         },
         {
             "title": "Xtra Rich",
             "year": "June 18, 2023",
             "cover": "2slimey - Xtra Rich.jpg",
             "url": "https://soundcloud.com/2slimey-sc/xtra-rich",
         },
         {
             "title": "Kullinan",
             "year": "July 24, 2023",
             "cover": "2slimey - Kullinan.jpg",
             "url": "https://soundcloud.com/2slimey-sc/kullinan",
         },
         {
             "title": "Not Over Me (prod. sorrovw)",
             "year": "October 15, 2023",
             "cover": "2slimey - Not Over Me.jpg",
             "url": "https://soundcloud.com/2slimey-sc/not-over-me",
         },
         {
             "title": "Glo reign",
             "year": "January 21, 2024",
             "cover": "2slimey - Glo reign.jpg",
             "url": "https://soundcloud.com/2slimey-sc/glo-reign",
         },
         {
             "title": "shrimp (prod. Vlac)",
             "year": "March 9, 2024",
             "cover": "2slimey - shrimp.jpg",
             "url": "https://soundcloud.com/2slimey4eva/shrimp",
             "music_video": "https://www.youtube.com/watch?v=lz9v-m_tapg",
         },
         {
             "title": "swamp (prod. Vlac)",
             "year": "April 6, 2024",
             "cover": "2slimey - swamp.jpg",
             "url": "https://soundcloud.com/2slimey4eva/swamp",
         },
         {
             "title": "no diddy (prod. wixxo, Vlac)",
             "year": "April 20, 2024",
             "cover": "2slimey - no diddy.jpg",
             "url": "https://soundcloud.com/2slimey4eva/no-diddy",
         },
         {
             "title": "PSA (feat. BabySolid)",
             "year": "May 12, 2024",
             "cover": "2slimey - PSA.jpg",
             "url": "https://soundcloud.com/2slimey4eva/psa-ft-babysolid-djbanned-1",
             "music_video": "https://www.youtube.com/watch?v=yR2qAjec-10",
         },
         {
             "title": "Traplantix (prod. vlor5k)",
             "year": "May 21, 2024",
             "cover": "2slimey - Traplantix.jpg",
             "url": "https://soundcloud.com/2slimey4eva/traplantix-vlor5k",
         },
         {
             "title": "Mike vixk (prod. vlor5k)",
             "year": "June 8, 2024",
             "cover": "2slimey - Mike vixk.jpg",
             "url": "https://soundcloud.com/2slimey4eva/mike-vixk-vlor5k-1",
         },
         {
             "title": "spinkrew (prod. Ninexool)",
             "year": "June 20, 2024",
             "cover": "2slimey - spinkrew.jpg",
             "url": "https://soundcloud.com/2slimey4eva/spinkrew-djrennessy-exclusive",
         },
         {
             "title": "SsoSlime (feat. Yhapojj) (prod. Bkwds, KTP)",
             "year": "June 28, 2024",
             "cover": "2slimey - SsoSlime.jpg",
             "url": "https://soundcloud.com/2slimey4eva/ssoslime-ft-yhapojj-bwkds-ktp",
             "music_video": "https://www.youtube.com/watch?v=_dv1Asqa9Kg",
         },
         {
             "title": "Tmz (prod. vlor5k)",
             "year": "July 13, 2024",
             "cover": "2slimey - Tmz.jpg",
             "url": "https://soundcloud.com/2slimey4eva/tmz-vlor5k",
             "music_video": "https://www.youtube.com/watch?v=XXdOT3IsgUE",
         },
         {
             "title": "Hit da feet (feat. wildkarduno) (prod. 19thou, Yakree)",
             "year": "July 20, 2024",
             "cover": "2slimey - Hit da feet.jpg",
             "url": "https://soundcloud.com/2slimey4eva/hit-da-feet-ft-wildkarduno",
         },
         {
             "title": "Rude (feat. Lil Novi)",
             "year": "July 24, 2024",
             "cover": "2slimey - Rude.jpg",
             "url": "https://soundcloud.com/1slipbrick/2slimey-lil-novi-rude-slipbrick-exclusive",
         },
         {
             "title": "Serena (prod. vlor5k)",
             "year": "August 7, 2024",
             "cover": "2slimey - Serena.jpg",
             "url": "https://soundcloud.com/2slimey4eva/serena-vlor5k",
             "music_video": "https://www.youtube.com/watch?v=luQIkjJQdlA",
         },
         {
             "title": "Zoo Bity (prod. krash)",
             "year": "August 24, 2024",
             "cover": "2slimey - Zoo Bity.jpg",
             "url": "https://soundcloud.com/2slimey4eva/zoo-bity-krashvegas",
         },
         {
             "title": "Bin laden (prod. Natepack)",
             "year": "September 21, 2024",
             "cover": "2slimey - bin laden.jpg",
             "url": "https://soundcloud.com/2slimey4eva/bin-laden-natepack",
         },
         {
             "title": "Daniel Larson",
             "year": "October 2, 2024",
             "cover": "2slimey - daniel larson.jpg",
             "url": "https://soundcloud.com/slumpaudiosradio/2slimey-daniel-larson-slump-audios-exclusive-dj-banned",
         },
         {
             "title": "Slimekoat (prod. vlor5k)",
             "year": "October 28, 2024",
             "cover": "2slimey - Slimekoat.jpg",
             "url": "https://soundcloud.com/2slimey4eva/slimekoat-vlor5k",
         },
         {
             "title": "Reef (prod. Djae1k)",
             "year": "January 14, 2025",
             "cover": "2slimey - Reef.jpg",
             "url": "https://soundcloud.com/2slimey4eva/reef-djae1k",
             "music_video": "https://www.youtube.com/watch?v=cJH9vRCODdA",
         },
         {
             "title": "Munyun (prod. byt, sorrovw)",
             "year": "February 9, 2025",
             "cover": "2slimey - munyun.jpg",
             "url": "https://soundcloud.com/2slimey4eva/munyun-byttt-sorrovw",
         },
         {
             "title": "Healin (prod. m4wth)",
             "year": "February 14, 2025",
             "cover": "2slimey - Healin.jpg",
             "url": "https://soundcloud.com/2slimey4eva/healin-mw4th",
             "music_video": "https://www.youtube.com/watch?v=z2nqIcLyzNw",
         },
         {
             "title": "S3X (prod. LIF3ALRT)",
             "year": "March 8, 2025",
             "cover": "2slimey - S3X.jpg",
             "url": "https://soundcloud.com/2slimey4eva/s3x-1",
         },
         {
             "title": "Jungle (prod. vlor5k)",
             "year": "March 28, 2025",
             "cover": "2slimey - Jungle.jpg",
             "url": "https://soundcloud.com/2slimey4eva/jungle-vlor5k",
             "music_video": "https://www.youtube.com/watch?v=FV37VOqezcY",
         },
         {
             "title": "Surf (prod. 15drtt)",
             "year": "April 27, 2025",
             "cover": "2slimey - Surf.jpg",
             "url": "https://soundcloud.com/2slimey4eva/surf-15drrtt",
             "music_video": "https://www.youtube.com/watch?v=cif4uzobcDA",
         },
         {
             "title": "no auto (feat. Samosthated) (prod. TRAPMONEYBIGGIE)",
             "year": "May 19, 2025",
             "cover": "2slimey - no auto.jpg",
             "url": "https://soundcloud.com/slumpaudiosradio/2slimey-samosthated-no-auto",
             "music_video": "https://www.youtube.com/watch?v=PAPssGQbVmM",
         },         
         {
             "title": "Krispy (prod. vlor5k)",
             "year": "May 20, 2025",
             "cover": "2slimey - Krispy.jpg",
             "url": "https://soundcloud.com/2slimey4eva/2slimey-krispy",
         },
         {
             "title": "pounds n counters (prod. xkxx, byt)",
             "year": "June 4, 2025",
             "cover": "2slimey - pounds n counters.jpg",
             "url": "https://soundcloud.com/2slimey4eva/pounds-n-counters-bytt-kxx",
             "music_video": "https://www.youtube.com/watch?v=HEIX2WgjJ8U",
         },
         {
             "title": "Vet (prod. 15drtt)",
             "year": "June 21, 2025",
             "cover": "2slimey - Vet.jpg",
             "url": "https://soundcloud.com/2slimey4eva/vet-15drtt",
             "music_video": "https://www.youtube.com/watch?v=vBoKLPKP8J0",
         },
         {
             "title": "Giraffes (prod. 15drtt)",
             "year": "October 4, 2025",
             "cover": "2slimey - Giraffes.jpg",
             "url": "https://soundcloud.com/2slimey4eva/giraffes-15drtt",
         },
         {
             "title": "times changin (prod. vlor5k)",
             "year": "March 20, 2026",
             "cover": "2slimey - times changin.jpg",
             "url": "https://soundcloud.com/2slimey4eva/times-changin",
             "music_video": "https://www.youtube.com/watch?v=-PC49dWgTPc",
         },
         {
             "title": "free slimey (prod. truslo)",
             "year": "April 8, 2026",
             "cover": "2slimey - Free slimey.jpg",
             "url": "https://soundcloud.com/2slimey4eva/free-slimey",
             "music_video": "https://www.youtube.com/watch?v=voOSiSVD1Wg",
         },
         {
             "title": "Kno you (prod. pwfuu)",
             "year": "May 8, 2026",
             "cover": "2slimey - Kno you.jpg",
             "url": "https://soundcloud.com/2slimey4eva/kno-you",
             "music_video": "https://www.youtube.com/watch?v=K9QkbfC7rCw",
         },
         {
             "title": "Luv cup (prod. Prod. Charlie)",
             "year": "July 31, 2026",
             "cover": "2slimey - Luv cup.jpg",
             "url": "https://soundcloud.com/2slimey4eva/luv-cup-1",
         },
         {
             "title": "Doug fit (prod. LVL, vlor5k)",
             "year": "August 17, 2026",
             "cover": "2slimey - Doug fitt.jpg",
             "url": "https://soundcloud.com/2slimey4eva/doug-fit",
         },
         {
             "title": "critical (prod. pouritupsoda, Noah Mejia, FlippenJosh)",
             "year": "August 28, 2026",
             "cover": "2slimey - critical.jpg",
             "url": "https://soundcloud.com/2slimey4eva/critical-2",
         },
         {
             "title": "Die for this (prod. mental)",
             "year": "September 25, 2026",
             "cover": "2slimey - Die for this.jpg",
             "url": "https://soundcloud.com/2slimey4eva/die-for-this",
         },
         
     ],
 },
{
     "name": "jaydes",
     "image": "jaydes.gif",                      # file name inside images/
     "aliases": ["witchposse", "Yen", "yaphoment", "blunt_blunt_blunt", "yentheterrible", "kimichrist", "kimi", "jaydeschrist", "Nunya", "evvls", "lord", "kimi 2"],                    # ["Other Name", "Old Tag"]
     "dob": "February 24, 2006",                        # "1996-03-04" or "March 4, 1996"
     "collectives": "najma",
     "links": {
         "spotify": "https://open.spotify.com/artist/5zI4LODdVYwnKZHv4mDHRv",
         "youtube_music": "https://music.youtube.com/channel/UCZSSwDVMEvH_AEI-KX1apWQ",
         "soundcloud": "https://soundcloud.com/jaydes",
     },
     "projects": [
         {
             "title": "entry log",
             "kind": "Compilation",          # Album / EP / Mixtape
             "year": "December 20, 2021",
             "cover": "jaydes - entry log.jpg",              # file name inside images/
             "url": "https://open.spotify.com/album/67qaM4rZLNIwFgGvgBY7Hv",
             "tracks": [
                       "entry one",
	                   "entry two",
	                   "entry three",
                       "entry four (prod. jaydes)",
                       "entry five (prod. jaydes)",
	                   "entry six (prod. jaydes)",
             ],
         },
         {
             "title": "!?",
             "kind": "EP",          # Album / EP / Mixtape
             "year": "December 31, 2021",
             "cover": "jaydes - ! question mark.jpg",              # file name inside images/
             "url": "https://music.youtube.com/playlist?list=OLAK5uy_kRsQi8k1dywHbZigmtz9UpNY89_f3kSWw",
             "tracks": [
                       "intro (prod. Will Rhead)",
	                   "sick (prod. Iankon)",
	                   "scam likely (prod. MexikoDro)",
                       "passive aggression (feat. Yung Fazo) (prod. Silo)",
                       "hearts (prod. jaydes)",
             ],
         },
         {
             "title": "romanticism",
             "kind": "EP",          # Album / EP / Mixtape
             "year": "April 22, 2022",
             "cover": "jaydes - romanticism.jpg",              # file name inside images/
             "url": "https://music.youtube.com/playlist?list=OLAK5uy_kF27fCRBsEcnPmvoFmy2nsOeXkmcEcydc",
             "tracks": [
                       "4u (prod. jaydes)",
	                   "tylenol (prod. quinn)",
	                   "migraine (prod. beabadoobee)",
                       "convenience (prod. Silo)",
             ],
         },
         {
             "title": "heartpacing",
             "kind": "EP",          # Album / EP / Mixtape
             "year": "August 13, 2022",
             "cover": "jaydes- heart pacing.png",              # file name inside images/
             "url": "https://music.youtube.com/playlist?list=OLAK5uy_l71hwlQOc9WnAslc0Jx5rd0ByMeapxyPw",
             "tracks": [
                       "built off slime (prod. jaydes)",
	                   "who can i trust (feat. Rich Amiri) (prod. jaydes)",
	                   "stuck to script (prod. jaydes)",
                       "sedated (prod. jaydes)",
                       "don't worry bout Me (prod. jaydes)",
	                   "patience (feat. Riovaz) (prod. jaydes)",
	                   "never meet your idols (prod. jaydes, kkei3)",
                       "drama queen (prod. jaydes)",
                       "hateinterlude (prod. jaydes)",
             ],
         },
         {
             "title": "sativa",
             "kind": "EP",          # Album / EP / Mixtape
             "year": "November 5, 2022",
             "cover": "jaydes -sativa.jpg",              # file name inside images/
             "url": "https://music.youtube.com/playlist?list=OLAK5uy_kkjILt33Bi0fFqHvMSGrFqFZrLa3FU3Yw",
             "tracks": [
                       "gelato (prod. jaydes, Hoodrixh)",
	                   "tell me (prod. jaydes, Hoodrixh)",
	                   "cartier (prod. AltoSGP)",
             ],
         },
         {
             "title": "bipolar",
             "kind": "EP",          # Album / EP / Mixtape
             "year": "April 13, 2024",
             "cover": "jaydes - bipolar.jpg",              # file name inside images/
	         "url": "https://music.youtube.com/playlist?list=OLAK5uy_l2fNsz_BaEuUKKnIhvQyYCIbjL8UhEukM",
             "tracks": [
                       "take you away (prod. John Waite, Chas Sandford, Mark Leonard)",
	                   "sloth (prod. jaydes)",
	                   "i kno what's going to happen to me (prod. jaydes)",
                       "disassembled (prod. The Police, Hugh Padgham)",
                       "insomnia (prod. jaydes, Stef Sinclair)",
	                   "pixxa (prod. xaviersobased)",
             ],
         },
         {
             "title": "Panic",
             "kind": "EP",          # Album / EP / Mixtape
             "year": "October 31, 2024",
             "cover": "jaydes - Panic.jpg",              # file name inside images/
	         "url": "https://music.youtube.com/playlist?list=OLAK5uy_m-4LM60cd0S4WeNes7YqWshDDhy6Vi8TY",
             "tracks": [
                       "stan (prod. jaydes)",
	                   "piss (prod. jaydes)",
	                   "babies (prod. Alex G)",
                       "die (prod. SXZU, Erik Rottenburg)",
                       "cry (prod. Dead Yami)",
	                   "lowlife (prod. jaydes)",
             ],
         },
         {
             "title": "Lord",
             "kind": "Album",          # Album / EP / Mixtape
             "year": "April 25, 2024",
             "cover": "jaydes - Lord.jpg",              # file name inside images/
	         "url": "https://soundcloud.com/jayden-archive/sets/lord",
             "tracks": [
                       "moodswings",
	                   "720p (prod. XanGang, jaydes)",
	                   "brandy melville (prod. dontscrewmeover)",
                       "coke!!! (prod. yuke)",
                       "ilovepeonsihatemyhoes (prod. jaydes)",
	                   "Last Burner!! It's A Shitter!!! (prod. jaydes)",
	                   "risk (prod. jaydes)",
                       "ritual (feat. yuke) (prod. jaydes)",
                       "why im blocked????????? (prod. jaydes)",
             ],
         },
         {
             "title": "ghetto cupid",
             "kind": "Album",          # Album / EP / Mixtape
             "year": "August 16, 2023",
             "cover": "jaydes - ghetto cupid.jpg",              # file name inside images/
	         "url": "https://music.youtube.com/playlist?list=OLAK5uy_kYZAg24jClXEydoBB9b6c5AGh7ngRizaI",
             "tracks": [
                       "rose (prod. grayskies, jaydes)",
	                   "anemic (prod. jaydes)",
	                   "let me b (prod. jaydes)",
                       "numb (prod. jaydes)",
                       "witchybitchy (prod. jaydes)",
	                   "damage (prod. jaydes)",
	                   "<3 (prod. Jewxlry, srrybouturshoes)",
                       "undercover (prod. jaydes)",
                       "dead girl (prod. jaydes)",
                       "fallen (prod. marcusbasquiat)",
                       "valentine (prod. jaydes)",
                       "misery (prod. Ric Ocasek)",
                       "spaz (prod. jaydes)",
                       "kesha k (prod. BossUp)",
                       "laylow (prod. kiltmymood)",
                       "horror (prod. jaydes)",
                       "draculea (prod. KRXXK)",
             ],
         },
         
     ],
     "singles": [
         {
             "title": "Jug (prod. Keyblade)",
             "year": "November 26, 2020",
             "cover": "jaydes - Jug.jpg",
             "url": "https://soundcloud.com/1zue/jaydes-jug-prod-keyblade",
         },
         {
             "title": "paypal (prod. glumboy)",
             "year": "February 27, 2021",
             "cover": "jaydes - paypal.jpg",
             "url": "https://soundcloud.com/jaydes/paypal",
         },
         {
             "title": "highschool (prod. LUNA, glumboy)",
             "year": "March 13, 2021",
             "cover": "jaydes - highschool.jpg",
             "url": "https://soundcloud.com/jaydes/highschool",
         },
         {
             "title": "staymadpussy (prod. MexikoDro)",
             "year": "April 1, 2021",
             "cover": "jaydes - staymadpussy.jpg",
             "url": "https://soundcloud.com/1zue/jaydes-staymadpussy-prod",
         },
         {
             "title": "27 (feat. Riovaz) (prod. CG)",
             "year": "December 18, 2020",
             "cover": "jaydes - 27.jpg",
             "url": "https://soundcloud.com/jaydes/27a1",
         },
         {
             "title": "offensive (prod. 800pts)",
             "year": "May 30, 2021",
             "cover": "jaydes - offensive.jpg",
             "url": "https://soundcloud.com/jaydes/offensive",
         },
         {
             "title": "do 2 much (prod. 800pts, jaydes)",
             "year": "June 11, 2021",
             "cover": "jaydes - do 2 much.jpg",
             "url": "https://soundcloud.com/jaydes/do-2-much",
         },
         {
             "title": "trust issues (prod. jaydes, Kayy Luciano)",
             "year": "June 27, 2021",
             "cover": "jaydes - trust issues.jpg",
             "url": "https://soundcloud.com/jaydes/trust-issues",
         },
         {
             "title": "wya? (prod. 800pts)",
             "year": "August 7, 2021",
             "cover": "jaydes - wya.jpg",
             "url": "https://soundcloud.com/jaydes/wya",
         },
         {
             "title": "melatonin (feat. Yung Fazo) (prod. LUNA)",
             "year": "September 5, 2021",
             "cover": "jaydes - melatonin.jpg",
             "url": "https://soundcloud.com/jaydes/melatonin",
         },
         {
             "title": "clueless (prod. Spookjamie)",
             "year": "October 7, 2021",
             "cover": "jaydes - clueless.jpg",
             "url": "https://soundcloud.com/jaydes/clueless",
         },
         {
             "title": "vivienne (prod. Silo)",
             "year": "November 6, 2021",
             "cover": "jaydes - vivienne.jpg",
             "url": "https://soundcloud.com/jaydes/vivienne",
             "music_video": "https://www.youtube.com/watch?v=FOzdrE4qkH0",
         },
         {
             "title": "slugs (prod. XanGang)",
             "year": "March 16, 2022",
             "cover": "jaydes - slugs.jpg",
             "url": "https://soundcloud.com/jaydes/slugs",
             "music_video": "https://www.youtube.com/watch?v=TMxJxGBb8gw",
         },
         {
             "title": "Shoulda Been There (feat. LEVON) (prod. Milanezie, Silo)",
             "year": "June 3, 2022",
             "cover": "jaydes - Shoulda Been There.jpg",
             "url": "https://soundcloud.com/jaydesarchive-music/shoulda-been-there",
         },
         {
             "title": "paranoia (prod. jaydes, zhou)",
             "year": "June 24, 2022",
             "cover": "jaydes - paranoia.jpg",
             "url": "https://soundcloud.com/jaydes/paranoia",
         },
         {
             "title": "south (prod. jaydes, ohissmcqueen, Hazardd)",
             "year": "September 21, 2022",
             "cover": "jaydes - south.jpg",
             "url": "https://soundcloud.com/jaydes/south",
         },
         {
             "title": "poison (prod. C Medina)",
             "year": "December 10, 2022",
             "cover": "jaydes - Jug.jpg",
             "url": "https://soundcloud.com/jaydes/poison",
             "music_video": "https://www.youtube.com/watch?v=MgKebqcV8o4",
         },
         {
             "title": "fendi (feat. hapes) (prod. jaydes)",
             "year": "February 27, 2024",
             "cover": "jaydes - fendi.jpg",
             "url": "https://soundcloud.com/hapes_sc/fendi-wjaydes",
         },
         
     ],
 },
 {
     "name": "prettifun",
     "image": "prettifun.gif",                      # file name inside images/
     "aliases": ["mikey"],                    # ["Other Name", "Old Tag"]
     "dob": "August 1, 2005",                        # "1996-03-04" or "March 4, 1996"
     "links": {
         "spotify": "https://open.spotify.com/artist/3J3ngZn7GjzjwCPBkqtz65",
         "youtube_music": "https://music.youtube.com/@prettifun",
         "soundcloud": "https://soundcloud.com/prettifun",
     },
     "projects": [
         {
             "title": "most wonderful time of year",
             "kind": "EP",          # Album / EP / Mixtape
             "year": "January 25, 2023",
             "cover": "prettifun - most wonderful time of the year.jpg",              # file name inside images/
	         "url": "https://music.youtube.com/playlist?list=OLAK5uy_my5Cnm9W9TL_kVvEUT_B7gNgnet9_fK_s",
             "tracks": [
                       "intro (prod. Iankon)",
	                   "low funds (prod. Iankon)",
	                   "everystep (prod. prettifun, Iankon)",
                       "might/poltergeist (prod. Iankon)",
                       "bribe (prod. Iankon)",
	                   "lmao (prod. Iankon)",
             ],
         },
         {
             "title": "Mr.TenFigs",
             "kind": "EP",          # Album / EP / Mixtape
             "year": "August 9, 2023",
             "cover": "prettifun - Mr.TenFigs.jpg",              # file name inside images/
	         "url": "https://music.youtube.com/playlist?list=OLAK5uy_mmU5T-o80aGjB7rKlU9aB_9e1x5msg8tA",
             "tracks": [
                       "Mr.TenFigs (prod. prettifun)",
	                   "Sleep Aid (prod. prettifun)",
	                   "Lie Too (prod. prettifun)",
                       "New Deal (prod. prettifun)",
                       "We Good (prod. Condo, Cade)",
	                   "Team Rocket (prod. Hitec)",
             ],
         },
         {
             "title": "Hi-Fi 0.5",
             "kind": "EP",          # Album / EP / Mixtape
             "year": "September 15, 2023",
             "cover": "prettifun - Hi-Fi 0.5.jpg",              # file name inside images/
	         "url": "https://music.youtube.com/playlist?list=OLAK5uy_lleU9jAbXwQ--amcx01KDfR5qkWFdoT-8",
             "tracks": [
                       "Lottery (prod. Hitec)",
	                   "Teezo Touchdown (prod. Hitec)",
	                   "Maybelline (prod. Hitec)",
                       "Lol xD (prod. Hitec)",
             ],
         },
         
         {
             "title": "Hi-Fi",
             "kind": "Album",          # Album / EP / Mixtape
             "year": "September 29, 2023",
             "cover": "prettifun - Hi-Fi.jpg",              # file name inside images/
             "url": "https://music.youtube.com/playlist?list=OLAK5uy_lcXYvwijSo-QHaxLPkSph7p5RZQEDKloM",
             "tracks": [
                       "That Way (prod. Hitec)",
	                   "Maybelline (prod. Hitec)",
	                   "Anxiety (prod. Hitec)",
                       "Cyberpunk 2077 (prod. Hitec, greedmp3)",
                       "Teezo Touchdown (prod. Hitec)",
	                   "3 Min Freestyle (prod. Hitec)",
	                   "At The Door (prod. Hitec)",
                       "Lol xD (prod. Hitec)",
                       "Jackie Chan (prod. Hitec)",
                       "Hocus Pocus (prod. Hitec)",
                       "Dc (prod. Hitec)",
                       "Pop Quiz (prod. Hitec)",
                       "Fuck The Industry (prod. Hitec)",
                       "Lottery (prod. Hitec)",
                       "Changing (prod. Hitec)",
                       "Alistair Overeem (prod. Hitec)",
                       "Used To (prod. Hitec)",
                       "Pretti (prod. Hitec)",
             ],
         },
         {
             "title": "Pretti",
             "kind": "Album",          # Album / EP / Mixtape
             "year": "August 1, 2024",
             "cover": "prettifun - Pretti.jpg",              # file name inside images/
             "url": "https://music.youtube.com/playlist?list=OLAK5uy_n1JkAGAjZ57k0hXfgy32xvzDe_H753ARE",
             "tracks": [
                       "Rita (prod. prettifun)",
	                   "Touch The Sun (prod. prettifun)",
	                   "Good Influence (prod. prettifun)",
                       "Sos (prod. prettifun)",
                       "Ice Cream (prod. prettifun)",
	                   "Honeybun (prod. egobreak)",
	                   "#FreePretti (prod. Jdolla, Praisedommy)",
                       "Light (prod. prettifun)",
                       "Wings (prod. prettifun)",
                       "Sparky (feat. Cayo) (prod. prettifun)",
                       "Money Hungry (prod. 9lives)",
                       "Type Beat (prod. prettifun)",
                       "Jump (prod. J0se)",
                       "Moon (prod. prettifun)",
                       "Maybe (prod. kailer)",
             ],
         },
         {
             "title": "FunHouse",
             "kind": "Album",          # Album / EP / Mixtape
             "year": "September 30, 2024",
             "cover": "prettifun - FunHouse.jpg",              # file name inside images/
             "url": "https://music.youtube.com/playlist?list=OLAK5uy_ng3obmAogJ9rvvA1scLYPOd_1M8Q-XFlk",
             "tracks": [
                       "Dead First (prod. Ginseng, MISOGI, grassarrows)",
	                   "Z&S (prod. Ginseng, ryanjacob)",
	                   "Feel Like Uzi (prod. MaxFlames, ssort)",
                       "Rolled1 (prod. Ginseng, MISOGI, legion)",
                       "Gaultier Bag (prod. gyro)",
	                   "Bbyangl (prod. Ginseng)",
	                   "Killem (prod. Ginseng, Jay Trench, legion)",
                       "Fedswatchin (prod. gyro)",
                       "Move Smartr (prod. Ginseng, MISOGI, ryanjacob, grassarrows)",
                       "Prttigirl (prod. MISOGI, love&peace)",
                       "Highly Favoured (prod. Iankon)",
                       "Quarters Pennies (prod. Iankon)",
                       "Head Strong (prod. Ginseng, MISOGI, Jay Trench, LUNEGAZE)",
                       "Meds (prod. legion)",
                       "Thank U (prod. Ginseng, MISOGI, legion, love&peace)",
                       "Achive It (prod. Lucid)",
                       "Miss U Angie (prod. Lucid, o0o)",
                       "I Don't Sleep (prod. legion)",
             ],
         },
         {
             "title": "FunHouse Deluxe",
             "kind": "Deluxe",          # Album / EP / Mixtape
             "year": "August 1, 2025",
             "cover": "prettifun - FunHouse Deluxe.jpg",              # file name inside images/
	         "url": "https://music.youtube.com/playlist?list=OLAK5uy_lTEd9SnFti7S0znRlntb4bUKh6AsIrLSE",
             "tracks": [
                       "My Name (prod. MISOGI, Outtatown)",
	                   "Kisses (prod. Jdolla)",
	                   "Fuck w Ya (prod. Ginseng, Jay Trench)",
                       "Famous (prod. Jay Trench)",
                       "Digital Love (prod. Iankon)",
	                   "Last Wish (prod. Iankon)",
	                   "Sides (prod. Jay Trench, SILENTHEAVEN)",
                       "Heartbreaker (prod. MISOGI, Outtatown)",
                       "Unfazed (prod. Ginseng)",
                       "Different (prod. Ginseng, Jay Trench, MISOGI, love&peace)",
                       "Internet (prod. Ginseng, Lucid)",
                       "Back (prod. Jay Trench)",
                       "idk wtf (prod. Ginseng)",
                       "Infinity (prod. Hitec)",
                       "Hi-Fi 2026 (prod. Hitec)",
             ],
         },
         {
             "title": "Pretti Loves U 2",
             "kind": "Album",          # Album / EP / Mixtape
             "year": "August 21, 2026",
             "cover": "prettifun - Pretti Loves U 2.jpg",              # file name inside images/
	         "url": "https://music.youtube.com/playlist?list=OLAK5uy_mu3S0uS0dPxR1ocRf_0lOTfDPc_b5THA4",
             "tracks": [
                       "Rollacoasta (prod. prettifun)",
	                   "Scene (prod. prettifun)",
	                   "Steps (prod. prettifun)",
                       "Deposit (prod. prettifun)",
                       "Just Me (prod. prettifun)",
	                   "Nobody (prod. prettifun)",
	                   "Moon and the Stars (prod. prettifun)",
                       "All Knowing (prod. prettifun)",
                       "Room (prod. prettifun)",
                       "Wtf idk (prod. prettifun)",
                       "UI (prod. prettifun)",
                       "All Love! (prod. prettifun)",
             ],
         },
         
     ],
     "singles": [
         {
             "title": "dream (prod. prettifun)",
             "year": "April 3, 2022",
             "cover": "prettifun - dream.jpg",
             "url": "https://soundcloud.com/prettifun/dream",
         },
         {
             "title": "kelp",
             "year": "April 7, 2022",
             "cover": "prettifun - kelp.jpg",
             "url": "https://soundcloud.com/prettifun/kelp",
         },
         {
             "title": "evisu",
             "year": "July 15, 2022",
             "cover": "prettifun - evisu.jpg",
             "url": "https://soundcloud.com/prettifun/evisu",
         },
         {
             "title": "Jackie Chan (prod. Hitec)",
             "year": "September 6, 2023",
             "cover": "prettifun - Jackie Chan.jpg",
             "url": "https://soundcloud.com/prettifun/jackie-chan-prod-hitec",
         },
         {
             "title": "Savior (prod. Hitec, Wvstend)",
             "year": "July 1, 2024",
             "cover": "prettifun - Savior.jpg",
             "url": "https://soundcloud.com/prettifun/savior-prod-hitec-wvstend",
         },
         {
             "title": "Ice Cream (prod. prettifun)",
             "year": "July 10, 2024",
             "cover": "prettifun - Ice Cream.jpg",
             "url": "https://soundcloud.com/prettifun/marcel-zago",
             "music_video": "https://www.youtube.com/watch?v=5jMvpFzukSk",
         },
         {
             "title": "idk wtf (prod. Ginseng)",
             "year": "January 30, 2025",
             "cover": "prettifun - idk wtf.jpg",
             "url": "https://soundcloud.com/prettifun/idk-wtf",
         },
         {
             "title": "Famous (prod. Jay Trench)",
             "year": "June 20, 2025",
             "cover": "prettifun - Famous.jpg",
             "url": "https://soundcloud.com/prettifun/famous",
         },
         {
             "title": "Unfazed (prod. Ginseng)",
             "year": "July 18, 2025",
             "cover": "prettifun - Unfazed.jpg",
             "url": "https://soundcloud.com/prettifun/unfazed",
             "music_video": "https://www.youtube.com/watch?v=RBKF3yjmWp8",
         },
         {
             "title": "Digital Love (prod. iankon)",
             "year": "July 25, 2025",
             "cover": "prettifun - Digital Love.jpg",
             "url": "https://soundcloud.com/prettifun/digital-love",
         },
         {
             "title": "YCDL (prod. legion, MISOGI, Outtatown)",
             "year": "November 28, 2025",
             "cover": "prettifun - YCDL.jpg",
             "url": "https://soundcloud.com/prettifun/ycdl",
         },
         {
             "title": "Workout (prod. legion, MISOGI, Outtatown)",
             "year": "December 19, 2025",
             "cover": "prettifun - Workout.jpg",
             "url": "https://soundcloud.com/prettifun/workout",
         },
         {
             "title": "Moon and the Stars (prod. prettifun)",
             "year": "May 12, 2026",
             "cover": "prettifun - Moon and the Stars.jpg",
             "url": "https://soundcloud.com/prettifun/moon-and-the-stars",
         },
         {
             "title": "Nobody (prod. prettifun)",
             "year": "June 16, 2026",
             "cover": "prettifun - Nobody.jpg",
             "url": "https://soundcloud.com/prettifun/nobody",
         },
         {
             "title": "Scene (prod. prettifun)",
             "year": "August 14, 2026",
             "cover": "prettifun - Scene.jpg",
             "url": "https://soundcloud.com/prettifun/scene",
         },
         ],
 },        
 {
     "name": "Summrs",
     "image": "summrs.gif",                      # file name inside images/
     "aliases": ["Summrino", "Summrs Archive", "Summr", "Louiveedee", "SummrBangz", "Lil Rino", "SummrsXO", "Lil Summrs", "Summrs International", "SummrsY"],                    # ["Other Name", "Old Tag"]
     "dob": "November 18, 1999",                        # "1996-03-04" or "March 4, 1996"
     "links": {
         "spotify": "https://open.spotify.com/artist/5L15t6I0PQS9SBXbiklPEN",
         "youtube_music": "https://music.youtube.com/@summrs7786",
         "soundcloud": "https://soundcloud.com/summrs",
     },
     "projects": [
         {
             "title": "DEVOTION",
             "kind": "Mixtape",          # Album / EP / Mixtape
             "year": "August 17, 2018",
             "cover": "Summrs - DEVOTION.jpg",              # file name inside images/
	         "url": "https://music.youtube.com/playlist?list=OLAK5uy_lyzidbGOfS2ZwoZ6VmNYPAXjoKySABcUM",
             "tracks": [
                       "Translucent (prod. Goyxrd)",
	                   "loner (prod. CashBently)",
	                   "Come Here (prod. Goyxrd)",
                       "Devotion Interlude Intro (prod. Goyxrd)",
                       "So Fr.. (prod. AltoSGP)",
	                   "Throug It All (prod. Thrillboy)",
	                   "Set It Off (prod. Lukovic, TrapboyTango)",
                       "Warzone (prod. Styn, Lukovic)",
                       "When You Fucked Up (prod. Thrillboy)",
                       "Golden (prod. XanGang)",
                       "We Got a Thang (prod. Goyxrd)",
                       "Choose (prod. Goyxrd, Kankan)",
                       "Gambling (prod. XanGang)",
                       "Cannot Be Me (prod. DiorDaze)",
                       "007 (prod. Ginseng)",
                       "Til I Diee (prod. XanGang)",
                       "The Wait (prod. Yung Star, XanGang, Slxyy)",
                     
             ],
         },
         {
             "title": "Revived",
             "kind": "Mixtape",          # Album / EP / Mixtape
             "year": "November 19, 2018",
             "cover": "Summrs - Revived.jpg",              # file name inside images/
	         "url": "https://music.youtube.com/playlist?list=OLAK5uy_kF-lHEB4Oh3vQZTOK-BbBzSfvUdqQIplk",
             "tracks": [
                       "Blurry (prod. AltoSGP)",
	                   "Cathedral (prod. XanGang)",
	                   "Coach (prod. Thrillboy)",
                       "Da Boss (prod. Goyxrd)",
                       "Blew It (prod. AltoSGP)",
	                   "2Late (prod. Thrillboy)",
	                   "Die Out (prod. Thrillboy)",
                       "Element (prod. Goyxrd, Neimxn)",
                       "Hope Your Happy (prod. Lovxrboi, GOONIE)",
                       "Globe (prod. Goyxrd)",
                       "French Toast (prod. XanGang)",
                       "Listen (prod. Goyxrd)",
                       "Show N Tell (prod. Yuntec)",
                       "Unforgettable (prod. Goyxrd)",
                       "See Me (prod. Thrillboy)",
             ],
         },
         {
             "title": "Isolation",
             "kind": "Album",          # Album / EP / Mixtape
             "year": "October 15, 2019",
             "cover": "Summrs - Isolation.jpg",              # file name inside images/
	         "url": "https://music.youtube.com/playlist?list=OLAK5uy_lFmAQGHeryMYqtcfaRG_X95Zkr3TjiME4",
             "tracks": [
                       "Go Bestie (feat. Autumn!) (prod. Eddie Gianni)",
	                   "Downfall (prod. CodyLemont, Dior Blunt)",
	                   "living a 2nd life (prod. CashBently)",
                       "test sum (prod. Eddie Gianni)",
                       "Greenlight (prod. XanGang)",
	                   "Dont Fold (prod. Thrillboy)",
	                   "Me (prod. Eddie Gianni)",
                       "#SlayParty (prod. healthykid, Dior Blunt)",
                       "Party Bitches (prod. CodyLemont, Dior Blunt)",
                       "Horses (prod. Skys)",
                       "“time Lost” A Interlude by Rino (prod. Dior Blunt, Summrs)",
                       "Cocaine/mollyinterlude (feat. Autumn!) (prod. Skys, Summrs)",
                       "The Vision (prod. Oscar100)",
                       "Ya Style (prod. BenjiCold, Thrillboy)",
                       "Tonight (prod. Max2Buck, Dior Blunt)",
             ],
         },
         {
             "title": "Intoxicated",
             "kind": "Album",          # Album / EP / Mixtape
             "year": "March 13, 2021",
             "cover": "Summrs - Intoxicated.jpg",              # file name inside images/
	         "url": "https://music.youtube.com/browse/MPADUCtMA4JKpNZyvlOlZvovv_aA",
             "tracks": [
                       "Went Mia (prod. Dior Blunt, DiorDaze)",
	                   "Heart Of The Moment (feat. TyFontaine) (prod. Dior Blunt, CodyLemont)",
	                   "Know You Gone Switch (prod. Dior Blunt)",
                       "Z06 (prod. Iankon)",
                       "Tryna Show You (prod. CGM Beats, Wonderr)",
	                   "Back In Orlando (prod. Dior Blunt)",
	                   "Won't Last (prod. healthykid, ninetyniiine)",
                       "The Sideline (prod. Dior Blunt)",
                       "Take Control (feat. Autumn!) (prod. ninetyniiine)",
                       "For The Streets Interlude (prod. qpid, Dior Blunt)",
                       "Truth Is (prod. Kankan)",
                       "Love Me (prod. Bizness Boi)",
                       "For Someone Else (feat. TyFontaine) (prod. Iankon)",
             ],
         },
         {
             "title": "Nothing more Nothing LESS",
             "kind": "Album",          # Album / EP / Mixtape
             "year": "September 26, 2021",
             "cover": "Summrs - Nothing more Nothing LESS.jpg",              # file name inside images/
	         "url": "https://music.youtube.com/playlist?list=OLAK5uy_klhhDQ2kYA7Oz4dEkR67TtXis9RGEL28Y",
             "tracks": [
                       "nmnl (Intro) (prod. Goyxrd)",
	                   "Never Ever (prod. Goyxrd)",
	                   "Like a Band (prod. 30nickk)",
                       "In the Name of You (prod. Goyxrd)",
                       "From da Heart (prod. Goyxrd)",
	                   "Bloods Always Thicker (prod. Goyxrd)",
	                   "Cant make this Up (prod. Goyxrd)",
                       "Da MVP (prod. Autumn!)",
                       "First 48 (prod. Autumn!)",
                       "Back 2 Da Basics (prod. Autumn!)",
                       "Im Ready (prod. Autumn!)",
                       "Where we left off (prod. XanGang, Goyxrd)",
                       "The Outro (prod. XanGang, Summrs)",
             ],
         },
         {
             "title": "FALLEN RAVEN",
             "kind": "Album",          # Album / EP / Mixtape
             "year": "June 27, 2022",
             "cover": "Summrs - FALLEN RAVEN.jpg",              # file name inside images/
	         "url": "https://music.youtube.com/playlist?list=OLAK5uy_lmrAwLIn-mM--1oJJO7jrmh4nhXMxpgk0",
             "tracks": [
                       "Let da bird out (prod. Hurtboy AG, Oscar4400xy, Jaxx, Mat1k)",
	                   "Wakeup (prod. Bhristo, lunar)",
	                   "So Much Cheese (prod. Prod Pink, bart how, Hudson Major)",
                       "Catch a Kill (prod. Hudson Major)",
                       "FadaPhillipe (prod. Bhristo, GeoGotBands, Hurtboy AG)",
	                   "Twin did dat (prod. Hurtboy AG, GeoGotBands, Charger)",
	                   "Swing Ya Pole (prod. Venexxi, Mingo, Paulo)",
                       "Clear Da Bidness (prod. Hurtboy AG, GeoGotBands, Only1Shredder)",
                       "Calico From Mehico (prod. GeoGotBands, WhoIsRiqo)",
                       "Dont Mean Shit (prod. BenjiCold)",
                       "5:35 am Interlude (prod. Hurtboy AG, Clay Priskorn)",
                       "Vali, CO (prod. Bhristo)",
                       "For You Interlude (prod. Ben10k, Dirty Dave, Danes Blood)",
                       "Ashes (prod. Hurtboy AG, JB Sauced Up, BEATSAINTFREE JG, lvl35dav)",
                       "Cuts so Deep 2 (prod. Goyxrd)",
                       "FTW (prod. 30nickk)",
                       "Perfect Timing (prod. KxngRada, Goyxrd)",
                       "Soulja Rag (prod. 30nickk)",
                       "Bonnie & Klyde 2 (prod. Goyxrd)",
                       "NSA (prod. 30nickk, mista)",
                       "Dear Mom, (prod. 30nickk)",
                       "Loving u is a Sin (prod. Hurtboy AG, Nick Schmidt, BEATSAINTFREE JG)",
                       "Caused Envy. (prod. Bhristo, Txylordank, oktanner)",
             ],
         },
         {
             "title": "Stuck In My Ways",
             "kind": "Album",          # Album / EP / Mixtape
             "year": "January 27, 2023",
             "cover": "Summrs - Stuck In My Ways.jpg",              # file name inside images/
	         "url": "https://music.youtube.com/playlist?list=OLAK5uy_nFz9CqfxYkN1kmz7Xihvrlk47d_yYv0Ks",
             "tracks": [
                       "Relying On Roxy (prod. BenjiCold)",
	                   "Start Striking (prod. BenjiCold)",
	                   "No Days Off (prod. BenjiCold)",
                       "Life's A Beautiful Curse (prod. BenjiCold, ZeeGoinXrazy)",
                       "Pure Motion (feat. Desire) (prod. GeoGotBands)",
	                   "No Morals (prod. BrentRambo, Hitmula)",
	                   "Russian Roulette (prod. BrentRambo)",
                       "Die Rich (prod. dulio, GeoGotBands)",
                       "Van Cleef Poppin (prod. GeoGotBands, Hakah Beats)",
                       "Addy Geek (prod. qioh, Wisvoo, mixed matches)",
                       "The Detox (prod. Cheif Keef, DP Beats, Alijah4k, prodby7000)",
                       "Drug Traffickin (prod. BrentRambo, Venexxi)",
                       "Like A River (prod. VenoTheBuilder, Jason Goldberg)",
                       "My Voicemail (prod. Dior Blunt, ninetyniiine, Idontkry, IVSIRS)",
                       "Closing The Book (prod. Mingo)",
                       "Blood Tears (Interlude) (prod. Jason Goldberg, Bak, BEATSAINTFREE JG, Hurtboy AG)",
                       "Miles On U (prod. Idontkry)",
                       "Album Just For You (prod. Summrs, Autumn!)",
                       "IKYMMG (prod. Goyxrd)",
                       "Pilates (prod. Goyxrd)",
                       "Like My Diamonds (prod. BenjiCold)",
                       "Baby Blue Gwag (prod. Summrs, Autumn!)",
                       "Switch Sound (prod. AltoSGP)",
                       "Praise Da Most High (prod. AltoSGP, 1saksss)",
                       "Stuck In My Ways (prod. Ben10k, Joe Reeves, Jason Goldberg)",
             ],
         },
         {
             "title": "GHOST",
             "kind": "Album",          # Album / EP / Mixtape
             "year": "April 28, 2023",
             "cover": "Summrs - GHOST.jpg",              # file name inside images/
	         "url": "https://music.youtube.com/playlist?list=OLAK5uy_mLhITpdP6T5I6PmjmksAYb4fIjKsgy-No",
             "tracks": [
                       "Devil On My Back (prod. Swishrr)",
	                   "Like Woah (prod. BNYX, martyr, oliimpus)",
	                   "Shake It (prod. BNYX, Sebastian Shah)",
                       "Eye 4 Eye (prod. dulio, Okami)",
                       "Rich N Turnt (feat. Desire) (prod. CHASETHEMONEY, noanalu)",
	                   "Real Goat (prod. Finn Tudor, M15)",
	                   "Prayer (prod. BNYX, Karl Rubin, DJ Replay)",
                       "No Really (prod. CHASETHEMONEY, noanalu)",
                       "Ball 4 Ball (prod. Finn Tudor, M15)",
                       "Got Dat Muneh (prod. GeoGotBands, Hakah Beats)",
                       "Free Body (prod. dulio, Oj2milly)",
                       "Like BK (prod. dulio, Oj2milly)",
                       "I'm Paid (prod. M15, Finn Tudor)",
                       "NVR Losing (prod. Lucid)",
                       "God Like (prod. BNYX, Jasford)",
                       "Goty (prod. dulio, M15)",
                       "Meet You There (prod. Finn Tudor, M15)",
                       "Munchkin (prod. CHASETHEMONEY, noanalu)",
                       "Snowflow (prod. dulio, Lucid)",
                       "It Get Krazy (prod. dulio, M15)",
                       "RIP Virgil (prod. Finn Tudor, M15)",
             ],
         },
         {
             "title": "What We Didn't Have",
             "kind": "Album",          # Album / EP / Mixtape
             "year": "September 18, 2023",
             "cover": "Summrs - What We Didn't Have.jpg",              # file name inside images/
	         "url": "https://music.youtube.com/playlist?list=OLAK5uy_mGxYdUnXG3SZL1CmzwGoYHimmu1EvFTrU",
             "tracks": [
                       "Overdosing On Toxicity (prod. XanGang)",
	                   "The Healing (prod. XanGang)",
	                   "Rehab (prod. Goyxrd, XanGang)",
                       "Feel Dumb (prod. Thrillboy, Goyxrd)",
                       "International (prod. Goyxrd)",
	                   "Playin With Demon / Jokes On U (prod. XanGang, Summrs, ucondrew, Goyxrd)",
	                   "The Talk (prod. Goyxrd, AxJunior)",
                       "Xanax / Burnt Memories (prod. XanGang)",
                       "Til Death Do Us Part (prod. XanGang)",
                       "If Ya Wanted 2 Know (prod. AxJunior, Galaxxy4r)",
                       "Top Off / House Arrest (prod. Goyxrd, AxJunior, Alijah4k)",
                       "Auntie Cat / How Dare You (prod. AltoSGP, XanGang)",
                       "Martin & Gina (feat. Autumn!) (prod. Oliver Easton, Julian Currier)",
                       "Chasing Ur High (feat. Desire) (prod. Goyxrd)",
                       "It's Nothing / Spiritual Outro (prod. XanGang, Telxry)",
             ],
         },
         {
             "title": "B4DARAVEN",
             "kind": "Album",          # Album / EP / Mixtape
             "year": "April 12, 2024",
             "cover": "Summrs - B4DARAVEN.jpg",              # file name inside images/
	         "url": "https://music.youtube.com/playlist?list=OLAK5uy_mcnFaqRE86nV9oGcvL03vU_jc9_SY6og4",
             "tracks": [
                       "Curbside at The Ritz (prod. KxngRada, ucondrew)",
	                   "Made man (prod. Prod. YONKO, ucondrew)",
	                   "Situationships (prod. Goyxrd)",
                       "Sneaky link/Love that 4 us (prod. XanGang, ucondrew, Prod. YONKO)",
                       "Drank n sex (prod. KxngRada, Skoozi)",
	                   "In our favor (prod. Prod. YONKO)",
	                   "Brioni shawl collar/Catfish (prod. XanGang, Alijah4k, KxngRada, TorenoMade)",
             ],
         },
         {
             "title": "Wick & Clancy: 2S3 Vol. 1",
             "kind": "EP",          # Album / EP / Mixtape
             "year": "August 26, 2019",
             "cover": "Summrs - Wick & Clancy.jpg",              # file name inside images/
	         "url": "https://music.youtube.com/playlist?list=OLAK5uy_k4K6F6MKUxJif0q_TRWhU4CyECCDdA_N0",
             "collab": "Autumn!",
             "tracks": [
                       "No Hope! (prod. BrentRambo)",
	                   "What You Did! (prod. BrentRambo, Summrs)",
	                   "2 Fed! (prod. Skys)",
                       "Bins No Good! (prod. 5heriff)",
             ],
         },
         {
             "title": "What We Have",
             "kind": "EP",          # Album / EP / Mixtape
             "year": "June 13, 2021",
             "cover": "Summrs - What We Have.jpg",              # file name inside images/
	         "url": "https://music.youtube.com/playlist?list=OLAK5uy_m31nqEMvxKfp5hlk44iDH3pV8B_8XEttA",
             "tracks": [
                       "what we have (prod. Goyxrd)",
	                   "put out fye (prod. Goyxrd)",
	                   "out da window (prod. Goyxrd)",
                       "just cant (prod. Autumn!)",
                       "bfo2 (prod. 30nickk)",
	                   "cut so deep (prod. Telxry)",
             ],
         },
         {
             "title": "NIGHTFALL",
             "kind": "EP",          # Album / EP / Mixtape
             "year": "August 2, 2024",
             "cover": "Summrs - NIGHTFALL.jpg",              # file name inside images/
	         "url": "https://music.youtube.com/playlist?list=OLAK5uy_m30mAiYnFfo4bAbEmtCKT32yQvTXwe1HM",
             "tracks": [
                       "Bentley Mulsanne (prod. ucondrew, KxngRada)",
	                   "FWWYN (prod. Swishrr)",
	                   "Phantom Muzik (prod. Mousha, noanalu)",
                       "F.O.B (prod. Synthetic, Venny, Yateski, talk2primo)",
                       "Marble Floors (prod. Swishrr, XanGang)",
	                   "Nightfall Outro (prod. Rafe, sharkboy, Bred, Synthetic, Cloak)",
             ],
         },
         

     ],
     "singles": [
         {
             "title": "Deserve It (feat. SupremeLouie) (prod. zJakkies)",
             "year": "January 8, 2018",
             "cover": "Summrs - Deserve It.jpg",
             "url": "https://soundcloud.com/xyzwl/summrs-deserve-it-prod-zjakkies",
         },
         {
             "title": "Cold Outside! (prod. CashBently)",
             "year": "April 12, 2018",
             "cover": "Summrs - Cold Outside.jpg",
             "url": "https://soundcloud.com/ntrsummrs/summrs-cold-outside-3-prod",
         },
         {
             "title": "Texas tea (prod. CashBently)",
             "year": "April 26, 2018",
             "cover": "Summrs - Texas tea.jpg",
             "url": "https://soundcloud.com/autumarwick/summrs-texas-tea",
         },
         {
             "title": "Tor Browser (prod. Leesta)",
             "year": "January 25, 2019",
             "cover": "Summrs - Tor Browser.jpg",
             "url": "https://soundcloud.com/summrs/we-have-your-ip-prod-leesta",
         },
         {
             "title": "Zone! (prod. Jakemills)",
             "year": "January 29, 2019",
             "cover": "Summrs - Zone!.jpg",
             "url": "https://soundcloud.com/jakemillsbeats/summrsxosummr-zone-prod-jakemills",
         },
         {
             "title": "get em gone (prod. Leesta)",
             "year": "February 13, 2019",
             "cover": "Summrs - get em gone.jpg",
             "url": "https://soundcloud.com/summrs/get-em-gone-prod-leesta",
         },
         {
             "title": "vicodines (prod. BrentRambo)",
             "year": "July 14, 2019",
             "cover": "Summrs - vicodines.jpg",
             "url": "https://soundcloud.com/summrs/vicodines-prod-noirbrent",
         },
         {
             "title": "Cliche (feat. Autumn!) (prod. Mike Frost, LuvNiko)",
             "year": "November 25, 2019",
             "cover": "Summrs - Cliche.jpg",
             "url": "https://soundcloud.com/luvniko/autumn-summrs-cliche-prod-mike-frost-x-luvniko",
         },
         {
             "title": "Cut The Act (prod. Sayuh, Slayer / slayedthis)",
             "year": "April 8, 2020",
             "cover": "Summrs - Cut The Act.jpg",
             "url": "https://soundcloud.com/boofpakk/1i4r5m48a8x8128",
         },
         {
             "title": "MOTHER of MY Kids (feat. TyFontaine) (prod. Slayer / slayedthis)",
             "year": "January 6, 2021",
             "cover": "Summrs - MOTHER of MY Kids.jpg",
             "url": "https://soundcloud.com/1800tyfontaine/mother-of-my-kids-prod-slayer",
         },
         {
             "title": "Im Rich (prod. sadbalmain, pinkgrillz)",
             "year": "March 30, 2022",
             "cover": "Summrs - Im Rich.jpg",
             "url": "https://soundcloud.com/summrs/im-rich-prod-sadbalmain",
         },
         {
             "title": "bird allegiance (prod. Goyxrd)",
             "year": "April 2, 2022",
             "cover": "Summrs - bird allegiance.jpg",
             "url": "https://soundcloud.com/summrs/bird-allegiance-prod-goyxrd",
         },
         {
             "title": "Trials & Tribulations (prod. BenjiCold)",
             "year": "February 19, 2021",
             "cover": "Summrs - trials and tribulations.jpg",
             "url": "https://soundcloud.com/summrs/trials-tribulations-prod",
         },
         {
             "title": "Bird Business (feat. Lamont Galore) (prod. AxJunior)",
             "year": "June 16, 2022",
             "cover": "Summrs - Bird Business.jpg",
             "url": "https://soundcloud.com/swizik1/summrs-bird-business-prod-axjunior",
         },
         {
             "title": "No Really (prod. CHASETHEMONEY, noanalu)",
             "year": "April 24, 2023",
             "cover": "Summrs - GHOST.jpg",
             "url": "https://soundcloud.com/summrs/no-really-1",
         },
         {
             "title": "free sosa (prod. Telxry)",
             "year": "May 18, 2023",
             "cover": "Summrs - free sosa.jpg",
             "url": "https://soundcloud.com/summrs/free-sosa-prod-telxry",
         },
         {
             "title": "Free Do / Can't Do It (prod. Goyxrd, Kat Lightning, egobreak)",
             "year": "April 29, 2023",
             "cover": "Summrs - Free Do.jpg",
             "url": "https://soundcloud.com/summrs/free-do-cant-do-it-prod-goyxrd",
         },
         {
             "title": "Swk (RIP KAINE) (prod. XanGang)",
             "year": "November 4, 2023",
             "cover": "Summrs - Swk.jpg",
             "url": "https://soundcloud.com/stalkings/swk",
         },
         {
             "title": "Check Me Out (prod. Chico Made It)",
             "year": "November 16, 2023",
             "cover": "Summrs - Check Me Out.jpg",
             "url": "https://soundcloud.com/asher-484095260/summrs-check-me-out-homixide-gang-diss",
         },
         {
             "title": "I BEN (prod. Swishrr)",
             "year": "January 22, 2024",
             "cover": "Summrs - I BEN.jpg",
             "url": "https://soundcloud.com/summrs/i-ben",
         },
         {
             "title": "IKDR (prod. ucondrew, KxngRada)",
             "year": "March 8, 2024",
             "cover": "Summrs - Summrs Ikdr.jpg",
             "url": "https://soundcloud.com/summrs/ikdr",
         },
         {
             "title": "all i got (prod. Goyxrd)",
             "year": "March 13, 2024",
             "cover": "Summrs - all i got.jpg",
             "url": "https://soundcloud.com/summrs/all-i-got-prod-goyxrd",
         },
         {
             "title": "nobody knows (prod. TayTayMadeIt)",
             "year": "June 16, 2024",
             "cover": "Summrs - nobody knows.jpg",
             "url": "https://soundcloud.com/summrs/nobody-knows",
         },
         {
             "title": "Pop out (prod. Synthetic, sharkboy, qioh)",
             "year": "July 13, 2024",
             "cover": "Summrs - Pop out.jpg",
             "url": "https://soundcloud.com/summrs/pop-out-prod-synthethic",
         },
         {
             "title": "Sick flow (prod. KxngRada)",
             "year": "July 14, 2024",
             "cover": "Summrs - Sick flow.jpg",
             "url": "https://soundcloud.com/summrs/sick-flow-prod-kxngrada",
         },
         {
             "title": "Marble Floors (prod. Swishrr, XanGang)",
             "year": "July 19, 2024",
             "cover": "Summrs - Marble Floors.jpg",
             "url": "https://soundcloud.com/summrs/marble-floors",
         },
         {
             "title": "You Mind? (prod. AltoSGP, XanGang, ucondrew, KxngRada)",
             "year": "September 26, 2024",
             "cover": "Summrs - You Mind.jpg",
             "url": "https://soundcloud.com/summrs/you-mind-prod-altosgp-xangang",
         },
         {
             "title": "Rino Hercules (feat. PlaqueBoyMax) (prod. Swishrr)",
             "year": "November 15, 2024",
             "cover": "Summrs - Rino Hercules.jpg",
             "url": "https://soundcloud.com/summrs/rino-hercules-prod-swish",
         },
         {
             "title": "Late Night (prod. xbrvdy, pouritupsoda, Rafe)",
             "year": "May 23, 2025",
             "cover": "Summrs - Late Night.jpg",
             "url": "https://soundcloud.com/summrs/late-night",
         },
         {
             "title": "BABYRINO (prod. pouritupsoda, curesdead, Gorskiyy, sxldner, Summrs)",
             "year": "July 4, 2025",
             "cover": "Summrs - BABYRINO.jpg",
             "url": "https://soundcloud.com/summrs/babyrino",
         },
         {
             "title": "WHEN I WANT (prod. pouritupsoda, tjriverss, fuckliquidz)",
             "year": "August 5, 2025",
             "cover": "Summrs - WHEN I WANT.jpg",
             "url": "https://soundcloud.com/summrs/when-i-want",
         },
         {
             "title": "WITH THE MAFIA (prod. T3rps, Yozy, Twrkimm)",
             "year": "October 17, 2025",
             "cover": "Summrs - WITH THE MAFIA.jpg",
             "url": "https://soundcloud.com/summrs/with-the-mafia",
         },
         {
             "title": "YESSA (prod. Summrs, Cai Burns, Jacksonwithheart)",
             "year": "January 23, 2026",
             "cover": "Summrs - YESSA.jpg",
             "url": "https://soundcloud.com/summrs/yessa",
         },
         
     ],
 },
 {
     "name": "Lil Shine",
     "image": "lil shine.gif",                      # file name inside images/
     "aliases": ["shine",],                    # ["Other Name", "Old Tag"]
     "dob": "February 18, 2005",                        # "1996-03-04" or "March 4, 1996"
     "links": {
         "spotify": "https://open.spotify.com/artist/6SmUCZMpJG06ZhIqMOJKCn",
         "youtube_music": "https://music.youtube.com/@1lilshine",
         "soundcloud": "https://soundcloud.com/ilovelilshine",
     },
     "projects": [
         {
             "title": "Losing Myself",
             "kind": "Album",          # Album / EP / Mixtape
             "year": "October 31, 2022",
             "cover": "Lil Shine - Losing Myself.jpg",              # file name inside images/
	         "url": "https://music.youtube.com/playlist?list=OLAK5uy_l8c_iWdlA1xKJLGTezgOInPZ3VYEaPN6Q",
             "tracks": [
                       "Losing Myself (prod. XanGang)",
	                   "Tempo (prod. AxJunior)",
	                   "Tied Up (prod. ZeeGoinXrazy)",
                       "Closure (prod. MaliceMoniz)",
                       "Daily Basis (prod. MaliceMoniz, Zhizhi)",
	                   "Insane (prod. MaliceMoniz, Marko)",
	                   "Truth Hurts (prod. nullkarta)",
                       "Feel Me (prod. Zukobain)",
                       "It's Over (prod. MaliceMoniz)",
                       "Watch It Bleed (prod. Skys, 30nickk, Lucid)",
                       "Don't Wanna Talk (prod. MaliceMoniz, jalenvlm)",
                       "Stars (prod. MaliceMoniz)",
                       "Told Her (prod. MaliceMoniz, Marko)",
                       "Goes Down (prod. Cloudbxy, Xosfromhell)",
                       "Choose Up (feat. Corey Lingo) (prod. MaliceMoniz, jalenvlm)",
             ],
         },
         {
             "title": "Lovesick",
             "kind": "EP",          # Album / EP / Mixtape
             "year": "August 1, 2023",
             "cover": "Lil Shine - Lovesick.jpg",              # file name inside images/
	         "url": "https://music.youtube.com/playlist?list=OLAK5uy_mhrBTW841FkMjwbuL9gOXA4v3YpeEBwBk",
             "tracks": [
                       "No More Rainy Days (Intro) (prod. MaliceMoniz, jalenvlm)",
	                   "Mistakes (prod. Cloudbxy)",
	                   "Alone (prod. pb3nch, voiceluvv)",
                       "Lovesick (prod. jalenvlm)",
                       "One Last Time (prod. nullkarta, Zukobain)",
	                   "Jeans Soaked (prod. jalenvlm)",
	                   "Too Much (prod. yvngzwest)",
                       "Worthless (prod. Iceteashawty)",
             ],
         },
         {
             "title": "Shine Forever",
             "kind": "Album",          # Album / EP / Mixtape
             "year": "January 1, 2025",
             "cover": "Lil Shine - Shine Forever.jpg",              # file name inside images/
	         "url": "https://music.youtube.com/playlist?list=OLAK5uy_nwdCRwaMnR5uQtPJ75eyP-pn5aao7yiv4",
             "tracks": [
                       "Game Day (prod. MaliceMoniz)",
	                   "Enticing (prod. nullkarta)",
	                   "Same Shit (prod. XanGang, Jkei)",
                       "Date Night (prod. Bstrxy, jalenvlm)",
                       "Worst Me (prod. fleafriends)",
	                   "Dork (prod. Zukobain, Sleepy)",
	                   "Reckless 2 (prod. Goyxrd)",
                       "God (prod. MaliceMoniz, L3)",
                       "Wassuhh (prod. Neimxn, MaliceMoniz)",
                       "G.Y.B (prod. MaliceMoniz)",
                       "Feel Me 2 (prod. Zukobain)",
                       "KissMeThruDaPhone (prod. nullkarta)",
                       "One Chance/In2Dis (prod. kudz, jalenvlm, Xankoma, se7en)",
             ],
         },
         {
             "title": "Get Rich Or Die Sippin'",
             "kind": "Album",          # Album / EP / Mixtape
             "year": "May 15, 2026",
             "cover": "Lil Shine - Get Rich Or Die Sippin.jpg",              # file name inside images/
	         "url": "https://music.youtube.com/playlist?list=OLAK5uy_lJNEC5rHbhf6CNSLYjxjAP6FGv9TELT2M",
             "tracks": [
                       "Nobody (prod. Maxim)",
	                   "Way2Up (prod. MaliceMoniz)",
	                   "Got Down (prod. Maxim)",
                       "Dam, Dam (prod. Maxim)",
                       "Like What? (prod. jalenvlm)",
	                   "Still Sippin' (feat. Summrs) (prod. MaliceMoniz)",
	                   "Forever (prod. nullkarta)",
                       "I Can't Go 4 Dat (prod. Lil Shine, MaliceMoniz)",
                       "So High (prod. Lil Shine, Skys)",
                       "Just Me N' My Cup (prod. mental, blxty)",
                       "You + Me (prod. MaliceMoniz)",
                       "Aye Malice Where The Bass @? (prod. MaliceMoniz, XanGang)",
                       "Jump Back In (prod. nullkarta, Zukobain)",
                       "Loud! (prod. Maxim)",
                       "All Love (prod. Maxim)",
                       "Red Dot (feat. Kankan) (prod. XanGang)",
                       "Five Star (prod. nullkarta)",
                       "Finally (The End) (prod. Lil Shine, MaliceMoniz)",
             ],
         },
         {
             "title": "Tearscape",
             "kind": "Album",          # Album / EP / Mixtape
             "year": "September 2, 2023",
             "cover": "Lil Shine - Tearscape.jpg",              # file name inside images/
	         "url": "https://music.youtube.com/playlist?list=OLAK5uy_lCjs-JedYlQrESDNrbELWOQBWbkfuhCiA",
             "tracks": [
                       "Lust (prod. jalenvlm, Shingan)",
	                   "Spotlight (prod. Kasamigo, TsePoppa, Cloudbxy)",
	                   "Wake Up (prod. voiceluvv, wintfye)",
                       "Falling 4 You (prod. Roxys, Sewsi)",
             ],
         },

     ],
     "singles": [
         {
             "title": "Loser (prod. MaliceMoniz)",
             "year": "November 11, 2021",
             "cover": "Lil Shine - Loser.jpg",
             "url": "https://soundcloud.com/ilovelilshine/loser-prod-solxmn",
         },
         {
             "title": "Snow Keep Fallin (prod. Wangi, Galaxxy4r)",
             "year": "March 21, 2022",
             "cover": "Lil Shine - Snow Keep Fallin.jpg",
             "url": "https://soundcloud.com/ilovelilshine/snow-keep-fallin-prod-galaxxy",
         },
         {
             "title": "See U In H3ll (prod. MaliceMoniz)",
             "year": "April 7, 2022",
             "cover": "Lil Shine - See U In H3ll.jpg",
             "url": "https://soundcloud.com/ilovelilshine/see-u-in-h3ll-prod-solxmn",
         },
         {
             "title": "Loose Ends (prod. nullkarta, Zukobain)",
             "year": "May 7, 2022",
             "cover": "Lil Shine - Loose Ends.jpg",
             "url": "https://soundcloud.com/ilovelilshine/loose-ends-prod-1kkyoto",
         },
         {
             "title": "By Myself (feat. Lawsy) (prod. Oscar)",
             "year": "May 14, 2022",
             "cover": "Lil Shine - By Myself.jpg",
             "url": "https://soundcloud.com/ilovelilshine/by-myself-w-lawsy-prod-oscar",
         },
         {
             "title": "Won't Stop (prod. nullkarta)",
             "year": "June 16, 2022",
             "cover": "Lil Shine - Won't Stop.jpg",
             "url": "https://soundcloud.com/ilovelilshine/wont-stop-prod-1kkyoto",
         },
         {
             "title": "Tell Me (pord. MaliceMoniz, AxJunior)",
             "year": "August 9, 2022",
             "cover": "Lil Shine - Tell Me.jpg",
             "url": "https://soundcloud.com/ilovelilshine/tell-me-prod-solxmn-and",
         },
         {
             "title": "How Deep Is Your Love (prod. Absxnce)",
             "year": "January 9, 2023",
             "cover": "Lil Shine - How Deep Is Your Love.jpg",
             "url": "https://soundcloud.com/ilovelilshine/how-deep-is-your-love-prod-absence",
         },
         {
             "title": "How It Goes (prod. Cloudbxy, Raken)",
             "year": "February 18, 2023",
             "cover": "Lil Shine - How It Goes.jpg",
             "url": "https://soundcloud.com/ilovelilshine/how-it-goes-prod-cloudbxy",
         },
         {
             "title": "Falling 4 You (prod. Roxys, Sewsi)",
             "year": "August 19, 2023",
             "cover": "Lil Shine - Falling 4 You.jpg",
             "url": "https://soundcloud.com/ilovelilshine/falling-4-you-prod-roxys",
         },
         {
             "title": "Lie Once, Lost Trust (prod. Gurushawty, Absxnce)",
             "year": "November 28, 2022",
             "cover": "Lil Shine - Lie Once, Lost Trust.jpg",
             "url": "https://soundcloud.com/ilovelilshine/lie-once-lost-trust-prod",
         },
         {
             "title": "Too Bad (prod. AxJunior, MaliceMoniz)",
             "year": "October 7, 2023",
             "cover": "Lil Shine - Too Bad.jpg",
             "url": "https://soundcloud.com/ilovelilshine/too-bad-prod-solxmn-axjunior",
         },
         {
             "title": "Hop Out (feat. Summrs) (prod. jalenvlm)",
             "year": "December 22, 2023",
             "cover": "Lil Shine - Hop Out.jpg",
             "url": "https://soundcloud.com/ilovelilshine/hop-out",
         },
         {
             "title": "Str8 Like Dat (prod. nullkarta, jalenvlm)",
             "year": "January 26, 2024",
             "cover": "Lil Shine - Str8 Lke Dat.jpg",
             "url": "https://soundcloud.com/mkeitstop/str8-like-dat-prod-1kkyoto-jxyy2k",
             "music_video": "https://www.youtube.com/watch?v=JYg8NEfTF6U",
         },
         {
             "title": "Snakes (prod. nullkarta)",
             "year": "April 5, 2024",
             "cover": "Lil Shine - Snakes.jpg",
             "url": "https://soundcloud.com/ilovelilshine/snakes",
         },
         {
             "title": "Dork (prod. Zukobain, Sleepy)",
             "year": "October 18, 2024",
             "cover": "Lil Shine - Dork.jpg",
             "url": "https://soundcloud.com/ilovelilshine/dork",
         },
         {
             "title": "Date Night",
             "year": "December 25, 2024",
             "cover": "Lil Shine - Shine Forever.jpg",
             "url": "https://soundcloud.com/ilovelilshine/date-night-prod-jxyy2k-bstrxy",
         },
         {
             "title": "Go Spin (prod. nullkarta)",
             "year": "September 26, 2025",
             "cover": "Lil Shine - Go Spin.jpg",
             "url": "https://soundcloud.com/ilovelilshine/go-spin-prod-1kkyoto",
         },
         {
             "title": "Sex Talk (prod. nullkarta)",
             "year": "October 17, 2025",
             "cover": "Lil Shine - Sex Talk.jpg",
             "url": "https://soundcloud.com/ilovelilshine/sex-talk-prod-1kkyoto",
         },
         {
             "title": "Fast Money (prod. jalenvlm)",
             "year": "October 31, 2025",
             "cover": "Lil Shine - Fast Money.jpg",
             "url": "https://soundcloud.com/ilovelilshine/fast-money-prod-jxyy2k",
         },
         
     ],
 },
 
 {
     "name": "conjuraxxion",
     "image": "conjuraxxion.gif",                      # file name inside images/
     "aliases": ["ECLIPSEXTAPE", "luci4isreal", "conjur8", "conjuraxxion {{6͙̜̤ͩ̆8̯̭̓̇͂6͙̜̤ͩ̆}}"],                    # ["Other Name", "Old Tag"]
     "dob": "",                        # "1996-03-04" or "March 4, 1996"
     "collectives": "iGore",
     "links": {
         "spotify": "https://open.spotify.com/artist/0R8fqxWf5aKOTWS3c8hwxB",
         "youtube_music": "https://music.youtube.com/@conjuraxxion",
         "soundcloud": "https://soundcloud.com/conjuraxxion",
     },
     "projects": [
         {
             "title": "Twilight Eclipse",
             "kind": "Album",          # Album / EP / Mixtape
             "year": "December 30, 2024",
             "cover": "conjuraxxion - Twilight Eclipse.jpg",              # file name inside images/
	         "url": "https://open.spotify.com/album/3HXSZWdAoDBHlD27BpvagG",
             "tracks": [
                       "It Get Vloody (prod. ordenupset)",
	                   "We are all vampires (feat. Luci4, OsamaSon) (prod. Luci4, OGWSIN)",
	                   "King Of The Sigils (prod. Goxan)",
                       "5KINWALKER (feat. LAZER DIM 700) (prod. Shadow Wizard Money Gang)",
                       "Real Vamp Stepper (prod. ordenupset)",
	                   "Vloody Walls (prod. Jshxwty)",
	                   "Twilight Night Club (feat. skypearleddat)",
             ],
         },
         {
             "title": "(Vampire Jesters)",
             "kind": "Collab EP (bleood & conjuraxxion)",          # Album / EP / Mixtape
             "year": "December 16, 2025",
             "cover": "bleood - vampire jesters.png",              # file name inside images/
             "collab": "bleood",
	         "url": "https://music.youtube.com/playlist?list=OLAK5uy_myuKtisPvDXZq0l8p9V8Wq9rB297il_mQ",
             "music_video": "https://www.youtube.com/watch?v=U0CbbHlZYKM",
             "tracks": [
                       "Streamer Money (prod. aghast)",
	                   "Jester vampires wit Guns (prod. bbmonsterdd)",
	                   "Lean Zombie (prod. dluxx)",
                       "Add Me Mud (prod. truslo, DJ L Beats)",
             ],
         },
         {
             "title": "Gatekeep Me, I Understand.",
             "kind": "Album",          # Album / EP / Mixtape
             "year": "June 26, 2026",
             "cover": "conjuraxxion - Gatekeep Me I Understand.jpg",              # file name inside images/
	         "url": "https://music.youtube.com/playlist?list=OLAK5uy_nO_j6GPK8ta3Wz9c01Gm5TH9XClfQT0qk",
             "tracks": [
                       "Stack Stack (prod. AURAMAXXER2015)",
	                   "All Black Fit",
	                   "Laughing In The Dark 2 (prod. isdamenok)",
                       "I'm up next (prod. conjuraxxionglazer)",
                       "p90 (prod. jetski)",
	                   "Make Em Bleed (prod. North West)",
	                   "When Dat Time Come Up (prod. bbmonsterdd)",
                       "He Did It (prod. jetski)",
                       "OMG, WTF!!!! (prod. Gen6)"
             ],
         },
         {
             "title": "ART",
             "kind": "EP",          # Album / EP / Mixtape
             "year": "August 31, 2026",
             "cover": "conjuraxxion - ART.jpg",              # file name inside images/
	         "url": "https://music.youtube.com/playlist?list=OLAK5uy_kN58Y71pH07FAm9ga8PJmKQDkQejnIKpE",
             "tracks": [
                       "NO PLACE FOR THIS SOUND",
	                   "BEFORE U KNEW ME",
	                   "REST IN JEST (feat. slaywitme) (prod. yrsci)",
                       "KYS BROKE BOY (feat. yrsci) (prod. yrsci)",
                       "I DON'T WANNA BE A FAILURE",
             ],
         },

     ],
     "singles": [
         {
             "title": "#life360 (prod. feliciasepesh)",
             "year": "December 26, 2023",
             "cover": "conjuraxxion - #life360.jpg",
             "url": "https://soundcloud.com/conjuraxxion/life360",
         },
         {
             "title": "vampire the masquerade (feat. MajinBlxxdy) (prod. sam rubin)",
             "year": "January 24, 2024",
             "cover": "conjuraxxion - vampire the masquerade.jpg",
             "url": "https://soundcloud.com/conjuraxxion/vampire-the-masquerade",
         },
         {
             "title": "5G (prod. KRXXK)",
             "year": "February 18, 2024",
             "cover": "conjuraxxion - 5G.jpg",
             "url": "https://soundcloud.com/conjuraxxion/swmg-mix-m",
         },
         {
             "title": "xxwitch (feat. Luci4) (prod. Luci4)",
             "year": "May 8, 2024",
             "cover": "conjuraxxion - xxwitch.jpg",
             "url": "https://soundcloud.com/conjuraxxion/luci4-x-eclipsextape-xxwitch",
         },
         {
             "title": "Vampire Plugg (prod. Luci4)",
             "year": "September 10, 2024",
             "cover": "conjuraxxion - VAMPIRE PLUGG.jpg",
             "url": "https://soundcloud.com/luci4isreal/1161vampire-plugg-pr0d-xx-luci4",
         },
         {
             "title": "Negative",
             "year": "February 2, 2025",
             "cover": "conjuraxxion - Negative.jpg",
             "url": "https://soundcloud.com/conjuraxxion/glock-and-a-k",
         },
         {
             "title": "ghoxxt #xxorcery #242",
             "year": "December 10, 2025",
             "cover": "conjuraxxion - ghoxxt.jpg",
             "url": "https://music.youtube.com/playlist?list=OLAK5uy_lvLQnxHUJnncwNcywmJVEeQNJm1uFczco",
         },
         {
             "title": "AINT XXHIT (prod. conjuraxxion)",
             "year": "July 14, 2025",
             "cover": "conjuraxxion - AINT XXHIT.jpg",
             "url": "https://soundcloud.com/conjuraxxion/conjuraxxionaintshit",
         },
         {
             "title": "BLXXD THURXXTY #g8keep (prod. djstar)",
             "year": "November 6, 2025",
             "cover": "conjuraxxion - BLXXD THURXXTY.jpg",
             "url": "https://music.youtube.com/playlist?list=OLAK5uy_kqx69FnTwwk7yMoDvia2NdU6g_t2dQ0WQ",
         },
         {
             "title": "katch a kase (prod. djstar)",
             "year": "November 6, 2025",
             "cover": "conjuraxxion - katch a kase.jpg",
             "url": "https://music.youtube.com/playlist?list=OLAK5uy_kFh3h151pOfRlMFmKXWYVmENQT5jHH1Ck",
         },
         {
             "title": "I'm Not Cool",
             "year": "December 10, 2025",
             "cover": "conjuraxxion - I'm Not Cool.jpg",
             "url": "https://music.youtube.com/playlist?list=OLAK5uy_leHuj9SrHmbgHRBFf5i2rwdgEPWQZAWak",
         },
         {
             "title": "NOBODY WANTED TO LISTEN #68k #g8keeep #xxorcery",
             "year": "December 10, 2025",
             "cover": "conjuraxxion - NOBODY WANTED TO LISTEN.jpg",
             "url": "https://soundcloud.com/crysquad/old-version-conjuraxxion-6-8",
         },
         {
             "title": "iiiTAKEHOEXX",
             "year": "December 10, 2025",
             "cover": "conjuraxxion - iiiTAKEHOEXX.jpg",
             "url": "https://music.youtube.com/playlist?list=OLAK5uy_n0ngIbtz59h9vgwiUwAar7b1tSGdq3Rkk",
         },
         {
             "title": "we don't gaf if you think you're famous",
             "year": "February 27, 2026",
             "cover": "conjuraxxion - we don't gaf if you think you're famous.jpg",
             "url": "https://soundcloud.com/conjuraxxion/ruff-mix-1-1",
         },
         {
             "title": "Laughing In The Dark (prod. prank)",
             "year": "April 1, 2026",
             "cover": "conjuraxxion - Laughing In The Dark.jpg",
             "url": "https://soundcloud.com/conjuraxxion/down-bad_2s",

         },
         {
             "title": "Inspire Then Die",
             "year": "May 1, 2026",
             "cover": "conjuraxxion - Inspire Then Die.jpg",
             "url": "https://soundcloud.com/conjuraxxion/i-need-it_3",
 
         },
         {
             "title": "will he do it? (prod. jetski)",
             "year": "April 25, 2026",
             "cover": "conjuraxxion - Will He Do It.jpg",
             "url": "https://soundcloud.com/conjuraxxion/will-he-do-it",

         },
         {
             "title": "Grand Theft Alchemy 7 (feat. slaywitme)",
             "year": "May 29, 2026",
             "cover": "conjuraxxion - Grand Theft Alchemy.jpg",
             "url": "https://soundcloud.com/conjuraxxion/rolling",

         },
         {
             "title": "cope harder (prod. bbmonsterdd)",
             "year": "May 31, 2026",
             "cover": "conjuraxxion - cope harder.jpg",
             "url": "https://soundcloud.com/conjuraxxion/conjuraxxion-prod-vol5k",
         },
         {
             "title": "Best Story (prod. vlor5k)",
             "year": "September 24, 2026",
             "cover": "conjuraxxion - Best Story.jpg",
             "url": "https://soundcloud.com/conjuraxxion/merged-copy-of-mic2-copy-of-mic3-3",
         },
         
     ],
 },
 {
     "name": "yoi",
     "image": "yoi - igore ugore wegore.png",                      # file name inside images/
     "aliases": ["yoidead"],                    # ["Other Name", "Old Tag"]
     "dob": "",                        # "1996-03-04" or "March 4, 1996"
     "collectives": ["iGore",],
     "links": {
         "spotify": "https://open.spotify.com/artist/6EqwmpSrsuOccgJqszTkT7",
         "youtube_music": "",
         "soundcloud": "https://soundcloud.com/y0i",
     },
     "singles": [
         {
             "title": "arp my tooli (feat. bleood) (prod. yoi)",
             "year": "November 4, 2024",
             "cover": "yoi - arp my tooli.jpg",
             "url": "https://soundcloud.com/y0i/arp-my-tooli-bleood",
         },
         {
             "title": "u cant understand dis (feat. bleood) (prod. yoi)",
             "year": "December 13, 2024",
             "cover": "yoi - u cant understand dis.jpg",
             "url": "https://soundcloud.com/y0i/u-cant-understand-dis-yoi",
         },
         {
             "title": "igore ugore wegore (feat. yrsci, bleood, ivvys) (prod. yoi)",
             "year": "February 18, 2025",
             "cover": "yoi - igore ugore wegore.png",
             "url": "https://soundcloud.com/y0i/igore-ugore-wegore",
         },
         {
             "title": "whatamidoing (prod. yoi)",
             "year": "March 1, 2025",
             "cover": "yoi - whatamidoing.jpg",
             "url": "https://soundcloud.com/y0i/whatamidoing",
         },
         {
             "title": "stim2this (prod. yoi)",
             "year": "May 6, 2025",
             "cover": "yoi - stim2this.jpg",
             "url": "https://soundcloud.com/y0i/stim2this",
         },
         {
             "title": "i kno (feat. sexadlibs) (prod. yoi, dontscrewmeover)",
             "year": "May 10, 2025",
             "cover": "yoi - i kno.jpg",
             "url": "https://soundcloud.com/y0i/i-kno-prod-yoi-dontscrewmeover",
         },
         {
             "title": "the last song ever (prod. yoi)",
             "year": "July 2, 2026",
             "cover": "yoi - the last song ever.jpg",
             "url": "https://soundcloud.com/y0i/the-last-song-ever",
         },
         {
             "title": "udontphaseme (prod. yoi)",
             "year": "February 5, 2025",
             "cover": "yoi - udontphaseme.jpg",
             "url": "https://soundcloud.com/y0i/udontphaseme",
         },
         
     ],
 },
 {
     "name": "ohsxnta",
     "image": "ohsxnta.gif",                      # file name inside images/
     "aliases": [""],                    # ["Other Name", "Old Tag"]
     "dob": "September 13, 2007",                        # "1996-03-04" or "March 4, 1996"
     "collectives": "Slime Krew",
     "links": {
         "spotify": "https://open.spotify.com/artist/5N2HfY7vdwZ6lLVHOW5D14",
         "youtube_music": "https://music.youtube.com/channel/UCpDonj8b-ht0uKK4V3mHwag",
         "soundcloud": "https://soundcloud.com/ohsxnta",
     },
     "projects": [
         {
             "title": "dawn",
             "kind": "EP",          # Album / EP / Mixtape
             "year": "September 11, 2022",
             "cover": "ohsxnta - dawn.jpg",              # file name inside images/
	         "url": "https://music.youtube.com/playlist?list=OLAK5uy_kxt2nl1CEDp6-jd7OGgD-DZPrK5I4FzM4",
             "tracks": [
                       "luv (prod. perc40)",
	                   "feel me (prod. tdf, perc40)",
	                   "tricks (feat. Okaymar) (prod. AltoSGP)",
                       "hope (prod. perc40)",
             ],
         },
         {
             "title": "The Cure",
             "kind": "Album",          # Album / EP / Mixtape
             "year": "July 12, 2024",
             "cover": "ohsxnta - The Cure.jpg",              # file name inside images/
	         "url": "https://music.youtube.com/playlist?list=OLAK5uy_kejaZaxeWPxSfTPJTlXVxWb3BFgmAj3vI",
             "music_video": "https://www.youtube.com/watch?v=BkADuGY3zDY",
             "tracks": [
                       "Just Me (prod. skai)",
	                   "Turks (prod. tdf)",
	                   "All Day (prod. skai)",
                       "For You (prod. perc40)",
                       "Say My Name (prod. skai)",
	                   "Justin Bieber (prod. skai)",
	                   "Anti-Hero (prod. perc40, XanGang)",
                       "Mashallah (prod. boolymon)",
                       "I Know You (prod. tdf)",
                       "Don't Worry (prod. marcusbasquiat)",
                       "Change (prod. perc40)",
             ],
         },
         {
             "title": "ohsama",
             "kind": "Collab EP  (OsamaSon & ohsxnta)",          # Album / EP / Mixtape
             "year": "March 27, 2023",
             "cover": "ohsxnta - ohsama.jpg",              # file name inside images/
	         "url": "https://music.youtube.com/playlist?list=PLo45IyUdwz374Y04vTJFNBsVxASaYWeBW",
             "collab": "OsamaSon",
             "tracks": [
                       "good try (prod. Thrty)",
	                   "red walls (prod. boolymon)",
	                   "child support (prod. perc40)",
                       "ms jackson (feat. wildkarduno) (prod. perc40, Jake Hansen)",
                       "glod up (feat. 1oneam) (prod. tdf, perc40)",
	                   "get slayed (prod. tdf)",
	                   "over (feat. 1oneam, Okaymar) (prod. twovrt, Marrgielaa)",
                       "lmk (prod. perc40, utrippin!)",
             ],
         },

     ],
     "singles": [
         {
             "title": "assumptions (prod. perc40)",
             "year": "October 15, 2022",
             "cover": "ohsxnta - assumptions.jpg",
             "url": "https://soundcloud.com/1ohsxnta_archive/assumptions-prod-perc40",
         },
         {
             "title": "no help (prod. perc40)",
             "year": "December 19, 2022",
             "cover": "ohsxnta - no help.jpg",
             "url": "https://soundcloud.com/ohsxnta/nohelp",
         },
         {
             "title": "uh oh (feat. 1oneam) (prod. perc40)",
             "year": "January 21, 2023",
             "cover": "ohsxnta - uh oh.jpg",
             "url": "https://soundcloud.com/1ohsxnta_archive/uh-oh-ft-1oneam-perc40",
         },
         {
             "title": "elegant (prod. perc40)",
             "year": "April 1, 2023",
             "cover": "ohsxnta - elegant.jpg",
             "url": "https://soundcloud.com/ohsxnta-archive/ohsxnta-elegant-perc40",
         },
         {
             "title": "thrtyball (prod. Thrty, Marrgielaa)",
             "year": "April 29, 2023",
             "cover": "ohsxnta - thrtyball.jpg",
             "url": "https://soundcloud.com/sdwo/ohsxnta-thrtyball-prod-thrty-marrgielaa",
         },
         {
             "title": "Pink Flat (prod. tdf)",
             "year": "October 6, 2023",
             "cover": "ohsxnta - Pink Flat.jpg",
             "url": "https://soundcloud.com/ohsxnta/pink-flat-produced-by-tdf",
         },
         {
             "title": "tookoffdabrain (prod. legion)",
             "year": "December 22, 2023",
             "cover": "ohsxnta - tookoffdabrain.jpg",
             "url": "https://soundcloud.com/ohsxnta/tookoffdabrain",
         },
         {
             "title": "barter (prod. perc40)",
             "year": "March 11, 2024",
             "cover": "ohsxnta - barter.jpg",
             "url": "https://soundcloud.com/ohsxnta/barter",
         },
         {
             "title": "Fuck Up Chos' (prod. CXO)",
             "year": "July 25, 2025",
             "cover": "ohsxnta - Fuck Up Chos'.jpg",
             "url": "https://soundcloud.com/ohsxnta/fck-up-chos",
         },
         {
             "title": "I Want My Heart Back (prod. CXO, ohsxnta)",
             "year": "April 24, 2026",
             "cover": "ohsxnta - I Want My Heart Back.jpg",
             "url": "https://soundcloud.com/ohsxnta/i-want-my-heart-back",
             "music_video": "https://www.youtube.com/watch?v=cKVzhiG5efk",
         },       
     ],
 },
 {
     "name": "Okaymar",
     "image": "Okaymar.gif",                      
     "aliases": ["",],                    
     "dob": "October 16, 2001",
     "collectives": "Slime Krew",
     "links": {
         "spotify": "https://open.spotify.com/artist/1IftlrOYVKoySjPYWNGO7K",
         "youtube_music": "https://music.youtube.com/channel/UCdrwsS4OwpITYecyzfqwOMg",
         "soundcloud": "https://soundcloud.com/okaymar",
     },
     "projects": [
         {
             "title": "lost files",
             "kind": "Album",          
             "year": "February 15, 2022",
             "cover": "Okaymar - lost files.jpg",              
	         "url": "https://soundcloud.com/1okaymar/sets/lost-files",
             "tracks": [
                       "weirdo (prod. twentywrld)",
	                   "g6 (prod. tdf)",
	                   "studio (prod. tdf, twentywrld)",
                       "juco (prod. tdf)",
                       "go ahead (prod. fakekickin)",
	                   "haha (prod. Toren Berios)",
	                   "murder muzik remix (prod. Rok, bart how, 4VRLIT)",
                       "top this (feat. Khalifsb) (prod. tdf)",
                       "undercover (prod. tdf)",
                       "dior (feat. Kankan) (prod. BenjiCold)",
             ],
         },


     ],
     "singles": [
         {
             "title": "Yellow (prod. perc40)",
             "year": "November 5, 2021",
             "cover": "Okaymar - Yellow.jpg",
             "url": "https://soundcloud.com/okaymar/yellow-prod-perc40",
         },
         {
             "title": "Sike (prod. tdf)",
             "year": "December 10, 2021",
             "cover": "Okaymar - Sike.jpg",
             "url": "https://soundcloud.com/okaymar/sike-prod-tdf-1",
         },
         {
             "title": "Fun (feat. 1oneam) (prod. perc40)",
             "year": "December 16, 2021",
             "cover": "Okaymar - Fun.jpg",
             "url": "https://soundcloud.com/okaymar/fun-ft-1oneamprod-perc40",
         },
         {
             "title": "Change (prod. Rare1)",
             "year": "January 9, 2022",
             "cover": "Okaymar - Change.jpg",
             "url": "https://soundcloud.com/okaymar/change-prod-rare1",
         },
         {
             "title": "Chef (prod. tdf)",
             "year": "February 4, 2022",
             "cover": "Okaymar - Chef.jpg",
             "url": "https://soundcloud.com/okaymar/chef-prod-tdf",
         },
         {
             "title": "Pouring Up (prod. perc40)",
             "year": "February 16, 2022",
             "cover": "Okaymar - Pouring Up.jpg",
             "url": "https://soundcloud.com/okaymar/pouring-up-prod-perc40",
         },
         {
             "title": "Tec (feat. Smokingskul) (prod. perc40)",
             "year": "March 6, 2022",
             "cover": "Okaymar - Tec.jpg",
             "url": "https://soundcloud.com/okaymar/tec-ft-smokingskul-prod-perc40",
         },
         {
             "title": "Woke up (feat. Lil Shine) (prod. AxJunior)",
             "year": "May 11, 2022",
             "cover": "Okaymar - Woke Up.jpg",
             "url": "https://soundcloud.com/okaymar/woke-up-ft-lil-shine-prod-axjunior",
         },
         {
             "title": "Freeway (feat. 1oneam, ohsxnta) (prod. perc40)",
             "year": "August 3, 2022",
             "cover": "Okaymar - Freeway.jpg",
             "url": "https://soundcloud.com/okaymar/freeway-ft-1oneam-ohsxnta-prod",
         },
         {
             "title": "Boot Up (prod. tdf)",
             "year": "July 7, 2022",
             "cover": "Okaymar - Boot Up.jpg",
             "url": "https://soundcloud.com/okaymar/boot-up-prod-tdf",
         },
         {
             "title": "Lab (prod. Jake Hansen)",
             "year": "October 17, 2022",
             "cover": "Okaymar - Lab.jpg",
             "url": "https://soundcloud.com/okaymar/lab-prod-jakehansen",
         },
         {
             "title": "Leave me alone <3 (prod. tdf)",
             "year": "January 18, 2023",
             "cover": "Okaymar - Leave Me Alone.jpg",
             "url": "https://soundcloud.com/okaymar/leave-me-alone-3-prod-tdf",
         },
         {
             "title": "Get right (prod. tdf)",
             "year": "March 20, 2023",
             "cover": "Okaymar - Get Right.jpg",
             "url": "https://soundcloud.com/okaymar/get-right-prod-tdf",
         },
         {
             "title": "Field Day (feat. 1oneam) (prod. perc40, 1oneam)",
             "year": "July 12, 2023",
             "cover": "Okaymar - Field Day.jpg",
             "url": "https://soundcloud.com/okaymar/field-day-ft-1oneam-prod-perc40-1oneam",
         },
         {
             "title": "Vacate (prod. Thrty)",
             "year": "August 23, 2023",
             "cover": "Okaymar - Vacate.jpg",
             "url": "https://soundcloud.com/okaymar/vacate-prod-thrty-1",
         },
         {
             "title": "Buy it (feat. 1oneam) (prod. perc40)",
             "year": "December 20, 2023",
             "cover": "Okaymar - Buy it.jpg",
             "url": "https://soundcloud.com/okaymar/buy-it-ft-1oneam-prod-perc40",
         },
         {
             "title": "Boolymon (feat. 1oneam) (prod. boolymon)",
             "year": "March 27, 2024",
             "cover": "Okaymar - Boolymon.jpg",
             "url": "https://soundcloud.com/okaymar/boolymon-ft-1oneam-prod-boolymon",
         },
         {
             "title": "Different (prod. tdf)",
             "year": "July 1, 2024",
             "cover": "Okaymar - Different.jpg",
             "url": "https://soundcloud.com/okaymar/different-prod-tdf",
         },
         {
             "title": "Okay (prod. prettifun)",
             "year": "September 17, 2024",
             "cover": "Okaymar - Okay.jpg",
             "url": "https://soundcloud.com/okaymar/okay-prod-prettifun",
         },
         {
             "title": "Laid (prod. tdf)",
             "year": "June 22, 2026",
             "cover": "Okaymar - Laid.jpg",
             "url": "https://soundcloud.com/salo-870558738/okaymar-laid",
         },
         
     ],
 },
 
 {
     "name": "1oneam",
     "image": "1oneam-showcasing-food.gif",                      # file name inside images/
     "aliases": ["lil' Zen",],                    # ["Other Name", "Old Tag"]
     "dob": "August 10, 2004",                        # "1996-03-04" or "March 4, 1996"
     "collectives": "Slime Krew",
     "links": {
         "spotify": "https://open.spotify.com/artist/089ASSwOW4Cih3frNuDtUv",
         "youtube_music": "https://music.youtube.com/channel/UCmX4ZeZ9ClPTiS8CIDieXcg",
         "soundcloud": "https://soundcloud.com/xx1oneam",
     },
     "projects": [
         {
             "title": "zen",
             "kind": "Album",          # Album / EP / Mixtape
             "year": "March 20, 2022",
             "cover": "1oneam - zen.jpg",              # file name inside images/
	         "url": "https://music.youtube.com/playlist?list=OLAK5uy_kIh8fQRZK33FTrO7aEYC0GJbYM1-5zPzE",
             "tracks": [
                       "bottega (prod. perc40)",
	                   "ran off (prod. fakekickin, Jake Hansen)",
	                   "selfish (prod. kohl)",
                       "over (prod. boost)",
                       "zen (prod. theo)",
	                   "sick (prod. perc40, tdf)",
	                   "aint feeling good (prod. tdf)",
                       "iran (prod. perc40, twentywrld)",
             ],
         },
         {
             "title": "myself",
             "kind": "Album",          # Album / EP / Mixtape
             "year": "September 16, 2022",
             "cover": "1oneam - myself.jpg",              # file name inside images/
	         "url": "https://music.youtube.com/playlist?list=OLAK5uy_mlbUzT8cjOy86dG_ncKHCG2LX7CkPGIKA",
             "tracks": [
                       "sorry (prod. perc40)",
	                   "cyclone (prod. perc40, Jake Hansen)",
	                   "wyo (prod. AltoSGP, A$att)",
                       "now (prod. AltoSGP)",
                       "too high (prod. perc40)",
	                   "casualties (prod. perc40)",
	                   "puppet (prod. tdf)",
                       "adderal (prod. perc40, utrippin!)",
             ],
         },
         {
             "title": "House Party",
             "kind": "Album",          # Album / EP / Mixtape
             "year": "October 20, 2023",
             "cover": "1oneam - House Party.jpg",              # file name inside images/
	         "url": "https://music.youtube.com/playlist?list=OLAK5uy_m5nf4en9HrJYhNLIuXBDe0wV2LRsx8_CM",
             "tracks": [
                       "Drunk AF (prod. tdf)",
	                   "Coke (prod. perc40)",
	                   "Too Late (prod. tdf)",
                       "Cancer (prod. tdf)",
                       "Dancer Bitch (prod. tdf)",
	                   "Out Da 34rth (prod. tdf)",
	                   "Double Up (prod. tdf)",
                       "2 Friends (prod. Rok)",
                       "Calling (prod. 1oneam)",
                       "Trap (prod. 1oneam)",
                       "Hemi (prod. tdf)",
                       "Push Start (prod. 1oneam)",
                       "My Arms (prod. tdf)",
                       "Grow Up (prod. tdf)",
             ],
         },
         {
             "title": "One Life",
             "kind": "Mixtape",          # Album / EP / Mixtape
             "year": "May 31, 2024",
             "cover": "1oneam - One Life.jpg",              # file name inside images/
	         "url": "https://music.youtube.com/playlist?list=OLAK5uy_lSdvpAjobE8p2gFS8hTJi3uO_S1YAUDFA",
             "tracks": [
                       "One Life (prod. 1oneam)",
	                   "Let You Down (prod. 1oneam)",
	                   "Who? Not Me (prod. 1oneam)",
                       "Want To (prod. 1oneam)",
                       "Lil Kim (prod. perc40)",
	                   "Bless Up (prod. tdf)",
	                   "Where You At? (prod. perc40)",
                       "Core (prod. 1oneam)",
                       "Balling (prod. skai)",
                       "Dlow (prod. twovrt)",
                       "Van Gogh (prod. tdf)",
                       "Whatchu Thought (prod. perc40)",
                       "Feel Right (prod. 1oneam)",
                       "Keep Going, Zen (prod. 1oneam)",
             ],
         },
         {
             "title": "One Death",
             "kind": "Deluxe",          # Album / EP / Mixtape
             "year": "October 11, 2024",
             "cover": "1oneam - One Death.jpg",              # file name inside images/
	         "url": "https://music.youtube.com/playlist?list=OLAK5uy_lL94xSVKRZjmbngxO93zWVZjeDDCsKM-w",
             "tracks": [
                       "Facetime (prod. 1oneam)",
	                   "Alicia Keys (prod. tdf)",
	                   "No Lies (prod. skai)",
                       "I Got (prod. perc40, skai)",
                       "Coraline (prod. 1oneam)",
	                   "Celebrate (prod. 1oneam)",
	                   "Top Dog (prod. Clams Casino, 1oneam)",
                       "Death of Me (prod. 1oneam)",
             ],
         },
         {
             "title": "Sin Ever After",
             "kind": "Album",          # Album / EP / Mixtape
             "year": "October 24, 2025",
             "cover": "1oneam - Sin Ever After.jpg",              # file name inside images/
	         "url": "https://soundcloud.com/xx1oneam/sets/sin-ever-after",
             "tracks": [
                       "Tags (prod. tdf)",
	                   "Marriott (prod. Lucid, 1oneam)",
	                   "Stuck To Him (prod. tdf)",
                       "Up To Something (prod. 1oneam)",
                       "I Can Fly (prod. 1oneam)",
	                   "Outside (prod. tdf)",
	                   "Match My Vibe (prod. perc40)",
                       "Who am I? (prod. tdf)",
                       "Cloud 9 (prod. tdf)",
                       "Golden Token (prod. tdf)",
                       "Just Like Me (prod. tdf)",
                       "Understand Me (prod. tdf)",
                       "Let It Go (prod. gyro)",
                       "Fuck The Talk (prod. tdf)",
                       "Call Me (prod. tdf)",
                       "Aint My Life (prod. 1oneam)",
                       "Did You Mean It? (prod. 1oneam)",
                       "No New Friends (prod. tdf)",
                       "Calm B4 Storm (Bonus) (prod. gyro)",
             ],
         },
         {
             "title": "Sin +",
             "kind": "Deluxe",          # Album / EP / Mixtape
             "year": "December 3, 2025",
             "cover": "1oneam - Sin.jpg",              # file name inside images/
	         "url": "https://music.youtube.com/playlist?list=OLAK5uy_kgpIUKIXdgGgdllJlUivIeQdaxAyTiId0",
             "tracks": [
                       "agent 47 (prod. azure, 1oneam)",
	                   "lifestyle / how can you (prod. 1oneam)",
	                   "5G (prod. MISOGI)",
                       "everyday (prod. BrentRambo)",
                       "make her dance (prod. skai)",
	                   "petrol (prod. BrentRambo)",
	                   "chainsmoker (prod. gyro)",
                       "hope you know (prod. 1oneam)",
                       "who is you (prod. 1oneam)",
             ],
         },
         {
             "title": "winter",
             "kind": "Single",          # Album / EP / Mixtape
             "year": "November 17, 2021",
             "cover": "1oneam - winter.png",              # file name inside images/
	         "url": "https://music.youtube.com/playlist?list=OLAK5uy_naYEsuCp2FbFGaiz4tU7jK02qzJwDralc",
             "tracks": [
                       "favors (prod. Elipropperr)",
	                   "déjà vu (prod. boost, theo)",
	                   "so what (prod. tdf)",
             ],
         },
         {
             "title": "winter II",
             "kind": "EP",          # Album / EP / Mixtape
             "year": "December 30, 2022",
             "cover": "1oneam - winter II.jpg",              # file name inside images/
	         "url": "https://music.youtube.com/playlist?list=OLAK5uy_ms6igAFa1kUh0TtVeGZkt3DFnmkCJmibI",
             "tracks": [
                       "Lies (prod. perc40)",
	                   "Face Off (prod. perc40)",
	                   "Enough (prod. tdf)",
                       "Clear (prod. AltoSGP)",
                       "Confusing (prod. perc40)",
             ],
         },

     ],
     "singles": [
         {
             "title": "dream (prod. tdf)",
             "year": "February 18, 2021",
             "cover": "1oneam - dream.jpg",
             "url": "https://soundcloud.com/ponldp/1oneam-dream",
         },
         {
             "title": "nerves (prod. perc40, Jake Hansen, fakekickin)",
             "year": "April 9, 2022",
             "cover": "1oneam - nerves.jpg",
             "url": "https://soundcloud.com/xx1oneam/nerves",
         },
         {
             "title": "blessed (feat. Okaymar) (prod. perc40)",
             "year": "May 7, 2022",
             "cover": "1oneam - blessed.jpg",
             "url": "https://soundcloud.com/xx1oneam/blessed-ft-okaymar-perc40",
         },
         {
             "title": "ten (prod. perc40)",
             "year": "May 2, 2022",
             "cover": "1oneam - ten.jpg",
             "url": "https://soundcloud.com/xx1oneam/ten-perc40",
         },
         {
             "title": "stealth (prod. Jake Hansen)",
             "year": "June 13, 2022",
             "cover": "1oneam - stealth.jpg",
             "url": "https://soundcloud.com/xx1oneam/stealth-jake-hansen-1",
         },
         {
             "title": "all 4 you (prod. perc40)",
             "year": "July 26, 2022",
             "cover": "1oneam - all 4 you.jpg",
             "url": "https://soundcloud.com/xx1oneam/all-4-you-perc40",
         },
         {
             "title": "like yuh (prod. perc40)",
             "year": "December 4, 2022",
             "cover": "1oneam - like yuh.jpg",
             "url": "https://soundcloud.com/xx1oneam/like-yuh-perc40",
         },
         {
             "title": "G19 (feat. Okaymar, ohsxnta) (prod. perc40)",
             "year": "October 29, 2022",
             "cover": "1oneam - G19.jpg",
             "url": "https://soundcloud.com/xx1oneam/g19-ft-okaymar-ohsxnta-perc40",
         },
         {
             "title": "traits (prod. boolymon, OsamaSon, twovrt)",
             "year": "March 15, 2023",
             "cover": "1oneam - traits.jpg",
             "url": "https://soundcloud.com/xx1oneam/traits-boolymon-osamason",
         },
         {
             "title": "okay (prod. perc40)",
             "year": "June 9, 2023",
             "cover": "1oneam - okay.jpg",
             "url": "https://soundcloud.com/xx1oneam/okay-perc40",
         },
         {
             "title": "film (prod. tdf)",
             "year": "July 28, 2023",
             "cover": "1oneam - film.jpg",
             "url": "https://soundcloud.com/xx1oneam/film-tdf",
         },
         {
             "title": "function (prod. tdf)",
             "year": "September 15, 2023",
             "cover": "1oneam - function.jpg",
             "url": "https://soundcloud.com/xx1oneam/function-tdf",
         },
         {
             "title": "hunnid hunnid (prod. 1oneam)",
             "year": "January 19, 2024",
             "cover": "1oneam - hunnid hunnid.jpg",
             "url": "https://soundcloud.com/xx1oneam/hunnid-hunnid-1",
         },
         {
             "title": "Foreign (prod. ok)",
             "year": "February 23, 2024",
             "cover": "1oneam - Foreign.jpg",
             "url": "https://soundcloud.com/xx1oneam/foreign",
         },
         {
             "title": "wym? (prod. skai)",
             "year": "April 5, 2024",
             "cover": "1oneam - Wym.jpg",
             "url": "https://soundcloud.com/xx1oneam/wym",
         },
         {
             "title": "Vogue (prod. 1oneam)",
             "year": "August 23, 2024",
             "cover": "1oneam - Vogue.jpg",
             "url": "https://soundcloud.com/xx1oneam/vogue",
         },
         {
             "title": "Penthouse (prod. 1oneam)",
             "year": "January 10, 2025",
             "cover": "1oneam - Penthouse.jpg",
             "url": "https://soundcloud.com/xx1oneam/penthouse",
         },
         {
             "title": "luv this feeling (prod. 1oneam)",
             "year": "March 21, 2025",
             "cover": "1oneam - luv this feeling.jpg",
             "url": "https://soundcloud.com/xx1oneam/luv-this-feeling",
         },
         {
             "title": "lotta time (prod. CXO)",
             "year": "July 15, 2025",
             "cover": "1oneam - lotta time.jpg",
             "url": "https://soundcloud.com/xx1oneam/lotta-time",
         },
         {
             "title": "let me out (prod. 1oneam)",
             "year": "July 17, 2026",
             "cover": "1oneam - let me out.jpg",
             "url": "https://soundcloud.com/xx1oneam/let-me-out",
         },
         
     ],
 },
 {
     "name": "wildkarduno",
     "image": "wildkarduno.gif",                      # file name inside images/
     "aliases": ["6servin", "x06", "baby evil",],                    # ["Other Name", "Old Tag"]
     "dob": "April 12, 2003",                        # "1996-03-04" or "March 4, 1996"
     "collectives": "Slime Krew",
     "links": {
         "spotify": "https://open.spotify.com/artist/0eHJOmR3T0Q3vd8uWd82sk",
         "youtube_music": "https://music.youtube.com/channel/UCFFIh1TdkyEhPdOHzD-A9rg",
         "soundcloud": "https://soundcloud.com/wildkarduno",
     },
     "projects": [
         {
             "title": "Triple 5 Lifestyle",
             "kind": "Album",          # Album / EP / Mixtape
             "year": "June 24, 2022",
             "cover": "wildkarduno - Triple 5 Lifestyle.jpg",              # file name inside images/
	         "url": "https://music.youtube.com/playlist?list=OLAK5uy_nrGzMR3NoWJLK3IjDpNEGXCsER4LEGlcI",
             "tracks": [
                       "Feeling Okay (prod. ILuvKam)",
	                   "448 Whoa's (prod. SouljaSpirits)",
	                   "Bread On My Head (feat. Glokk40Spaz) (prod. Percshawty)",
                       "Free K9 (prod. SouljaSpirits, Rockyy Thugn)",
                       "No Dissin (prod. ILuvKam)",
	                   "Redeye (feat. Sluttyxhris)",
	                   "5Wrld (prod. twentywrld)",
             ],
         },
         {
             "title": "Baby Evil Vol. 2",
             "kind": "Mixtape",          # Album / EP / Mixtape
             "year": "October 6, 2023",
             "cover": "wildkarduno - Baby Evil Vol 2.jpg",              # file name inside images/
	         "url": "https://music.youtube.com/playlist?list=OLAK5uy_l7Nbs7hRp4MFnQvqioD-6qo4geDS22OX4",
             "tracks": [
                       "Beam (prod. SenseiATL)",
	                   "It Equal (prod. Thrty, twovrt)",
	                   "Already Done It (prod. SenseiATL)",
                       "Take Sum (prod. SenseiATL)",
                       "U Dont Kno (prod. Glokay)",
	                   "Kay Flock (prod. tdf)",
	                   "Erase (prod. tdf)",
                       "Goin 4 Nun (prod. SenseiATL)",
                       "Beef Bout a Hoe (prod. Swvsh)",
             ],
         },
         {
             "title": "Still Healing",
             "kind": "Mixtape",          # Album / EP / Mixtape
             "year": "January 2, 2024",
             "cover": "wildkarduno - Still Healing.jpg",              # file name inside images/
	         "url": "https://music.youtube.com/playlist?list=OLAK5uy_mUHPQkw4aEudpA-7fUunt9U1_LKCUot0k",
             "tracks": [
                       "The Voice (prod. WhyCeg)",
	                   "BlockBoy (prod. SenseiATL)",
	                   "Interrogation Room (prod. HariRoc)",
                       "Choose my Fate (prod. tdf)",
                       "Chosen (prod. Percshawty)",
	                   "Conversations with Baby Evil (prod. SenseiATL)",
	                   "Still Healing (prod. WhyCeg)",
                       "Roxk Out 2 (prod. SenseiATL)",
                       "Eastside Story (prod. SenseiATL)",
                       "Don't Check In (prod. SenseiATL)",
                       "Draw the Line (prod. boolymon, SenseiATL, Marrgielaa)",
                       "Fuck You Pay Me (prod. SenseiATL)",
                       "Shawty Lo (prod. SenseiATL)",
                       "New Flame (prod. SenseiATL)",
                       "Play no Games (prod. SenseiATL)",
             ],
         },
         {
             "title": "Evil Hero",
             "kind": "Album",          # Album / EP / Mixtape
             "year": "July 31, 2024",
             "cover": "wildkarduno - Evil Hero.jpg",              # file name inside images/
	         "url": "https://music.youtube.com/playlist?list=OLAK5uy_kbYtLhAyUWxnI_S5r7cvl_GOwa6ClF8jg",
             "tracks": [
                       "Rookie (prod. Hoodrixh)",
	                   "Listen (prod. SenseiATL)",
	                   "Right Path (prod. Four3va, Swishrr)",
                       "Believin (prod. SenseiATL)",
                       "Old Gucci (prod. Hoodrixh)",
	                   "Watxh Yo Shoes (prod. Notharom)",
	                   "Not Feelin It (prod. 444jet)",
                       "Be A Sign (prod. Kankan, XanGang)",
                       "Stendo (prod. Vonperp)",
                       "Dstnd (prod. Notharom)",
             ],
         },
         {
             "title": "Reminiscing",
             "kind": "Album",          # Album / EP / Mixtape
             "year": "May 8, 2025",
             "cover": "wildkarduno - Reminiscing.jpg",              # file name inside images/
	         "url": "https://music.youtube.com/playlist?list=OLAK5uy_kpCxTlzfMF6xR0JQIE92jYZUBFnI0Fovg",
             "tracks": [
                       "hella pain in my eyes (prod. Marrgielaa, PurpTokyo)",
	                   "The Truth (prod. tdf)",
	                   "fox 2 (prod. tdf)",
                       "rlly scary (prod. Al Chapo)",
                       "Yow (prod. boolymon, Thrty)",
	                   "Hella Hammers (prod. Thrty)",
	                   "No Mask (prod. Yakree)",
                       "Dat (prod. Yakree, Prod. Slayer)",
                       "Witch (prod. Jdolla, Yakree)",
                       "I Kan Vision My Time Komin (prod. Dezeiioun)",
                       "Kaveman 5 (prod. Marrgielaa, boolymon)",
                       "not a demon 555 (prod. boolymon, Marrgielaa)",
             ],
         },
         {
             "title": "9 Life",
             "kind": "Album",          
             "year": "May 23, 2025",
             "cover": "wildkarduno - 9 Life.jpg",              
	         "url": "https://music.youtube.com/playlist?list=OLAK5uy_nnBfH5zvEe44LJqaWEO4hhimhN53Tg-Ro",
             "tracks": [
                       "Not Goin (prod. Bakkwoods)",
	                   "Preacher (prod. Fish$cale)",
	                   "Real Deal Za (prod. Fish$cale, Shoon)",
                       "Seeing Signs (prod. Fish$cale)",
                       "AK-47 (prod. 19thou)",
	                   "Diamond Back (prod. HariRoc)",
	                   "From Da Jump (prod. Four3va)",
                       "Renegade (prod. reincarnation!)",
                       "Revenge (prod. HariRoc)",
                       "Man In Da Middle (prod. Fish$cale)",
                       "9 Lives (prod. Vonperp)",
                       "Outside (prod. Rok)",
             ],
         },
         {
             "title": "Ascension",
             "kind": "Album",          
             "year": "July 30, 2026",
             "cover": "wildkarduno - Ascension.jpg",              
	         "url": "https://music.youtube.com/playlist?list=OLAK5uy_m_OjhXXCmqaO2vO1wXVM17TM3NJX9jEYg",
             "tracks": [
                       "Mike Vick (prod. yrsci, congressofbando)",
	                   "Bleed4Me ! (prod. yrsci)",
	                   "Demonia (prod. 20MOP, yrsci)",
                       "5 Promises (prod. numeroneuf)",
                       "RedRum (prod. BenjiCold, 406ahmad)",
	                   "DOA (prod. ivvys, yrsci)",
	                   "Jus Hoop (prod. BenjiCold)",
                       "Joker (prod. Duncxn, KRAGER, jellomvsic)",
                       "12 Kant Stop Shit (prod. exset)",
                       "Obsession (prod. tdf)",
             ],
         },


     ],
     "singles": [
         {
             "title": "xoolin. (prod. boolymon)",
             "year": "May 21, 2022",
             "cover": "wildkarduno - Xoolin.jpg",
             "url": "https://soundcloud.com/wildkarduno/xoolin",
         },
         {
             "title": "555/STIXKY! (prod. boolymon)",
             "year": "March 24, 2022",
             "cover": "wildkarduno - Stixky.jpg",
             "url": "https://soundcloud.com/nijakaske/wildkarduno-okaymar-555stixky-boolymon",
         },
         {
             "title": "Keep a Pole/Knaxk",
             "year": "July 28, 2022",
             "cover": "wildkarduno - Keep a Pole.jpg",
             "url": "https://soundcloud.com/wildkarduno/keep-a-pole-knaxk",
         },
         {
             "title": "switxhes 2 (feat. 1oneam, Lawsy, ohsxnta) (prod. ILuvKam)",
             "year": "August 12, 2022",
             "cover": "wildkarduno - switxhes 2.jpg",
             "url": "https://soundcloud.com/wildkarduno/switxhes2",
         },
         {
             "title": "heart gone (prod. perc40)",
             "year": "September 14, 2022",
             "cover": "wildkarduno - heart gone.jpg",
             "url": "https://soundcloud.com/wildkarduno/heart-gone-perc40",
         },
         {
             "title": "i dont give a fuxk bout da 808s (prod. perc40, utrippin!)",
             "year": "February 6, 2023",
             "cover": "wildkarduno - i dont give a fuxk bout da 808s.jpg",
             "url": "https://soundcloud.com/wildkarduno/i-dont-give-a-fuxk-bout-da",
             "music_video": "https://www.youtube.com/watch?v=k8NKHwHpUm8",
         },
         
     ],
 },
 
 {
     "name": "1300SAINT",
     "image": "1300SAINT.gif",                      # file name inside images/
     "aliases": ["",],                    # ["Other Name", "Old Tag"]
     "dob": "April 24, 2004",                        # "1996-03-04" or "March 4, 1996"
     "links": {
         "spotify": "https://open.spotify.com/artist/40VzC4fLTuY4YWFwKXK4Cv",
         "youtube_music": "https://music.youtube.com/channel/UCFr1pnVIF_9XopwQLqVahBw",
         "soundcloud": "https://soundcloud.com/1300saint",
     },
     "projects": [
         {
             "title": "NOIR",
             "kind": "Album",          # Album / EP / Mixtape
             "year": "December 16, 2022",
             "cover": "1300SAINT - NOIR.jpg",              # file name inside images/
	         "url": "https://music.youtube.com/playlist?list=OLAK5uy_lIVRjDwik00ri8kalgCUbwHDdOj_YluzQ",
             "tracks": [
                       "5% TINT",
	                   "FLASHING CAMERAS",
	                   "LIKE ME",
                       "CHROME CROSS (feat. Southsidesilhouette) (prod. prodbypatrick)",
                       "SERENE",
	                   "IN REVERSE",
	                   "@NIGHT",
                       "HI N LO",
                       "LUV = GUN",
                       "BREATHE IN (prod. KAI H)",
                       "ME MYSELF & I",
                       "GONE",
                       "MAN OF THE YEAR",
             ],
         },
         {
             "title": "fleshwound",
             "kind": "Single",          # Album / EP / Mixtape
             "year": "January 23, 2023",
             "cover": "1300SAINT - fleshwound.jpg",              # file name inside images/
	         "url": "https://music.youtube.com/playlist?list=OLAK5uy_m5KHT45hgxi4vsusxHPEGXdv-IGW9O9qA",
             "tracks": [
                       "face (prod. armaan)",
	                   "take me there (prod. armaan)",
             ],
         },
         {
             "title": "untitled 01",
             "kind": "Single",          # Album / EP / Mixtape
             "year": "May 2, 2023",
             "cover": "1300SAINT - untitled 01.jpg",              # file name inside images/
	         "url": "https://music.youtube.com/playlist?list=OLAK5uy_kz4d-Q1HkXF0aujgG01p2KM79XJ4EY7Pg",
             "tracks": [
                       "plenty (prod. armaan)",
	                   "god's hands (prod. armaan)",
             ],
         },
         {
             "title": "untitled 02",
             "kind": "Single",          # Album / EP / Mixtape
             "year": "August 17, 2023",
             "cover": "1300SAINT - untitled 02.jpg",              # file name inside images/
	         "url": "https://music.youtube.com/playlist?list=OLAK5uy_mpN_updmi-L80hCxUnuwfr_DRLqwVqmCo",
             "tracks": [
                       "throne (prod. armaan)",
	                   "@'em (prod. armaan)",
             ],
         },
         {
             "title": "+++",
             "kind": "Single",          # Album / EP / Mixtape
             "year": "August 28, 2023",
             "cover": "1300SAINT - +++.jpg",              # file name inside images/
	         "url": "https://music.youtube.com/playlist?list=OLAK5uy_mDqxVU4GEjvB9EP1AQb1MBhWtKOVl2IJs",
             "tracks": [
                       "centerfold (prod. Blais Mauger, Brood)",
	                   "yesterdays",
             ],
         },
         {
             "title": "SEDUCE & DESTROY",
             "kind": "EP",          # Album / EP / Mixtape
             "year": "September 30, 2023",
             "cover": "1300SAINT - SEDUCE & DESTROY.jpg",              # file name inside images/
	         "url": "https://music.youtube.com/playlist?list=OLAK5uy_nuU4sl1mR-dfJDCcXUKldVpss4wWZ7Y-s",
             "tracks": [
                       "DYING BREED (prod. armaan, shynemoonlight)",
	                   "ONE (prod. 1lvcxs)",
	                   "PRAY 4 ME (prod. 1lvcxs, ReidMD)",
                       "TO DIE FOR (prod. 1lvcxs, PortalStorms)",
                       "BLISS (prod. Seditionry, AnotherVGN)",
	                   "MERCY (prod. untitled)",
             ],
         },
         {
             "title": "PURE AUDIO",
             "kind": "EP",          # Album / EP / Mixtape
             "year": "February 7, 2025",
             "cover": "1300SAINT - PURE AUDIO.jpg",              # file name inside images/
	         "url": "https://music.youtube.com/playlist?list=OLAK5uy_lT6inydFf0zMYqvsE9fuLrD6zu9EmevxQ",
             "tracks": [
                       "TRUST NOBODY (prod. revisitingearth)",
	                   "ALMIGHTY (feat. Yung Kayo) (prod. Jordan Payne)",
	                   "DECEASED (NO WAY) (prod. PROJECT4PLAY)",
                       "JUST WOKE UP (prod. James Fargo.)",
                       "BABYFACE (prod. Onetimee, hanjoo)",
	                   "IF I DIE (prod. prodluke)",
             ],
         },
         {
             "title": "SAINT SEASON",
             "kind": "EP",          # Album / EP / Mixtape
             "year": "April 25, 2025",
             "cover": "1300SAINT - SAINT SEASON.jpg",              # file name inside images/
	         "url": "https://music.youtube.com/playlist?list=OLAK5uy_mBMVkKDa4pZzf8kpZYBDizVGSIyyjP6Lg",
             "tracks": [
                       "REDROBIN (prod. Peeb, Jesse Morris, Alexete)",
	                   "IN TROUBLE (feat. Nine Vicious) (prod. PROJECT4PLAY, RAFMADE)",
	                   "SHOGUN (prod. Onetimee, prodluke, ProducedByHassan)",
                       "SEEUMSAYIN (prod. Peeb, Jesse Morris)",
                       "BLAKK TRUKK (feat. Nine Vicious) (prod. prodluke, Onetimee)",
	                   "SOUTHSIDE FOREVER (prod. London on da Track, BeatsByJuko, Keymajor)",
	                   "SHUT UP (feat. SahBabii, Young Thug) (prod. CashMoneyAP)",
             ],
         },
         {
             "title": "NewDrug.",
             "kind": "Album",          # Album / EP / Mixtape
             "year": "August 15, 2025",
             "cover": "1300SAINT - NewDrug.jpg",              # file name inside images/
	         "url": "https://music.youtube.com/playlist?list=OLAK5uy_luIOZQKDwwDjp3N84iLGCd-2d43OgsWMY",
             "tracks": [
                       "Worry Bout Yours. (prod. pleasures, hanjoo)",
	                   "BloodSucker (prod. T9C, Austen Vance)",
	                   "Set. (feat. Sk8star, Diorvsyou, ApolloRed1)",
                       "Kutta. (prod. Onetimee, prodluke)",
                       "Not @ All. (prod. Peeb, Jesse Morris, Sett 7v)",
	                   "Pray2TheLord. (prod. Deadboybrio)",
             ],
         },
         {
             "title": "ALL HAIL",
             "kind": "Album",          # Album / EP / Mixtape
             "year": "February 28, 2025",
             "cover": "1300SAINT - ALL HAIL.jpg",              # file name inside images/
	         "url": "https://music.youtube.com/playlist?list=OLAK5uy_lRIAP9zu5C2LAl2G4Fi3XtvrAHNFuwdLk",
             "tracks": [
                       "NEVER THEM INTRO (prod. James Fargo., armaan)",
	                   "VENOM (prod. Noir1070, Austen Vance, armaan)",
	                   "I SEE RED (prod. Onetimee, prodluke)",
                       "OUT BAD (prod. Jwade, revisitingearth)",
                       "LCKY NMBR 7 (prod. Deadboybrio, Esse, daniia, armaan)",
	                   "EVERYTHING SLATT (prod. PROJECT4PLAY, eli.yf, armaan)",
	                   "LIFE OF A DON (prod. 3rdPerson, pleasures, untitled, Onetimee, armaan)",
                       "THUG INTERLUDE (feat. Young Thug) (prod. Onetimee)",
                       "SAFE & SOUND (prod. James Fargo., Darkboy Santana, armaan)",
                       "GALLERY (prod. Onetimee, Mxthew, armaan)",
                       "BTTR & BTTR (prod. KAI H, Jordan Payne)",
                       "CAYENNE (prod. Onetimee, pleasures)",
                       "SUNSEX (prod. Teenrcer, armaan)",
                       "THE WORLD IS YOURS (prod. James Fargo., armaan)",
             ],
         },
         {
             "title": "SAVIOR",
             "kind": "Album",          # Album / EP / Mixtape
             "year": "November 21, 2025",
             "cover": "1300SAINT - SAVIOR.jpg",              # file name inside images/
	         "url": "https://music.youtube.com/playlist?list=OLAK5uy_mdLwdDGUi7lcR2NE-Yg9t-Xz-gQpDEUP8",
             "tracks": [
                       "BIGGER THAN LIFE (prod. Synthetic, Noah Mejia, Venny, armaan)",
	                   "KYOTO (prod. Austen Vance, elijahgeeked)",
	                   "STOP PLAYIN (prod. Kferno)",
                       "SLITHERIN (prod. Austen Vance, armaan)",
                       "RIP POPE (feat. Lil Gotit) (prod. Onetimee)",
	                   "HEARD IT ALL (prod. Onetimee, YOUNGERNEXTLIFE, armaan)",
	                   "DIVINE (prod. Onetimee, Vertigo, armaan)",
                       "MONA LISA (prod. Austen Vance, armaan)",
                       "PALM SPRINGS (prod. Onetimee, Vertigo, armaan)",
                       "SLIMIER > YOU (prod. Onetimee)",
                       "BOUNTY (prod. Onetimee, 1miicah, armaan)",
                       "SOULTIES (prod. Peeb, Sett 7v, Onetimee, armaan)",
                       "CHAINZ & CORVETTEZ (feat. Yung Heir) (prod. Onetimee, prodluke, armaan)",
                       "FLAWS (prod. Peeb, armaan, Shlappy, Jakik)",
                       "RETURN YOU (prod. Noah Mejia, Nico Baran, armaan, Blaztii)",
                       "INTERLUDE (prod. Bhristo, Onetimee, armaan, KWAKZ)",
                       "SAVIOR SOLITUDE (prod. 1300SAINT, Bhristo, KWAKZ)",
             ],
         },
         {
             "title": "SAVIOR: +++",
             "kind": "Deluxe",          # Album / EP / Mixtape
             "year": "March 6, 2026",
             "cover": "1300SAINT - SAVIOR +++.jpg",              # file name inside images/
	         "url": "https://music.youtube.com/playlist?list=OLAK5uy_mk0rA7Fvi-RfOMHR6PtHeqKk8UQqJ1yOc",
             "tracks": [
                       "MILITIA BOSS (prod. shynemoonlight, Jordan Payne)",
	                   "BLONDE P*NK (prod. Jordan Payne)",
	                   "MAMI (prod. Nine Vicious, Onetimee, Sett 7v)",
                       "WHITE OPS (prod. skiicreated)",
                       "PANDEMONIUM (prod. Jordan Payne)",
	                   "I NEED (feat. Sk8star) (prod. Onetimee, armaan)",
	                   "PRETTY PU$$Y (prod. skiicreated)",
                       "LOADOUT (HIT) (feat. ApolloRed1) (prod. Jordan Payne)",
                       "EA (feat. Nine Vicious) (prod. Onetimee, prodluke)",
                       "SHELLS (prod. Ayelavish!, armaan)",
                       "LIFETIME (prod. 406ahmad)",
                       "BIGGER THAN LIFE (prod. Synthetic, Noah Mejia, Venny, armaan)",
	                   "KYOTO (prod. Austen Vance, elijahgeeked)",
	                   "STOP PLAYIN (prod. Kferno)",
                       "SLITHERIN (prod. Austen Vance, armaan)",
                       "RIP POPE (feat. Lil Gotit) (prod. Onetimee)",
	                   "HEARD IT ALL (prod. Onetimee, YOUNGERNEXTLIFE, armaan)",
	                   "DIVINE (prod. Onetimee, Vertigo, armaan)",
                       "MONA LISA (prod. Austen Vance, armaan)",
                       "PALM SPRINGS (prod. Onetimee, Vertigo, armaan)",
                       "SLIMIER > YOU (prod. Onetimee)",
                       "BOUNTY (prod. Onetimee, 1miicah, armaan)",
                       "SOULTIES (prod. Peeb, Sett 7v, Onetimee, armaan)",
                       "CHAINZ & CORVETTEZ (feat. Yung Heir) (prod. Onetimee, prodluke, armaan)",
                       "FLAWS (prod. Peeb, armaan, Shlappy, Jakik)",
                       "RETURN YOU (prod. Noah Mejia, Nico Baran, armaan, Blaztii)",
                       "INTERLUDE (prod. Bhristo, Onetimee, armaan, KWAKZ)",
                       "SAVIOR SOLITUDE (prod. 1300SAINT, Bhristo, KWAKZ)",                       
             ],
         },

     ],
     "singles": [
         {
             "title": "4U (prod. shynemoonlight)",
             "year": "February 23, 2023",
             "cover": "1300SAINT - 4U.jpg",
             "url": "https://soundcloud.com/1300saint/4you",
         },
         {
             "title": "own way (prod. opi1k, shynemoonlight)",
             "year": "July 16, 2023",
             "cover": "1300SAINT - own way.jpg",
             "url": "https://soundcloud.com/1300saint/own-way-opi1k-x-shyne-mix-1",
         },
         {
             "title": "thrax (prod. jordanpayne)",
             "year": "August 5, 2023",
             "cover": "1300SAINT - thrax.jpg",
             "url": "https://soundcloud.com/1300saint/thrax",
         },
         {
             "title": "so long, and farewell (prod. revisitingearth)",
             "year": "November 17, 2023",
             "cover": "1300SAINT - so long, and farewell.jpg",
             "url": "https://soundcloud.com/1300saint/so-long-and-farewell",
         },
         {
             "title": "Thread (prod. Patrick)",
             "year": "December 21, 2023",
             "cover": "1300SAINT - Thread.jpg",
             "url": "https://soundcloud.com/1300saint/thread-prod-patrick",
         },
         {
             "title": "fallout (prod. Saint Rose, prod.ivi)",
             "year": "February 6, 2024",
             "cover": "1300SAINT - fallout.jpg",
             "url": "http://soundcloud.com/1300saint/fallout",
         },
         {
             "title": "don't lie to me (prod. Hitech)",
             "year": "March 3, 2024",
             "cover": "1300SAINT - don't lie to me.jpg",
             "url": "https://soundcloud.com/1300saint/dont_lie_to_me-mp3",
         },
         {
             "title": "Escalade (prod. Zackary Arthur, cabernett, pleasures)",
             "year": "September 6, 2024",
             "cover": "1300SAINT - Escalade.jpg",
             "url": "https://soundcloud.com/1300saint/escalade",
         },
         {
             "title": "Worth It (prod. Hitech, 3rdPerson)",
             "year": "October 18, 2024",
             "cover": "1300SAINT - Worth It.jpg",
             "url": "https://soundcloud.com/1300saint/worth-it",
         },
         {
             "title": "United (prod. armaan, v12nico, brood.esque)",
             "year": "December 4, 2024",
             "cover": "1300SAINT - United.jpg",
             "url": "https://soundcloud.com/1300saint/united",
         },
         {
             "title": "OH K (prod. Davonum)",
             "year": "January 10, 2025",
             "cover": "1300SAINT - OH K.jpg",
             "url": "https://soundcloud.com/1300saint/oh-k",
         },
         {
             "title": "NOT A TELFAR (prod. Onetimee, hanjoo)",
             "year": "April 5, 2025",
             "cover": "1300SAINT - NOT A TELFAR.jpg",
             "url": "https://soundcloud.com/1300saint/nat",
         },
         {
             "title": "Bazo (prod. Bhristo, revisitingearth)",
             "year": "June 13, 2025",
             "cover": "1300SAINT - Bazo.jpg",
             "url": "https://soundcloud.com/1300saint/bazo-1",
         },
         {
             "title": "#FKITWEBALL (prod. Goxan, Skello)",
             "year": "August 8, 2025",
             "cover": "1300SAINT - FKITWEBALL.jpg",
             "url": "https://soundcloud.com/1300saint/fkitweball",
             "music_video": "https://www.youtube.com/watch?v=J1Zp9xe4t7c",
         },
         {
             "title": "MOLLY (prod. Richie Souf, cashheart)",
             "year": "May 22, 2026",
             "cover": "1300SAINT - MOLLY.jpg",
             "url": "https://soundcloud.com/1300saint/molly",
         },
         
     ],
 },
 {
     "name": "diamond*",
     "image": "diamond.jpg",                      
     "aliases": ["", "", "", "", ""],                    
     "dob": "July 2, 1998",
     "collectives": "ØWAY",
     "links": {
         "spotify": "https://open.spotify.com/artist/2U3bFzN7xGOhqdATusepqC",
         "youtube_music": "https://music.youtube.com/@dimantvvs",
         "soundcloud": "https://soundcloud.com/diamond-554292457",
     },
     "projects": [
         {
             "title": "nØ idØls",
             "kind": "Album",          
             "year": "July 4, 2025",
             "cover": "diamond - no idols.jpg",              
	         "url": "https://music.youtube.com/playlist?list=OLAK5uy_mpKwyzYISEFV-6stjRh876dLVFbJcGch8",
             "tracks": [
                       "angels cry (prod. teenslug)",
	                   "frØzen (prod. teenslug)",
	                   "twin flame (prod. bbmevis)",
                       "1stØp shØp (prod. teenslug, Percaso)",
                       "bada bing, bada bØØm (feat. Tezzus) (prod. Kassgocrazy, Rochambeau)",
	                   "brainstØrm (prod. Nate Varter)",
	                   "skys the limit (prod. bbmevis)",
                       "pØle dance",
                       "internet bae (prod. Nate Varter)",
                       "gucci sØcks",
                       "grace! (prod. teenslug)",
                       "CARMELØ (prod. PROJECT4PLAY)",
                       "extraterrestrial (prod. Zaydntdoit)",
             ],
         },
         {
             "title": "BLING SLIME VØL 1: HØSTED BY DJ HØLIDAY",
             "kind": "Mixtape",          
             "year": "July 8, 2026",
             "cover": "diamond - BLING SLIME VOL 1.jpg",              
	         "url": "https://music.youtube.com/playlist?list=OLAK5uy_nFVmLU-nG_xnAarziNA4xyyLLUo12Eses",
             "tracks": [
                       "MAN ØN THE MØØN (prod. Nate Varter)",
	                   "ALMIGHTY DØLLA (prod. 90lumiere)",
	                   "WYD2 (prod. thr6x, Zaan)",
                       "FØURS (feat. Young Thug) (prod. Brav06, chinoo.xo)",
                       "HEDIS N PELLES (feat. Pz') (prod. Bhristo, Luc1us, Kat Lightning)",
	                   "GG (prod. Tyekoo)",
	                   "HØRSEBIT (feat. Lil Righteous) (prod. Funkay, Phil)",
                       "3 WISHES (feat. Sk8star) (prod. godfoggy, Philippe Goudiaby)",
                       "STFU (prod. Tyekoo)",
                       "BURGERS N FRIES (feat. Southsidesilhouette)",
                       "MATTER ØF TIME (prod. Zaydntdoit)",
             ],
         },
         {
             "title": "The Beauty of It:)",
             "kind": "EP",          
             "year": "October 18, 2019",
             "cover": "diamond - The Beauty of It.jpg",              
	         "url": "https://music.youtube.com/playlist?list=OLAK5uy_n5fE5-ivOQAJ6nxxGw2C7xPiLC5P5EvII",
             "tracks": [
                       "Divine (prod. KriticalHit)",
	                   "Anxiety",
	                   "Blondie",
                       "Red Wine",
                       "Unicorn Gab",
             ],
         },
         {
             "title": "diamants sur sa chatte",
             "kind": "EP",          
             "year": "January 9, 2024",
             "cover": "diamond - diamants sur sa chatte.jpg",              
	         "url": "https://music.youtube.com/playlist?list=OLAK5uy_nWw_jyrgv0Y2nnLht4dN1E5yJ7ExFf1ug",
             "tracks": [
                       "lambchops & blue cheese (prod. Zaan)",
	                   "sex in da A.M (prod. Nate Varter)",
	                   "i love pussy (prod. Nate Varter)",
                       "harley davidson (prod. Nate Varter)",
             ],
         },


     ],
     "singles": [
         {
             "title": "Øur daily bread! (prod. Zaan)",
             "year": "August 31, 2023",
             "cover": "diamond - our daily bread.jpg",
             "url": "https://soundcloud.com/diamond-554292457/our-daily-bread",
         },
         {
             "title": "rose (prod. light*DK)",
             "year": "September 14, 2023",
             "cover": "diamond - rose.jpg",
             "url": "https://soundcloud.com/diamond-554292457/rose-prod-light-dk",
             "music_video": "https://www.youtube.com/watch?v=PXroixR26Vc",
         },
         {
             "title": "xtra xtra (prod. Nate Varter)",
             "year": "September 24, 2023",
             "cover": "diamond - xtra xtra.jpg",
             "url": "https://soundcloud.com/diamond-554292457/xtra-xtra-x-nate-vater",
         },
         {
             "title": "testarossa (prod. Nate Varter)",
             "year": "September 24, 2023",
             "cover": "diamond - testarossa.jpg",
             "url": "https://soundcloud.com/diamond-554292457/testarossa-x-nate-varter",
         },
         {
             "title": "temptation (feat. Tezzus) (prod. diamond*)",
             "year": "October 9, 2023",
             "cover": "diamond - temptation.jpg",
             "url": "https://soundcloud.com/diamond-554292457/temptation-x-tezzus",
         },
         {
             "title": "imperial swagg (prod. Nate Varter)",
             "year": "October 21, 2023",
             "cover": "diamond - imperial swagg.jpg",
             "url": "https://soundcloud.com/diamond-554292457/imperial-swagg",
             "music_video": "https://www.youtube.com/watch?v=E01PQbh1kAU",
         },
         {
             "title": "kokaine karter",
             "year": "2023",
             "cover": "diamond - kokaine karter.jpg",
             "url": "https://music.youtube.com/playlist?list=OLAK5uy_kWPaP-RlI1wiJS-YM71L_2pa0s66yNgJw",
         },
         {
             "title": "KMD (prod. Nate Varter)",
             "year": "December 19, 2023",
             "cover": "diamond - KMD.jpg",
             "url": "https://soundcloud.com/diamond-554292457/kmd-x-nate-vater",
             "music_video": "https://www.youtube.com/watch?v=toivy5a74hE",
         },
         {
             "title": "prune juice! (prod. Zaan, medtover)",
             "year": "January 27, 2024",
             "cover": "diamond - prune juice.jpg",
             "url": "https://soundcloud.com/hafaae/diamond-prune-juice",
         },
         
     ],
 },
 
 {
     "name": "boolymon",
     "image": "boolymon.gif",                      # file name inside images/
     "aliases": ["snakechildpain"],                    # ["Other Name", "Old Tag"]
     "dob": "December 4, 2004",                        # "1996-03-04" or "March 4, 1996"
     "collectives": ["Slime Krew", "odd squad"],
     "links": {
         "spotify": "https://open.spotify.com/artist/0T4s3xc50BkYsAvK2tV9cd",
         "youtube_music": "https://music.youtube.com/channel/UCQ2rTYldl99SKlViMalUDqg",
         "soundcloud": "https://soundcloud.com/boolymon",
     },
     "projects": [
         {
             "title": "glove world",
             "kind": "Album",          # Album / EP / Mixtape
             "year": "June 2, 2026",
             "cover": "boolymon - glove world.jpg",              # file name inside images/
	         "url": "https://music.youtube.com/playlist?list=OLAK5uy_m4f6hWbmN-CtLQpoI7XbPtsKSVVfnY4eQ",
             "tracks": [
                       "Glove world (prod. dbglokk)",
	                   "Talking crazy (prod. dbglokk)",
	                   "Put em up (prod. dbglokk)",
                       "Ghost (prod. dbglokk)",
                       "Mike jack (prod. dbglokk)",
	                   "Smoking crack (prod. dbglokk)",
	                   "Doink (prod. dbglokk)",
                       "CTBTMLA (prod. dbglokk, Marrgielaa)",
             ],
         },
         {
             "title": "tony",
             "kind": "Album",          
             "year": "July 7, 2023",
             "cover": "boolymon - Tony.jpg",              
	         "url": "https://music.youtube.com/playlist?list=PL0d-M9h88inVwZD-sLYgXI0c-h4cApj36",
             "tracks": [
                       "wig (feat. OsamaSon) (prod. boolymon)",
	                   "hero (feat. Okaymar) (prod. boolymon, Thrty)",
	                   "for the team (feat. 1oneam) (prod. boolymon)",
                       "took da chance (feat. Smokingskul) (prod. boolymon)",
                       "kid (feat. wildkarduno) (prod. boolymon)",
	                   "greys anatomy (feat. ohsxnta) (prod. boolymon)",
	                   "dont trip (feat. squillo) (prod. boolymon)",
                       "get rekt (feat. 1oneam) (prod. boolymon)",
                       "slime you out (feat. OsamaSon) (prod. boolymon)",
                       "aesthetic 2 (feat. Smokingskul) (prod. boolymon, twovrt)",
                       "red (feat. OsamaSon) (prod. boolymon, perc40)",
                       "lesson (feat. wildkarduno) (prod. boolymon)",
                       "zaxbys (feat. ohsxnta, OsamaSon) (prod. boolymon, Thrty)",
                       "fun (feat. OsamaSon) (prod. boolymon, OsamaSon)",
                       "aunt berta (feat. Smokingskul, squillo) (prod. boolymon)",
             ],
         },

     ],
     "singles": [
         {
             "title": "distro got banned (prod. 1flave)",
             "year": "November 24, 2024",
             "cover": "boolymon - distro got banned.jpg",
             "url": "https://soundcloud.com/penguinsso/boolymon-distro-got-banned-1",
         },
         {
             "title": "think he dat guy (prod. Thrty)",
             "year": "December 29, 2023",
             "cover": "boolymon - think he dat guy.jpg",
             "url": "https://soundcloud.com/slimepointe/boolymon-think-he-dat-guy-prod",
         },
         {
             "title": "jaydes (prod. twovrt)",
             "year": "November 23, 2024",
             "cover": "boolymon - jaydes.jpg",
             "url": "https://soundcloud.com/twovrt/boolymon-jaydes-prod-twovrt",
         },
         {
             "title": "pain (prod. Afrixkan)",
             "year": "December 31, 2023",
             "cover": "boolymon - pain.jpg",
             "url": "https://soundcloud.com/cokencasinos/boolymon-pain",
         },
         {
             "title": "stupid ho (prod. twovrt)",
             "year": "October 9, 2024",
             "cover": "boolymon - stupid ho.jpg",
             "url": "https://soundcloud.com/twovrt/stupid-ho",
         },
         {
             "title": "crumbs (prod. joathxn, skipclzz)",
             "year": "December 7, 2024",
             "cover": "boolymon - crumbs.jpg",
             "url": "https://soundcloud.com/slimepointe/boolymon-crumbs-prod-fluffy",
         },
         {
             "title": "Not My Bro (prod. Wise)",
             "year": "December 8, 2024",
             "cover": "boolymon - Not My Bro.jpg",
             "url": "https://soundcloud.com/tubman-underground/boolymon-not-my-bro-prod-wise",
         },
         {
             "title": "hitting the folks (prod. ogkush420)",
             "year": "December 15, 2024",
             "cover": "boolymon - hitting the folks.jpg",
             "url": "https://soundcloud.com/localjunkie666/boolymon-hittng-the-folks",
         },
         {
             "title": "burn in hell (prod. twovrt)",
             "year": "December 23, 2024",
             "cover": "boolymon - burn in hell.jpg",
             "url": "https://soundcloud.com/twovrt/boolymon-burn-in-hell-prod",
         },
         
     ],
 },
 {
     "name": "Nine Vicious",
     "image": "Nine Vicious.gif",                      # file name inside images/
     "aliases": ["Baby Tino", "Lil Nine", "Lil Trey", "BabySpyda"],                    # ["Other Name", "Old Tag"]
     "dob": "July 15, 2002",                        # "1996-03-04" or "March 4, 1996"
     "links": {
         "spotify": "https://open.spotify.com/artist/6Rs7Ufqb4h0FTuVg6wlqOy",
         "youtube_music": "https://music.youtube.com/channel/UCrBhppZQ3tdXYTkMqOHYM7g",
         "soundcloud": "https://soundcloud.com/ninesomnia",
     },
     "projects": [
         {
             "title": "Studio Addict",
             "kind": "Mixtape",          # Album / EP / Mixtape
             "year": "December 13, 2024",
             "cover": "Nine Vicious - Studio Addict.jpg",              # file name inside images/
	         "url": "https://music.youtube.com/playlist?list=OLAK5uy_lELQtvyxsHMpq7BHypmGRqqwUhJe_o7KM",
             "tracks": [
                       "Studio Addict (prod. 406ahmad)",
	                   "Tokyo (prod. 406ahmad)",
	                   "F&N (prod. Nosaint, chxncex)",
                       "The Truth (prod. 406ahmad, Kal Pierce)",
                       "Los Angeles (prod. 406ahmad)",
	                   "Ye (prod. 406ahmad)",
	                   "Interlude (prod. revisitingearth)",
                       "One Beer (prod. 406ahmad)",
                       "Boom Bap (prod. 406ahmad)",
                       "Slide Aht (prod. Jwade, Nine Vicious)",
                       "Black Truck Talking (prod. Mightbejohn, Kagyu, Crackywyd)",
                       "Love Hurts (prod. 406ahmad)",
                       "Just Landed (prod. prodbypatrick, youknowozi)",
             ],
         },
         {
             "title": "Tumblr Music",
             "kind": "Album",          # Album / EP / Mixtape
             "year": "March 31, 2025",
             "cover": "Nine Vicious - Tumblr Music.jpg",              # file name inside images/
	         "url": "https://music.youtube.com/playlist?list=OLAK5uy_ma9F9UcdggOxVG_ZeprDEuhFAT2n2SfSA",
             "tracks": [
                       "Margiela Steppin (prod. 406ahmad)",
	                   "Makaveli (prod. prodbypatrick, Jwade)",
	                   "Clout Demons (prod. 406ahmad, MacShooter)",
                       "Sp5der (prod. prodbypatrick)",
                       "X and Instagram (prod. prodbypatrick, Jwade)",
	                   "Anti You (prod. Jwade, Nine Vicious)",
	                   "Mad Rappers (prod. 406ahmad)",
                       "Hit Em Up (prod. prodbypatrick, Jwade)",
                       "Beastmode (prod. prodbypatrick, Jwade, 1takeshi)",
                       "Again (prod. prodbypatrick, Jwade)",
                       "Take Me Down (prod. Nine Vicious, Elliott Latham)",
             ],
         },
         {
             "title": "FOR NOTHING",
             "kind": "Album",          # Album / EP / Mixtape
             "year": "July 4, 2025",
             "cover": "Nine Vicious - FOR NOTHING.jpg",              # file name inside images/
	         "url": "https://music.youtube.com/playlist?list=OLAK5uy_lXXIecjksJNOFf6oX3nux7iAQTmwxF9mQ",
             "tracks": [
                       "Can't Tell Me Nothing (prod. 406ahmad)",
	                   "Talkin Swag (prod. 406ahmad)",
	                   "New Means (prod. 406ahmad)",
                       "Co-sign (prod. prodbypatrick, R8)",
                       "Valley (prod. Bella, Elliot Latham)",
	                   "Moshpit (prod. prodbypatrick)",
	                   "Internet Gangsta (prod. BenjiCold)",
                       "Face (prod. Otxhello, Ajax, Dilip)",
                       "Chaos (prod. prodbypatrick, zatru, Jwade)",
                       "Mobb Deep (prod. 406ahmad)",
                       "Hurt Sum (prod. prodbypatrick)",
                       "Slatt Gospel (prod. 406ahmad)",
                       "Pretty (prod. Nosaint)",
                       "Dbz (prod. 406ahmad)",
                       "So Many Tears (prod. 406ahmad, Signedhonestly)",
                       "The End (prod. 406ahmad)",
             ],
         },
         {
             "title": "B4EM",
             "kind": "Album",          # Album / EP / Mixtape
             "year": "January 31, 2026",
             "cover": "Nine Vicious - B4EM.jpg",              # file name inside images/
	         "url": "https://music.youtube.com/playlist?list=OLAK5uy_nlZuw19WNy9GqUh0K-i2e0jYzAZuu4FjM",
             "tracks": [
                       "Raging Love (prod. 406ahmad)",
	                   "Riri (prod. prodbypatrick)",
	                   "More Painting (prod. Bella, Roqstar, Elliot Latham)",
                       "4Real (prod. 406ahmad)",
                       "Racks Blue (prod. R8)",
	                   "Listen Up Jews (prod. prodbypatrick, Bella)",
	                   "Fuck Ogs (prod. prodbypatrick, 406ahmad)",
                       "24Hrs (prod. 406ahmad)",
                       "Free Smoke (prod. Nosaint)",
                       "Anal (prod. prodbypatrick, Jwade, Bella)",
             ],
         },
         {
             "title": "EMOTIONS",
             "kind": "Album",          # Album / EP / Mixtape
             "year": "April 3, 2026",
             "cover": "Nine Vicious - EMOTIONS.jpg",              # file name inside images/
	         "url": "https://music.youtube.com/playlist?list=OLAK5uy_lOZUYqzGF9cIHwiLHCa84xSgoy-Xte3JQ",
             "tracks": [
                       "Talk About It (prod. 406ahmad)",
	                   "Amazing (prod. Bella, prodbypatrick, Jwade, Nine Vicious)",
	                   "Posing Tonight (prod. prodbypatrick)",
                       "Rolling Loud (prod. prodbypatrick, Elliot Latham)",
                       "Fashion Killa (prod. 406ahmad)",
	                   "Purple Swag (prod. prodbypatrick)",
	                   "Clock It (prod. prodbypatrick)",
                       "Treven O'Ryan Echols (prod. 406ahmad)",
                       "Vivienne Westwood / RIP (prod. Bella)",
                       "Want U (prod. Bella)",
                       "Project4play/Svj (prod. R8, prodbypatrick, Jwade)",
                       "Molly Ecstacy (prod. R8)",
                       "Sunset Hill (feat. Kacy Hill) (prod. Kacy Hill)",
                       "U Dig Det (prod. prodbypatrick, Jwade)",
                       "My Whole Heart (prod. 406ahmad)",
                       "Julia (prod. 406ahmad)",
                       "Need (prod. YUME)",
                       "Love Album (prod. R8, Jwade)",
                       "Italy (prod. R8)",
                       "Electric Feel (prod. 406ahmad)",
                       "Lifes Funny (prod. 406ahmad)",
                       "Forgot (prod. 406ahmad)",
                       "Blowing Emotions (prod. Nosaint, prodbypatrick)",
             ],
         },
         {
             "title": "SEDITION",
             "kind": "Mixtape",          # Album / EP / Mixtape
             "year": "September 11, 2026",
             "cover": "Nine Vicious - SEDITION.jpg",              # file name inside images/
	         "url": "https://music.youtube.com/playlist?list=OLAK5uy_mSSNOiXWdpv9l_Jexz2R6L7_6yFkek71Y",
             "tracks": [
                       "Anytime (prod. prodbypatrick, Bella)",
	                   "Cracker (prod. prodbypatrick, Bella)",
	                   "Mind Racing (prod. Bella)",
                       "Sing To Your Heart (prod. prodbypatrick, Bella)",
                       "Roq and Kobe (prod. prodbypatrick, Bella)",
	                   "Classy Girls (prod. prodbypatrick)",
	                   "Stranger Things (prod. prodbypatrick, Bella)",
                       "Casino (prod. prodbypatrick)",
                       "Chateau Marmont (prod. prodbypatrick)",
                       "Zone 3 (prod. Bella)",
                       "Fuck Flags (prod. Bella)",
                       "U.O.E.N.O (feat. NDO Dee) (prod. prodbypatrick, Roqstar)",
                       "Sardina (prod. Bella)",
                       "Go Bestie (prod. R8)",
                       "To Be Continued (prod. R8, prodbypatrick)",
             ],
         },
         {
             "title": "B4SA",
             "kind": "Mixtape",          # Album / EP / Mixtape
             "year": "November 15, 2024",
             "cover": "Nine Vicious - B4SA.jpg",              # file name inside images/
	         "url": "https://music.youtube.com/playlist?list=OLAK5uy_nU_B_S-8o8MhwoA6ldOJ5JkIHZI88yzok",
             "tracks": [
                       "Asakusabashi (prod. 406ahmad)",
	                   "Cuddle My Wrist (prod. 406ahmad, Kal Pierce)",
	                   "Fake Kickin (prod. 406ahmad)",
                       "Imma Krazy X (prod. 406ahmad)",
                       "Best Show On Earth (prod. Cade, prodbypatrick, yybaker)",
             ],
         },
         {
             "title": "B4TM",
             "kind": "EP",          # Album / EP / Mixtape
             "year": "January 31, 2025",
             "cover": "Nine Vicious - B4TM.jpg",              # file name inside images/
	         "url": "https://music.youtube.com/playlist?list=OLAK5uy_mCop0JVHpUjei4AuYkrU1E80zECOJQ3js",
             "tracks": [
                       "RIP Keed (prod. prodbypatrick, Jwade, Nine Vicious)",
	                   "Slime Bidness (prod. 406ahmad)",
	                   "Conversating (prod. prodbypatrick, Jwade)",
                       "You Said (prod. 406ahmad)",
                       "Outro (prod. prodbypatrick, Jwade, Taurus, Casper1of1, Splited Stupid, Nine Vicious)",
             ],
         },
         {
             "title": "B4FN",
             "kind": "EP",          # Album / EP / Mixtape
             "year": "June 6, 2025",
             "cover": "Nine Vicious - B4FN.jpg",              # file name inside images/
	         "url": "https://music.youtube.com/playlist?list=OLAK5uy_nyrsl3EOqczvONI80lIlUlHOir9b-M1rE",
             "tracks": [
                       "So FN (prod. 406ahmad)",
	                   "IMY (prod. 406ahmad)",
	                   "Movin On (prod. 406ahmad)",
                       "Fuck Yo Gang (prod. prodbypatrick)",
                       "Me N Slime (prod. Bella, prodbypatrick)",
                       "A Song (prod. 406ahmad, Signedhonestly)",
             ],
         },
         {
             "title": "ONE MORE WEEK",
             "kind": "EP",          # Album / EP / Mixtape
             "year": "June 27, 2025",
             "cover": "Nine Vicious - ONE MORE WEEK.jpg",              # file name inside images/
	         "url": "https://soundcloud.com/ninevicious-projects/sets/one-more-week",
             "tracks": [
                       "RIP GUS (prod. 406ahmad)",
	                   "My Shooter (prod. prodbypatrick)",
	                   "Skims (prod. 406ahmad)",
                       "Came A Long Way (prod. Bella, prodbypatrick)",
                       "What Them Racks Do (prod. Pyrex)",
             ],
         },
         {
             "title": "Couple Days",
             "kind": "EP",          # Album / EP / Mixtape
             "year": "January 24, 2026",
             "cover": "Nine Vicious - Couple Days.jpg",              # file name inside images/
	         "url": "https://soundcloud.com/user-267541570/sets/couple-days",
             "tracks": [
                       "pain (prod. 406ahmad)",
	                   "Washed Up (prod. 406ahmad)",
	                   "Feelings (prod. prodbypatrick)",
                       "French Montana (prod. prodbypatrick)",
             ],
         },
         {
             "title": "GIMME A MONTH",
             "kind": "Compilation",          # Album / EP / Mixtape
             "year": "March 11, 2026",
             "cover": "Nine Vicious - GIMME A MONTH.jpg",              # file name inside images/
	         "url": "https://soundcloud.com/whyamisoemotional/sets/gimme-a-month",
             "tracks": [
                       "Gen 5 (prod. 406ahmad)",
	                   "Bad Man (prod. prodbypatrick)",
	                   "Crazy Love (prod. 406ahmad)",
                       "Home Alone (prod. bella)",
                       "Piru (prod. Nosaint)",
             ],
         },
         {
             "title": "ARE YALL READY?",
             "kind": "EP",          # Album / EP / Mixtape
             "year": "March 12, 2026",
             "cover": "Nine Vicious - ARE YALL READY.jpg",              # file name inside images/
	         "url": "https://soundcloud.com/whyamisoemotional/sets/are-yall-ready",
             "tracks": [
                       "Unfortunate (prod. R8)",
	                   "Coors Light (prod. Bella)",
	                   "Japan Hoes (prod. Jwade)",
                       "Fought The Law (prod. prodbypatrick)",
                       "My World (prod. 406ahmad)",
             ],
         },

     ],
     "singles": [
         {
             "title": "U Fancy ? (prod. 406ahmad)",
             "year": "July 15, 2024",
             "cover": "Nine Vicious - U Fancy.jpg",
             "url": "https://soundcloud.com/ninesomnia/u-fancy-prod-406ahmad-music",
             "music_video": "https://www.youtube.com/watch?v=nD2X47-iERQ",
         },
         {
             "title": "U Bad (prod. 406ahmad)",
             "year": "September 7, 2024",
             "cover": "Nine Vicious - U Bad.jpg",
             "url": "https://soundcloud.com/ninesomnia/u-bad-prod-406ahmad-1",
             "music_video": "https://www.youtube.com/watch?v=5CQJRjxv-CM",
         },
         {
             "title": "All Facts (prod. 406ahmad)",
             "year": "September 29, 2024",
             "cover": "Nine Vicious - All Facts.jpg",
             "url": "https://soundcloud.com/ninesomnia/all-facts-prod-ahamd",
             "music_video": "https://www.youtube.com/watch?v=xpW8AQAM6Uk",
         },
         {
             "title": "My Speakers (prod. Jwade, Bella)",
             "year": "October 12, 2024",
             "cover": "Nine Vicious - My Speakers.jpg",
             "url": "https://soundcloud.com/ninesomnia/my-speakers-prod-jwade-bella",
         },
         {
             "title": "SOBS (prod. 406ahmad)",
             "year": "March 27, 2025",
             "cover": "Nine Vicious - SOBS.jpg",
             "url": "https://soundcloud.com/ninesomnia/sobs",
         },
         {
             "title": "Over N Over (prod. prodbypatrick)",
             "year": "September 3, 2026",
             "cover": "Nine Vicious - Over N Over.jpg",
             "url": "https://soundcloud.com/ninesomnia/over-n-over",
         },
         
     ],
 },
 {
     "name": "406ahmad",
     "image": "406ahmad.jpg",                      # file name inside images/
     "aliases": ["",],                    # ["Other Name", "Old Tag"]
     "dob": "",                        # "1996-03-04" or "March 4, 1996"
     "links": {
         "spotify": "https://open.spotify.com/artist/0wqrFq3UW32Nrk0prfcGT5",
         "youtube_music": "https://music.youtube.com/channel/UCTqlJi9Qr2yjmQU8_Xh5e-w",
         "soundcloud": "https://soundcloud.com/406ahmad",
     },
     "projects": [
         {
             "title": "LIFE OF AHMAD",
             "kind": "Album",          # Album / EP / Mixtape
             "year": "March 1, 2024",
             "cover": "406ahmad - LIFE OF AHMAD.jpg",              # file name inside images/
	         "url": "https://soundcloud.com/406ahmad/sets/life-of-ahmad",
             "tracks": [
                       "try again",
	                   "how high",
	                   "call em kill em",
                       "urthem00n",
                       "man i thought you was the one 4 me ≧ ﹏ ≦",
	                   "ahmad must die",
	                   "ksubi",
                       "stop Meee",
                       "2406... music",
                       "lyin8Dfun",
                       "speed dial",
                       "im at the ho right NOW",
             ],
         },
         {
             "title": "LIFE OF AHMAD 2",
             "kind": "Album",          
             "year": "November 1, 2024",
             "cover": "406ahmad - LIFE OF AHMAD 2.jpg",              
	         "url": "https://music.youtube.com/playlist?list=OLAK5uy_mzNoEtTw3H--yUoB-cQY9vYeUP_MIO_XI",
             "tracks": [
                       "COMMENTS (Intro) (feat. Lil Tyh) (prod. 406ahmad)",
	                   "feelGuD (feat. Lil Tyh) (prod. 406ahmad)",
	                   "YOUNG N29GA (feat. Lil Tyh) (prod. 406ahmad)",
                       "Hittin (feat. Nine Vicious) (prod. 406ahmad)",
                       "Know I Did (feat. Nine Vicious) (prod. 406ahmad)",
	                   "DO WHAT I WANT (feat. Lil Tyh) (prod. 406ahmad)",
	                   "JUMPMAN (feat. Lil Tyh) (prod. 406ahmad)",
                       "ExtraNumber (feat. Richxxzno) (prod. 406ahmad)",
                       "Groupie (feat. Nine Vicious) (prod. 406ahmad)",
                       "expectations (interlude) (feat. Lil Tyh) (prod. 406ahmad)",
                       "4 THE WORLD (feat. rodneyy) (prod. 406ahmad)",
                       "pillsbury doughboy (feat. MacShooter) (prod. 406ahmad)",
                       "Tumblr Love Story (feat. Nine Vicious) (prod. 406ahmad)",
             ],
         },
         {
             "title": "LIFE OF AHMAD 2.5",
             "kind": "EP",        
             "year": "April 13, 2025",
             "cover": "406ahmad - LIFE OF AHMAD 2.5.jpg",            
	         "url": "https://music.youtube.com/playlist?list=OLAK5uy_nVgm4i3OOGW_xVa3uJt9bMocxAcK-vqXs",
             "tracks": [
                       "GRANDPA FLOW (feat. Lil Tyh) (prod. 406ahmad)",
	                   "Blood Thicker Than Water (feat. Nine Vicious) (prod. 406ahmad)",
	                   "SCHWAG (feat. Lil Tyh) (prod. 406ahmad)",
                       "Ain't No End (feat. Nine Vicious) (prod. 406ahmad)",
                       "SHE LIKE DA BRAIDS (feat. Lil Tyh) (prod. 406ahmad)",
	                   "U Fine Shit (feat. Nine Vicious) (prod. 406ahmad)",
             ],
         },
         {
             "title": "40.6FM® ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ # tuned back in",
             "kind": "Compilation EP",          
             "year": "May 14, 2025",
             "cover": "406ahmad - tuned back in.jpg",              
	         "url": "https://music.youtube.com/playlist?list=OLAK5uy_kbjTpDiF_WKc-k64BN3pwukebhOBPLyds",
             "tracks": [
                       "Trust Issues (feat. Lil Tyh) (prod. 406ahmad)",
	                   "Story of Nine V (feat. Nine Vicious) (prod. 406ahmad)",
	                   "4L (Pi'erre Bourne Flip) (prod. 406ahmad)",
                       "NVREVER (feat. Yungzayy) (prod. 406ahmad)",
                       "Pinned (feat. Nine Vicious) (prod. 406ahmad)",
	                   "Shavon (feat. Nine Vicious) (prod. 406ahmad)",
	                   "Heart & Soul (feat. Lil Tyh) (prod. 406ahmad)",
             ],
         },


     ],
     "singles": [
     ],
 },
 
 {
     "name": "*67",
     "image": "star67.gif",                      # file name inside images/
     "aliases": ["star67", "Ismokecones", "osama xan laden", "wifiskeleton", "TRAPGOTH", "youaresogoddamnpathetic", "july", "helen", "doctor skeleton", "dj bonecrusher", "skeleton", "skele", "glaceon", "N (9a4)", "saddesteeveer", "dj gothangel", "skeleton archive", "dj cannibal", "secretsaturdays", "fuxkcy", "weddingcakethc", "fxkcy", "Moody", "ijustfeelmoody"],                    # ["Other Name", "Old Tag"]
     "dob": "July 24, 2003",                        # "1996-03-04" or "March 4, 1996"
     "dead": "yes",
     "links": {
         "spotify": "https://open.spotify.com/artist/3bJWbzkh2WK8JRLgmflcwk",
         "youtube_music": "https://music.youtube.com/@starophrenic",
         "soundcloud": "https://soundcloud.com/o67",
     },
     "projects": [
         {
             "title": "archives",
             "kind": "Album",          # Album / EP / Mixtape
             "year": "May 24, 2022",
             "cover": "star67 - archives.jpg",              # file name inside images/
	         "url": "https://music.youtube.com/playlist?list=OLAK5uy_knbVRbEFgkeiZyXqKeIFovbpEaNtrooCc",
             "tracks": [
                       "u ain't (feat. Bacleo) (prod. 333ciro)",
	                   "random title lmao (feat. aghast)",
	                   "gimme bluud #greed (feat. zinoblade)",
                       "lmfao ok (prod. Astralproperties)",
                       "leave me alone (prod. Thukk)",
	                   "sad vamp sex music (prod. Astralproperties, Toby Fox)",
	                   "#astrologyhoes 😂 #imaleo (prod. reidsixx)",
                       "tbh (prod. Astralproperties)",
                       "money 💸💸💸 (prod. 333ciro, Smokkestaxkk)",
                       "#ihatehumans (prod. bnbonic)",
             ],
         },
         {
             "title": "archives 2",
             "kind": "Compilation Album",          # Album / EP / Mixtape
             "year": "August 17, 2022",
             "cover": "star67 - archives 2.jpg",              # file name inside images/
	         "url": "https://music.youtube.com/playlist?list=OLAK5uy_kZtdI7D0_gYmNcmMfvV0jPC-jUkQkQTcg",
             "tracks": [
                       "no1 :( (prod. Dyan D)",
	                   "i_dnt_wnna_knw (prod. Dyan D)",
	                   "her <3 around my neck (prod. KL)",
                       "her </3 in my hands (prod. Kayy Luciano)",
                       "not evil o.o",
	                   "not evil og speed",
	                   "u dont luv me </3 (prod. *67)",
                       "tell me dat u luv me </3 (prod. Kayy Luciano)",
                       "luvv potion </3 (prod. twikipedia)",
                       "vampyr shawty ﹤/3 🧛‍♀️🍷 (prod. reidsixx)",
                       "vampyr shawty **OG** (prod. reidsixx)",
                       "‎vampyr shawty 2 🩸 #ivc (prod. Astralproperties)",
                       "worlds a fuck cover (prod. 2aja, *67)",
                       "take It all away (prod. Thukk)",
                       "#envy 🐍🎃 (prod. sh1ny)",
                       "#envy pt 2 #akahadiza (prod. zinoblade)",
                       "wit da clique lmao (feat. yuke) (prod. kkei3)",
                       "in #101 we trust (feat. kaystrueno) (prod. heroinsick, nyli)",
                       "run me yo blood (prod. dannyxgesko)",
                       "bored (prod. *67)",
                       "duel links",
             ],
         },
         {
             "title": "grims adventure ⛧",
             "kind": "Album",          # Album / EP / Mixtape
             "year": "June 4, 2022",
             "cover": "star67 - grims adventure.jpg",              # file name inside images/
	         "url": "https://music.youtube.com/playlist?list=OLAK5uy_ld5wUTITiRTnqiXRKgPlrJNEep3VMu7hE",
             "tracks": [
                       "retire it (prod. sh1ny)",
	                   "fma 2003 (prod. Thukk)",
	                   "#ghoul (prod. dannyxgesko)",
                       "sumtime (prod. kaystrueno)",
                       "lov u like a razor (prod. Cold Hart)",
	                   "#sp3llcaster (prod. reidsixx)",
	                   "who u wit? (prod. kaystrueno)",
                       "gone 2 soon (prod. sh1ny)",
             ],
         },
         {
             "title": "musik",
             "kind": "Album",          # Album / EP / Mixtape
             "year": "April 21, 2023",
             "cover": "star67 - musik.jpg",              # file name inside images/
	         "url": "https://music.youtube.com/playlist?list=OLAK5uy_lPf4sEkRs4xBJ8-_sKLijjdE42zY2lSN4",
             "tracks": [
                       "johto (prod. Swampkill)",
	                   "paranoid (prod. narcix)",
	                   "pretty little liars (prod. Astralproperties)",
                       "2k freestyle **deleting later** #IVC (prod. *67)",
                       "ion wna do shyt (prod. ESPIONAGE)",
	                   "konami (prod. keepsecrets)",
	                   "switched (feat. froe)",
                       "diss (prod. 333ciro)",
                       "casino (prod. lungskull)",
             ],
         },
         {
             "title": "*mixx*",
             "kind": "Album",          # Album / EP / Mixtape
             "year": "August 4, 2023",
             "cover": "star67 - mixx.jpg",              # file name inside images/
	         "url": "https://music.youtube.com/playlist?list=OLAK5uy_no9JLcWE0JP-babSXlYm6STtyduQ084NU",
             "tracks": [
                       "#heaven #can #wait #mixx",
	                   "#rain #mixx",
	                   "#one #in #a #million #mixx",
                       "#i #just #died #mixx",
                       "#weak #mixx",
	                   "#can #we #talk #mixx",
	                   "#they #dont #know #mixx",
                       "#who #can #i #run #to #mixx",
                       "#barbie 💃💄 mixx #mdma #greed",
                       "#like #a #tattoo #mixx (prod. *67)",
                       "#tayk #mixx (prod. Lord Fubu)",
             ],
         },
         {
             "title": "#sacrificedher",
             "kind": "EP",          # Album / EP / Mixtape
             "year": "December 2, 2021",
             "cover": "star67 - sacrificedher.jpg",              # file name inside images/
	         "url": "https://music.youtube.com/playlist?list=OLAK5uy_lSidqr_ax2p9Xf1vVQv27R1BGdI95Xpoc",
             "tracks": [
                       "#getdrained #101 (prod. Astralproperties)",
	                   "imm9rtal (prod. kaystrueno)",
	                   "#sloth 💉😴 (prod. dannyxgesko)",
                       "fallen@angel6* (prod. sh1ny)",
                       "fukk h8rs #badluck (prod. sh1ny)",
	                   "you're watching it backwards (prod. *67)",
             ],
         },

     ],
     "singles": [
         {
             "title": "sippin mud",
             "year": "July 2, 2021",
             "cover": "star67 - sippin mud.jpg",
             "url": "https://soundcloud.com/o67o/sippin-mud",
         },
         {
             "title": "whatsapp (feat. lieu) (prod. MexikoDro)",
             "year": "April 26, 2021",
             "cover": "star67 - whatsapp.jpg",
             "url": "https://soundcloud.com/o67o/whatsapp",
         },
         {
             "title": "mad at me (prod. Astralproperties)",
             "year": "September 10, 2021",
             "cover": "star67 - mad at me.jpg",
             "url": "https://soundcloud.com/o67archive/mad-at-me",
         },
         {
             "title": "ion wna do shyt (prod. ESPIONAGE)",
             "year": "November 22, 2021",
             "cover": "star67 - ion wna do shyt.jpg",
             "url": "https://soundcloud.com/o67archive/ion-wna-do-shyt",
         },
         {
             "title": "not me mix (つ﹏⊂) #greed #ivc 🩸💸 (prod. *67)",
             "year": "August 2, 2021",
             "cover": "star67 - not me mix.jpg",
             "url": "https://soundcloud.com/o67archive/not-me-mix-greed-ivc",
         },
         {
             "title": "#lust #greed anthem (feat. kaystrueno) (prod. sh1ny)",
             "year": "November 8, 2021",
             "cover": "star67 - lust greed anthem.jpg",
             "url": "https://soundcloud.com/greedmoney/lust",
         },
         {
             "title": "#trapnigga (feat. yuke)",
             "year": "January 20, 2022",
             "cover": "star67 - trapnigga.jpg",
             "url": "https://soundcloud.com/yuke/trap",
         },
         {
             "title": "cant fw ppl (feat. yuke) (prod. jaydes)",
             "year": "March 24, 2021",
             "cover": "star67 - cant fw ppl.jpg",
             "url": "https://soundcloud.com/o67archive/cant-fw-ppl",
         },
         {
             "title": "??? (feat. yuke)",
             "year": "April 19, 2021",
             "cover": "star67 - three question marks.jpg",
             "url": "https://soundcloud.com/o67archive/questionmarks",
         },
         {
             "title": "i hate zombys :pp (prod. 333ciro)",
             "year": "August 16, 2021",
             "cover": "star67 - i hate zombys.jpg",
             "url": "https://soundcloud.com/o67o/i-hate-zombys",
         },
         {
             "title": "won (feat. yuke, jaydes, lungskull) (prod. BURR SHRINE, lungskull)",
             "year": "April 8, 2021",
             "cover": "star67 - won.jpg",
             "url": "https://soundcloud.com/o67archive/won",
         },
         {
             "title": "#sloth 💉😴 (prod. dannyxgesko)",
             "year": "December 2, 2021",
             "cover": "star67 - sloth.jpg",
             "url": "https://soundcloud.com/o67archive/sloth",
         },
         {
             "title": "#lust #pride #ih8posers (feat. kaystrueno) (prod. living luxury)",
             "year": "May 24, 2022",
             "cover": "star67 - lust pride Ih8posers.jpg",
             "url": "https://soundcloud.com/greedmoney/pride",
         },
         {
             "title": "goofies #greed (feat. kaystrueno) (prod. H4llwd)",
             "year": "January 12, 2022",
             "cover": "star67 - goofies.jpg",
             "url": "https://soundcloud.com/getir67/goofies-greed-feat-kaystrueno",
         },
         {
             "title": "iwd2 (prod. Astralproperties)",
             "year": "May 25, 2022",
             "cover": "star67 - iwd2.jpg",
             "url": "https://soundcloud.com/o67archive/iwd2",
         },
         {
             "title": "fukk rapping bru (feat. islurwhenitalk) (prod. reidsixx)",
             "year": "April 2, 2022",
             "cover": "star67 - fukk rapping bru.jpg",
             "url": "https://soundcloud.com/o67o/fukk-rapping-bru",
         },
         {
             "title": "spirit krusher #greed #poserK (feat. kaystrueno) (prod. BLiTZ, 05sjinx)",
             "year": "April 27, 2022",
             "cover": "star67 - spirit krusher.jpg",
             "url": "https://soundcloud.com/greedmoney/spirit",
         },
         {
             "title": "greed (feat. yuke) (prod. zinoblade)",
             "year": "October 17, 2021",
             "cover": "star67 - greed.jpg",
             "url": "https://soundcloud.com/o67archive/greed-feat-yuke",
         },
         {
             "title": "cast a spell (feat. yuke) (prod. Tekika)",
             "year": "December 9, 2022",
             "cover": "star67 - cast a spell.jpg",
             "url": "https://soundcloud.com/o67archive/cast-a-spell",
         },
         {
             "title": "wish me away (prod. yai3)",
             "year": "May 7, 2023",
             "cover": "star67 - wish me away.jpg",
             "url": "https://soundcloud.com/o67archive/wish-me-away",
         },
         {
             "title": "demon #2k23 lmao 👻🐳 (prod. gardenofhades)",
             "year": "August 27, 2023",
             "cover": "star67 - demon.jpg",
             "url": "https://soundcloud.com/o67o/demon",
         },
         {
             "title": "cant stop greed #lust #😢🩸 (prod. flyingfish)",
             "year": "August 28, 2023",
             "cover": "star67 - cant stop greed.jpg",
             "url": "https://soundcloud.com/o67archive/cant-stop-greed-lust",
         },
         {
             "title": "corpse bride 👰🏼‍♀️",
             "year": "May 11, 2023",
             "cover": "star67 - corpse bride.jpg",
             "url": "https://soundcloud.com/o67o/corpse-bride",
         },
         {
             "title": "but_my_brain_so_fryed.wav (prod. 05sjinx)",
             "year": "May 15, 2023",
             "cover": "star67 - but my brain so fryed.jpg",
             "url": "https://soundcloud.com/o67o/but_my_brain_so_fryed",
         },
         
     ],
 },
 {
     "name": "yuke",
     "image": "yukee.jpg",                      # file name inside images/
     "aliases": ["propblood", "Baby Beel"],                    # ["Other Name", "Old Tag"]
     "dob": "2008",                        # "1996-03-04" or "March 4, 1996"
     "collectives": "najma",
     "links": {
         "spotify": "https://open.spotify.com/artist/3gJ7vM5lzXzYuYpnPy9WAL",
         "youtube_music": "https://music.youtube.com/@pourin",
         "soundcloud": "https://soundcloud.com/yuke",
     },
     "projects": [
         {
             "title": "sprain",
             "kind": "Album",          # Album / EP / Mixtape
             "year": "September 20, 2023",
             "cover": "yuke - sprain.jpg",              # file name inside images/
	         "url": "https://music.youtube.com/playlist?list=OLAK5uy_nOhmSwPpVDhPAPzXLO5obAnTMu5shY-vE",
             "tracks": [
                       "sativa (prod. marcusbasquiat)",
	                   "messy torture (feat. jaydes) (prod. zai)",
	                   "adversary (feat. jaydes) (prod. KRXXK)",
                       "love me while i'm here",
                       "anemia (prod. yuke)",
	                   "bleh bleh (prod. KRXXK)",
	                   "DIE ON ME (prod. SpaceGhostPurp, yuke)",
                       "rip unc 2 (prod. jaydes)",
                       "vampire witch (prod. jaydes)",
                       "ill admit it (prod. jaydes)",
                       "mataaaa (prod. FearDorian, bbyazul, histarkey)",
                       "schemin (prod. Downhill2k01)",
             ],
         },
         {
             "title": "trap finesse cult",
             "kind": "Mixtape",          # Album / EP / Mixtape
             "year": "March 29, 2024",
             "cover": "yuke - trap finesse cult.jpg",              # file name inside images/
	         "url": "https://music.youtube.com/playlist?list=OLAK5uy_l7jBz_NR8eqho4bufTuih_GePRnPCuMGY",
             "tracks": [
                       "blueprint (prod. Kade)",
	                   "sourtooth zomby grl (prod. zatru)",
	                   "goth bby (prod. karakuli, ogkush420)",
                       "widow rave coke whore (prod. zatru)",
                       "blood soda freestyle (feat. jaydes) (prod. october, yuke)",
	                   "braineater (prod. zatru)",
	                   "nauseated (prod. 90mgz, Luck)",
                       "giveaway (feat. kushbabykeys) (prod. karakuli)",
                       "what we was (prod. karakuli)",
                       "x you out for o's (prod. karakuli)",
                       "Blame (prod. october)",
                       "hellbound (prod. fashionist)",
                       "Snake! Snake! Snake! (prod. Goxan)",
                       "She Bless Me (prod. bbuggin)",
                       "splee my stain (feat. jaydes) (prod. jaydes)",
                       "anxious (prod. ogkush420)",
                       "finesse cult anthem (feat. jaydes) (prod. why5)",
             ],
         },
         {
             "title": "Mascara",
             "kind": "Mixtape",          # Album / EP / Mixtape
             "year": "July 26, 2024",
             "cover": "yuke - Mascara.jpg",              # file name inside images/
	         "url": "https://music.youtube.com/playlist?list=OLAK5uy_l3dmkARx8FhRqwc0FZ4UAqdFGOReCb0lE",
             "tracks": [
                       "used to it (prod. zai)",
	                   "wtf, wtf?, wtf! (prod. filthygenes)",
	                   "besos (prod. bandocasht)",
                       "sundress (prod. Essence)",
                       "count blues pop pinks (prod. StoopidXool)",
	                   "whereUwant222 (prod. bandocasht)",
	                   "medusas interlude",
                       "rave with all the weird girls (prod. zatru)",
                       "RRockkOutt (prod. zatru)",
                       "remember that time we bled (prod. zai)",
                       "witch bitch 2 (prod. bandocasht)",
                       "pump fake (prod. 20MOP, squillo)",
                       "trap dirty fit clean (prod. squillo)",
             ],
         },
         {
             "title": "Cheetah World",
             "kind": "Album",          # Album / EP / Mixtape
             "year": "December 1, 2024",
             "cover": "yuke - Cheetah World.jpg",              # file name inside images/
	         "url": "https://music.youtube.com/playlist?list=OLAK5uy_ljwpWXrRNqPfXcq_wArlzqF2cEWpKmcr8",
             "tracks": [
                       "Finessed (prod. boolymon)",
	                   "gone bad (prod. Al Chapo)",
	                   "you yea you!! (prod. yuke)",
                       "don't worry (prod. perc40)",
                       "Sick of it (prod. 7300)",
	                   "for me, sometimes for you (prod. cairo)",
	                   "dnd (prod. Jshxwty)",
                       "cookies (feat. elijxhwtf) (prod. elijxhwtf, Wise)",
                       "bad person (prod. Essence)",
                       "bloodrain (prod. filthygenes)",
                       "prince beel (prod. boolymon)",
                       "hella sht (prod. ksuuvi)",
                       "ian goin 2 (prod. cairo, Marrgielaa)",
                       "Cake (prod. twovrt)",
                       "xoxoOooOo (feat. Kid Moon) (prod. october)",
             ],
         },
         {
             "title": "is it propblood",
             "kind": "Compilation Album",          # Album / EP / Mixtape
             "year": "November 7, 2025",
             "cover": "yuke - is it propblood.jpg",              # file name inside images/
	         "url": "https://music.youtube.com/playlist?list=OLAK5uy_mAY_Yp1BBhk4Z6P9NUgtIOz9aPz2LWcJY",
             "tracks": [
                       "Ummm I swear.. (prod. yuke)",
	                   "4:44 am freestyle (prod. yaridubz)",
	                   "puppets homesick (prod. bbuggin)",
                       "they stole everything (prod. bbuggin)",
                       "....fried!!!x!-_-!x!!! (prod. propblood)",
	                   "sick manic state yes i'm baby beel (prod. Harrison)",
	                   "phone_chirpin_#📲🐣 (prod. yuke)",
                       "mayb i'll like u :p (prod. chuchumiyake)",
                       "hahahaha kill me tonight #NoWonderI’mNumb😵😂😂",
                       "Reap what you sow (prod. karakuli)",
                       "My doubts (prod. 19thou)",
                       "our fairytale (prod. october)",
                       "broke my wrist (prod. 50made, yuke)",
                       "broward hoes love xanax (feat. jaydes) (prod. yuke, bleood)",
                       "dead lungs (😵🫁) (prod. yuke, ogkush420)",
                       "616th sense (prod. yuke)",
                       "at me not u (prod. yuke)",
                       "c'est la vie (prod. yuke, thuggpint)",
                       "propblood but when i bleed out it'll be for real (prod. ogkush420)",
                       "getawayfromme! (prod. yuke)",
                       "show sum racks (prod. yuke)",
             ],
         },
         {
             "title": "Cheetah World (Deluxe)",
             "kind": "Deluxe",          # Album / EP / Mixtape
             "year": "December 31, 2024",
             "cover": "yuke - Cheetah World Deluxe.jpg",              # file name inside images/
	         "url": "https://music.youtube.com/playlist?list=OLAK5uy_lnIoo_ttj-7yaz9mn8aId1O9CYMGwpfJg",
             "tracks": [
                       "Cheetahprint (prod. perc40)",
	                   "Knew Friends (prod. perc40)",
	                   "Destiny's Child (prod. Al Chapo)",
                       "Uptown (prod. Oscar100, reklus1ve)",
                       "Made Me Sick!! (feat. Kid Moon) (prod. 19thou, Al Chapo)",
	                   "Misery (prod. XanGang)",
	                   "Goodnight Interlude (prod. yuke)",
             ],
         },
         {
             "title": "Miss Misery",
             "kind": "Album",          # Album / EP / Mixtape
             "year": "March 7, 2025",
             "cover": "yuke - Miss Misery.jpg",              # file name inside images/
	         "url": "https://music.youtube.com/playlist?list=OLAK5uy_l6HfZ5MJnC4ggN2JFVB0B0Th0a3iIuhDk",
             "tracks": [
                       "superstar (prod. Synthetic, ivvys, bass)",
	                   "just with you (prod. XanGang)",
	                   "save dat shit (prod. zatru)",
                       "take his loot (feat. boolymon) (prod. boolymon)",
                       "lucky (prod. twovrt, boolymon, Thrty, Stimglocks)",
	                   "moneyteam92 (prod. zai)",
	                   "finer things (prod. 19thou)",
                       "#Yolo (prod. boolymon)",
                       "soho (prod. perc40, twovrt)",
                       "need rest (prod. perc40)",
                       "weep 111 interlude (prod. yuke, cashcache!)",
                       "really ill (prod. clay10)",
                       "miss calls (prod. twovrt, ZaySkillz)",
                       "sex magik (feat. suban) (prod. suban)",
                       "way 222! (prod. zai)",
                       "hold me back (bonus outro) (prod. kashpaint)",
             ],
         },
         {
             "title": "Cheetah World 2",
             "kind": "Album",          # Album / EP / Mixtape
             "year": "August 1, 2025",
             "cover": "yuke - Cheetah World 2.jpg",              # file name inside images/
	         "url": "https://music.youtube.com/playlist?list=OLAK5uy_kg5-4MFtN8NblAeMJSeOekCFt3Y5Oa6YQ",
             "tracks": [
                       "Brain, slushy! (prod. zatru)",
	                   "Apathy (prod. zatru)",
	                   "my finessa <3 (prod. october, yuke)",
                       "Misery, Pt. 2 (prod. yuke)",
                       "wake, bake, repeat (prod. zatru)",
	                   "Unlucky (prod. cashcache!)",
	                   "now & later (prod. bbuggin)",
                       "all You had (prod. yuke)",
                       "Paranoia (prod. october)",
                       "backstabber (feat. suban) (prod. FearDorian, blsq)",
                       "Ms. Headache (prod. jaydes)",
                       "she's an addict (prod. zai)",
                       "just forget me interlude (prod. yuke, october)",
                       "On You (prod. zatru)",
                       "DoYouFeelIt? (prod. zatru, scarephomet)",
                       "tore My Heart off My sleeve (prod. zatru, scarephomet)",
                       "Soo In My Head (prod. zatru, scarephomet)",
                       "kill (prod. perc40)",
                       "outta sight (prod. perc40)",
                       "sorry (prod. perc40)",
                       "Not today (prod. ksuuvi)",
                       "crashed out (prod. perc40)",
                       "still (bonus) (feat. ksuuvi) (prod. ksuuvi)",
             ],
         },
         {
             "title": "Cheetah World 3",
             "kind": "Album",          # Album / EP / Mixtape
             "year": "July 17, 2026",
             "cover": "yuke - Cheetaah World 3.jpg",              # file name inside images/
	         "url": "https://music.youtube.com/playlist?list=OLAK5uy_lFFpEbnx8_6JU8HbtRUXKECVrnvAoBwF0",
             "tracks": [
                       "yaeba (intro) (prod. zai)",
	                   "Kelly K (prod. elibanss)",
	                   "Loose Screws (prod. zatru)",
                       "Serotonin (prod. zai)",
                       "vámonos (feat. ksuuvi) (prod. clay10)",
	                   "heavy metul (prod. october)",
	                   "My Flesh (prod. october)",
                       "Ruthless Fun (prod. twentythree)",
                       "ick (feat. jaydes) (prod. october)",
                       "Therapy (prod. Devstacks)",
                       "Wishing Well (prod. st47ic)",
                       "Bitter (prod. zatru)",
                       "On My Way! (prod. ss3bby, anonnn)",
                       "Lust (prod. bbuggin)",
                       "codependent (prod. st47ic)",
                       "weirdness (prod. ss3bby, anonnn)",
                       "take a test (feat. elibanss) (prod. elibanss)",
                       "once again (prod. sur6ery)",
             ],
         },
         {
             "title": "finesse angel",
             "kind": "Collab EP (yuke & *67)",          # Album / EP / Mixtape
             "year": "May 10, 2025",
             "cover": "yuke - finesse angel.jpg",              # file name inside images/
             "collab": "*67",
	         "url": "https://archive.org/details/finesse-angel",
             "tracks": [
                       "haunting you 👻😢 (prod. Dimitris Vokolos)",
	                   "creepy chan (prod. yuke, Sehous)",
	                   "tabs b4 sleep..zzz (prod. october)",
             ],
         },
         {
             "title": "beel",
             "kind": "Single",          # Album / EP / Mixtape
             "year": "August 17, 2023",
             "cover": "yuke - beel.jpg",              # file name inside images/
	         "url": "https://music.youtube.com/playlist?list=OLAK5uy_kFY5RGxvWkqUoEARH6XKm5_gjDlKF_sjA",
             "tracks": [
                       "mana (prod. zinoblade)",
	                   "not my her (prod. rue22222)",
	                   "marcy (prod. yuke)",
             ],
         },
         {
             "title": "bx baby",
             "kind": "EP",          
             "year": "December 22, 2023",
             "cover": "yuke - bx baby.jpg",              
	         "url": "https://music.youtube.com/playlist?list=OLAK5uy_lmP9I96xltgamtmvvS7uymOHseokzopco",
             "tracks": [
                       "save me (prod. kiltmymood)",
	                   "bratz (prod. yuke)",
	                   "see u (prod. 7venlyves)",
                       "too much (feat. jaydes) (prod. Kayy Luciano)",
                       "betrayal (prod. slaywitme)",
	                   "Sacrifice Myself to Tundra (prod. exset)",
             ],
         },
         {
             "title": "bonus 4 my cult",
             "kind": "Single",          
             "year": "April 3, 2024",
             "cover": "yuke - bonus 4 my cult.jpg",              
	         "url": "https://music.youtube.com/playlist?list=OLAK5uy_kmKjm2rXhEs8lJl4Tk5kjVSI3O-jXd4DA",
             "tracks": [
                       "splee my stain (feat. jaydes) (prod. jaydes)",
	                   "head split (prod. october)",
             ],
         },
         {
             "title": "6 cheetahs 1 dove 6 owls",
             "kind": "Single",          
             "year": "April 21, 2024",
             "cover": "yuke - 6 cheetahs 1 dove 6 owls.jpg",              
	         "url": "https://music.youtube.com/playlist?list=OLAK5uy_mLpFM8QonXookAntfEDGETCXCEoJubKXs",
             "tracks": [
                       "heart soo dull (prod. ogkush420)",
	                   "dead fantasy (prod. fakehundreds)",
	                   "grave dug (prod. jaydes)",
             ],
         },
         {
             "title": "Broke my wrist / liar",
             "kind": "Single",          
             "year": "May 10, 2024",
             "cover": "yuke - Broke my wrist liar.jpg",              
	         "url": "https://music.youtube.com/playlist?list=OLAK5uy_l7C3Fm9ZDhUw4saQfCCWKo9OMmPFKrXTY",
             "tracks": [
                       "broke my wrist (prod. 50made, yuke)",
	                   "liar (prod. 50made)",
             ],
         },
         {
             "title": "sorry",
             "kind": "Single",          
             "year": "July 3, 2024",
             "cover": "yuke - sorry.jpg",              
	         "url": "https://music.youtube.com/playlist?list=OLAK5uy_k1vR_y86kGT0CGrCqnKDmq-wTCNm_5E9A",
             "tracks": [
                       "3.5 wood before i finally end it (prod. Sincerely Dre)",
	                   "ooooOooOoo (prod. outtaloveee)",
             ],
         },
         {
             "title": "death parade.. throw your hands up",
             "kind": "EP",          
             "year": "September 20, 2024",
             "cover": "yuke - death parade.jpg",              
	         "url": "https://music.youtube.com/playlist?list=OLAK5uy_lPkLXqIRqJPF3-o8M06wopj-CI_ZgUgEU",
             "tracks": [
                       "#girltalk #crushingg (prod. yuke)",
	                   "trap ↑ jump (prod. Essence)",
	                   "death parade (prod. zatru)",
             ],
         },
         {
             "title": "b4, miss misery",
             "kind": "Single",          
             "year": "February 13, 2025",
             "cover": "yuke - b4 miss misery.jpg",              
	         "url": "https://music.youtube.com/playlist?list=OLAK5uy_lz-KFJS8d_6gRZEgjOJISbBL3fNHoiBlA",
             "tracks": [
                       "know (prod. XanGang)",
	                   "not again (feat. irokkout) (prod. ogkush420)",
             ],
         },
         {
             "title": "b4 cheetah world 3",
             "kind": "EP",          
             "year": "May 27, 2026",
             "cover": "yuke - b4 cheetah world 3.jpg",              
	         "url": "https://music.youtube.com/playlist?list=OLAK5uy_myw5hPwF_wi-KTttSV29wfU13iMqGn8Uo",
             "tracks": [
                       "Loop (prod. Jsavant)",
	                   "jt to my uzi (prod. october)",
	                   "i gotta smoke before i eat (prod. october)",
             ],
         },
         

     ],
     "singles": [
         {
             "title": "creepin (prod. Kayy Luciano)",
             "year": "July 22, 2021",
             "cover": "yuke - creepin.jpg",
             "url": "https://soundcloud.com/youlied/creep",
         },
         {
             "title": "guap (prod. Lincoln Minaj)",
             "year": "June 4, 2021",
             "cover": "yuke - guap.jpg",
             "url": "https://soundcloud.com/yuke/guap",
         },
         {
             "title": "hit my dougie (prod. Cali Swag District)",
             "year": "January 1, 2021",
             "cover": "yuke - hit my dougie.jpg",
             "url": "https://soundcloud.com/yuke/yook",
         },
         {
             "title": "persona (feat. jaydes) (prod. sh1ny)",
             "year": "November 10, 2021",
             "cover": "yuke - persona.jpg",
             "url": "https://soundcloud.com/yuke/persona",
         },
         {
             "title": "why? (prod. yuke)",
             "year": "January 8, 2022",
             "cover": "yuke - why.jpg",
             "url": "https://soundcloud.com/youlied/why",
         },
         {
             "title": "gone (prod. lungskull)",
             "year": "February 19, 2021",
             "cover": "yuke - gone.jpg",
             "url": "https://soundcloud.com/arzfindsomepeace/yuke-lungskull-gone",
         },
         {
             "title": "fangs (prod. jaydes)",
             "year": "February 22, 2022",
             "cover": "yuke - fangs.jpg",
             "url": "https://soundcloud.com/trliy/yuke-fangs-feat-jaydes",
         },
         {
             "title": "hi tech (feat. jaydes) (prod. kkei3)",
             "year": "April 11, 2022",
             "cover": "yuke - hi tech.jpg",
             "url": "https://soundcloud.com/yuke/hi-tech",
         },
         {
             "title": "howl (feat. jaydes) (prod. yuke, gementines)",
             "year": "May 20, 2022",
             "cover": "yuke - howl.jpg",
             "url": "https://soundcloud.com/yuke/howl",
         },
         {
             "title": "ion want it (prod. Lymz, reidsixx)",
             "year": "June 3, 2022",
             "cover": "jaydes - entry log.jpg",
             "url": "https://soundcloud.com/yuke/fame",
         },
         {
             "title": "chase a check (prod. d0llywood1)",
             "year": "April 11, 2023",
             "cover": "yuke - chase a check.jpg",
             "url": "https://soundcloud.com/djphat1996/yuke-chase-a-check-prod",
         },
         {
             "title": "nosebleeds (prod. BossUp)",
             "year": "April 14, 2023",
             "cover": "yuke - nosebleeds.jpg",
             "url": "https://soundcloud.com/yuke/nosebleeds",
         },
         {
             "title": "blessed (fed ex) (prod. why5)",
             "year": "May 5, 2023",
             "cover": "yuke - blessed.jpg",
             "url": "https://soundcloud.com/yuke/blessed_fed_ex",
         },
         {
             "title": "No time (prod. StoopidXool)",
             "year": "June 1, 2023",
             "cover": "yuke - No time.jpg",
             "url": "https://soundcloud.com/yuke/no-time",
         },
         {
             "title": "Björk (All she do is chew on xan) (prod. MexikoDro)",
             "year": "June 23, 2023",
             "cover": "jaydes - entry log.jpg",
             "url": "https://soundcloud.com/yuke/bjork",
         },
         {
             "title": "HIT MY CELL (prod. BossUp, D. Murci)",
             "year": "July 26, 2023",
             "cover": "yuke - HIT MY CELL.jpg",
             "url": "https://soundcloud.com/yuke/trap_til_sun_down",
         },
         {
             "title": "30 fps 180ping (o_O) ? (prod. loveableang4l)",
             "year": "November 1, 2024",
             "cover": "yuke - 30 fps 180ping.jpg",
             "url": "https://sprained.bandcamp.com/track/30-fps-180ping-o-o",
         },
         {
             "title": "witch bitch (prod. yuke)",
             "year": "July 29, 2023",
             "cover": "yuke - witch.jpg",
             "url": "https://soundcloud.com/yuke/witch",
         },
         {
             "title": "no trust (it's urgent) #HaHaHa (prod. Croagpunk)",
             "year": "July 26, 2023",
             "cover": "yuke - no trust HaHaHa.jpg",
             "url": "https://soundcloud.com/yuke/urgency",
         },
         {
             "title": "heinous nonsense (feat. jaydes) (prod. suban)",
             "year": "July 30, 2023",
             "cover": "yuke - heinous nonsense.jpg",
             "url": "https://soundcloud.com/yuke/heinous",
         },
         {
             "title": "stupid bitches (feat. tana) (prod. yuke)",
             "year": "August 30, 2023",
             "cover": "yuke - stupid btchs.jpg",
             "url": "https://soundcloud.com/yuke/bana",
         },
         {
             "title": "reload (feat. jaydes) (prod. yuke)",
             "year": "September 14, 2023",
             "cover": "yuke - reload.jpg",
             "url": "https://soundcloud.com/yuke/reload",
         },
         {
             "title": "labyrinth (prod. yuke)",
             "year": "October 13, 2023",
             "cover": "yuke - labyrinth.jpg",
             "url": "https://soundcloud.com/yuke/labyrinth",
         },
         {
             "title": "on your own (prod. NerdCoke)",
             "year": "October 7, 2023",
             "cover": "yuke - on your own.jpg",
             "url": "https://soundcloud.com/yuke/on-your-own",
         },
         {
             "title": "crashdummy (prod. 9)",
             "year": "October 29, 2023",
             "cover": "yuke - crashdummy.jpg",
             "url": "https://soundcloud.com/goetiass/yuke-crashdummy",
         },
         {
             "title": "save me (prod. kiltmymood)",
             "year": "December 14, 2023",
             "cover": "yuke - save me.jpg",
             "url": "https://soundcloud.com/yuke/save-me",
         },
         {
             "title": "trapspot (feat. jaydes) (prod. kiltmymood)",
             "year": "January 20, 2024",
             "cover": "yuke - trapspot.jpg",
             "url": "https://soundcloud.com/yuke/trapspot",
         },
         {
             "title": "right now? (feat. jaydes) (prod. imsg)",
             "year": "January 29, 2024",
             "cover": "yuke - right now.jpg",
             "url": "https://soundcloud.com/yuke/rn_rn",
         },
         {
             "title": "percocet princess (prod. marcusbasquiat)",
             "year": "February 4, 2024",
             "cover": "yuke - percocet princess.jpg",
             "url": "https://soundcloud.com/goetiass/yuke-percocet-princess",
         },
         {
             "title": "fuck, shit! (feat. zai) (prod. zatru)",
             "year": "February 14, 2024",
             "cover": "yuke - percocet princess.jpg",
             "url": "https://soundcloud.com/vicodin78/yuke-fuck-shit-w-wuu",
         },
         {
             "title": "finesse cult anthem (feat. jaydes) (prod. why5)",
             "year": "March 20, 2024",
             "cover": "yuke - trap finesse cult.jpg",
             "url": "https://soundcloud.com/yuke/fca",
         },
         {
             "title": "trap lullaby (prod. Milan)",
             "year": "April 24, 2024",
             "cover": "yuke - trap lullaby.jpg",
             "url": "https://soundcloud.com/yuke/trap-lullaby",
         },
         {
             "title": "screw you (prod. Essence)",
             "year": "May 6, 2024",
             "cover": "yuke - screw you.jpg",
             "url": "https://soundcloud.com/yuke/screw-you",
         },
         {
             "title": "sanctioned (ignorant flauntin) (prod. Dylvinci)",
             "year": "May 31, 2024",
             "cover": "yuke - sanctioned.jpg",
             "url": "https://soundcloud.com/yuke/ignorant",
         },
         {
             "title": "hit my stain <3 (prod. Essence)",
             "year": "June 14, 2024",
             "cover": "yuke - hit my stain.jpg",
             "url": "https://soundcloud.com/yuke/hit-my-stain",
         },
         {
             "title": "ppfm (prod. Goxan)",
             "year": "June 24, 2024",
             "cover": "yuke - ppfm.jpg",
             "url": "https://soundcloud.com/yuke/ppfm",
         },
         {
             "title": "ian goin (prod. karakuli)",
             "year": "March 1, 2024",
             "cover": "yuke - ian goin.jpg",
             "url": "https://soundcloud.com/yuke/iangoin",
             "music_video": "https://www.youtube.com/watch?v=5CMfzGy_QPc",
         },
         {
             "title": "ok (feat. elijxhwtf) (prod. BenjiCold)",
             "year": "August 9, 2024",
             "cover": "yuke - ok.jpg",
             "url": "https://soundcloud.com/yuke/ok-w-elijxhwtf",
         },
         {
             "title": "you not (prod. Polo Boy Shawty)",
             "year": "August 19, 2024",
             "cover": "yuke - you not.jpg",
             "url": "https://soundcloud.com/yuke/you-not",
         },
         {
             "title": "RRegret (prod. zatru)",
             "year": "September 13, 2024",
             "cover": "yuke - RRegret.jpg",
             "url": "https://soundcloud.com/yuke/regret",
             "music_video": "https://www.youtube.com/watch?v=lRGJq45VLRY",
         },
         {
             "title": "my bad (feat. jaydes) (prod. 444jet)",
             "year": "October 9, 2024",
             "cover": "yuke - my bad.jpg",
             "url": "https://soundcloud.com/yuke/my-bad",
         },
         {
             "title": "Christmas Killing (feat. Marrgielaa) (prod. boolymon)",
             "year": "December 25, 2024",
             "cover": "yuke - percocet princess.jpg",
             "url": "https://soundcloud.com/yuke/christmas-killing",
         },
         {
             "title": "ciao </3 (prod. yuke)",
             "year": "January 24, 2025",
             "cover": "yuke - ciao.jpg",
             "url": "https://soundcloud.com/yuke/ciao",
         },
         {
             "title": "out da spot (feat. ksuuvi) (prod. bbuggin)",
             "year": "January 31, 2025",
             "cover": "yuke - out da spot.jpg",
             "url": "https://soundcloud.com/yuke/out-da-spot-wit-ksuuvi",
         },
         {
             "title": "rihanna (prod. yuke)",
             "year": "March 29, 2025",
             "cover": "yuke - rihanna.jpg",
             "url": "https://soundcloud.com/yuke/rihanna-prod-me",
         },
         {
             "title": "Brain, slushy! (prod. zatru)",
             "year": "June 16, 2025",
             "cover": "yuke - brain slushy.jpg",
             "url": "https://soundcloud.com/yuke/brainslushy",
         },
         {
             "title": "uh huh (prod. elibanss)",
             "year": "September 20, 2025",
             "cover": "yuke - uh huh.jpg",
             "url": "https://soundcloud.com/yuke/uh-huh-prod-eli",
         },
         {
             "title": "drop (feat. Dragnutz) (prod. twentythree)",
             "year": "October 17, 2025",
             "cover": "yuke - drop.jpg",
             "url": "https://soundcloud.com/yuke/drop",
         },
         {
             "title": "malware exe (prod. try1, Bassfreak)",
             "year": "November 15, 2025",
             "cover": "yuke - malware exe.jpg",
             "url": "https://soundcloud.com/yuke/malware-exe-prod-try1",
         },
         {
             "title": "damned (prod. jaydes)",
             "year": "January 21, 2026",
             "cover": "yuke - damned.jpg",
             "url": "https://soundcloud.com/trapfinessecult/damned",
         },
         {
             "title": "Open (prod. bbuggin)",
             "year": "February 13, 2026",
             "cover": "yuke - Open.jpg",
             "url": "https://soundcloud.com/benso-359794309/yuke-open",
         },
         {
             "title": "in a bad mood (prod. cylis)",
             "year": "June 7, 2026",
             "cover": "yuke - in a bad mood.jpg",
             "url": "https://soundcloud.com/trapfinessecult/bad-mood",
         },
         {
             "title": "ouch (prod. bleood)",
             "year": "July 11, 2025",
             "cover": "yuke - ouch.jpg",
             "url": "https://soundcloud.com/trapfinessecult/yuke-ouch",
         },
         
     ],
 },
 {
     "name": "yrsci",
     "image": "yrsci.jpg",                      
     "aliases": ["",],                    
     "dob": "June 26, 2008",
     "collectives": "iGore",   
     "links": {
         "spotify": "https://open.spotify.com/artist/7y7kZ5DDqttLU66sVpWjgG",
         "youtube_music": "https://music.youtube.com/channel/UCkIU9mYh70Fc-RaLuL4U_Vw",
         "soundcloud": "https://soundcloud.com/yrsci",
     },
     "projects": [
         {
             "title": "",
             "kind": "Album",          
             "year": "",
             "cover": "",              
	         "url": "",
             "tracks": [
                       "",
	                   "",
	                   "",
                       "",
                       "",
	                   "",
	                   "",
                       "",
             ],
         },


     ],
     "singles": [
         {
             "title": "law (prod. perc40)",
             "year": "February 17, 2024",
             "cover": "yrsci - law.jpg",
             "url": "https://soundcloud.com/vtet/yrsci-law-prod-perc40",
         },
         {
             "title": "anthem (feat. Universe, ivvys) (prod. rachyl)",
             "year": "January 13, 2024",
             "cover": "yrsci - anthem.jpg",
             "url": "https://soundcloud.com/yrsci-archive/anthem-w-universe-n-ivvys-prod",
         },
         {
             "title": "nobody (feat. vaunt) (prod. rachyl)",
             "year": "January 27, 2024",
             "cover": "yrsci - nobody.jpg",
             "url": "https://soundcloud.com/yrsci-archive3/nobody-w-vaunt-prod-rachyl",
         },
         {
             "title": "suicide at dawn 2 (prod. bonxpf)",
             "year": "2024",
             "cover": "yrsci - suicide at dawn 2.jpg",
             "url": "https://soundcloud.com/yrsci-archive/suicide-at-dawn-2-prod-bonxpf",
         },
         {
             "title": "yea i said it (prod. rachyl)",
             "year": "2024",
             "cover": "yrsci - yea i said it.jpg",
             "url": "https://soundcloud.com/yrsci-archive3/yea-i-said-it-prod-rachyl",
         },
         {
             "title": "trust (prod. myrlu)",
             "year": "2024",
             "cover": "yrsci - trust.jpg",
             "url": "https://soundcloud.com/yrsci-archive/trust-prod-myrlu",
         },
         
     ],
 },
 
 {
     "name": "ifleeze",
     "image": "ifleeze.gif",                      
     "aliases": ["geekordieeee", "afleezyyy",],                    
     "dob": "",                        
     "links": {
         "spotify": "https://open.spotify.com/artist/5LavxxfaEyZq4185erWwic",
         "youtube_music": "https://music.youtube.com/channel/UCeBHR6ukyTHIT-YFoFpF0iw",
         "soundcloud": "https://soundcloud.com/afleezyyy-topic",
     },
     "projects": [
         {
             "title": "GEEKLAND",
             "kind": "Album",          
             "year": "May 26, 2025",
             "cover": "ifleeze - GEEKLAND.jpg",              
	         "url": "https://music.youtube.com/playlist?list=OLAK5uy_nIj8qpv-j4LIDszbgURPCUloCEzus2aXk",
             "tracks": [
                       "Yeti Intro (prod. advnxm)",
	                   "Stranger (prod. 130jajo, Sslimez)",
	                   "Kicked Me Out (feat. Pdotty) (prod. Icebergcxc)",
                       "Lamelo Ball (prod. jamalslime)",
                       "Fun & Guns (prod. lucgeng)",
	                   "Yessssss (prod. 556fivefivesix)",
	                   "Kicked From Reign",
                       "Sharinigan Clan (prod. yuxngmake21)",
                       "Geek & Fleeze (prod. fuckkona)",
                       "32 Flow (feat. 32 Georgia Dome) (prod. ibk)",
                       "Fleeze & Boom (prod. wastedance)",
                       "Flow (feat. maloffkraxk) (prod. pglocks)",
                       "Lab Rats (prod. krashahtkitty, tril14r)",
                       "Harvey Beak (prod. Rroy)",
                       "Dont Kill Yourself (prod. yuxngmake21)",
                       "Anime Nigga (prod. fmjinmypocket, drewwcold)",
             ],
         },
         {
             "title": "see u in 30 days",
             "kind": "EP",          
             "year": "October 24, 2025",
             "cover": "ifleeze - see u in 30 days.jpg",              
	         "url": "https://music.youtube.com/playlist?list=OLAK5uy_nIOppTecdTWbEd5ioCgd6TgzY8Qa49cr4",
             "tracks": [
                       "wit my slime (prod. lilslime)",
	                   "goten (prod. 1luvvhate)",
	                   "lil o (prod. brei4k, mahxltxl)",
                       "red juice (prod. lucgeng)",
                       "phoenix suns (prod. lucgeng)",
             ],
         },
         {
             "title": "slime u in 30 days",
             "kind": "EP",          
             "year": "August 11, 2026",
             "cover": "ifleeze - slime u in 30 days.jpg",              
	         "url": "https://music.youtube.com/playlist?list=OLAK5uy_m5f5c7Snf6qtvB3JYx72FVLyGDiYMUd-I",
             "tracks": [
                       "model ho (prod. slimeyourdayone, faraone)",
	                   "slime you (prod. slimeyourdayone, my7threason, bottletiphero)",
	                   "long story short its over (prod. slimeyourdayone, my7threason, faraone)",
             ],
         },


     ],
     "singles": [
         {
             "title": "gore (prod. 50vault)",
             "year": "July 19, 2024",
             "cover": "ifleeze - gore.jpg",
             "url": "https://soundcloud.com/afleezyyy-topic/afleezyyy-gore-prod-50vault",
         },
         {
             "title": "kouldntgeterection (prod. Vlac)",
             "year": "August 12, 2024",
             "cover": "ifleeze - kouldntgeterection.jpg",
             "url": "https://soundcloud.com/afleezyyy-topic/kouldntgeterection-prod",
         },
         {
             "title": "ChainSaw (prod. Jshxwty)",
             "year": "November 2, 2024",
             "cover": "ifleeze - ChainSaw.jpg",
             "url": "https://soundcloud.com/afleezyyy-topic/fleeze-chainsaw-prod-jshwty",
         },
         {
             "title": "idk who u is ",
             "year": "March 26, 2026",
             "cover": "ifleeze - idk who u is.jpg",
             "url": "https://soundcloud.com/afleezyyy-topic/idk-who-u-is",
         },
         {
             "title": "a drug / blakkflag! (prod. lucgeng, mani)",
             "year": "July 6, 2026",
             "cover": "ifleeze - ChainSaw.jpg",
             "url": "https://soundcloud.com/slumpaudiosradio/ifleeze-a-drug-blakkflag",
         },
         
     ],
 },
 
]


# ---------------------------------------------------------------- helpers
# Nothing below here needs editing.

FEATURE_RE = re.compile(r"\s*[\(\[]\s*(?:feat\.?|ft\.?|featuring|with)\s+([^)\]]+)[\)\]]", re.I)
PRODUCER_RE = re.compile(r"\s*[\(\[]\s*(?:prod\.?(?:\s+by)?|produced\s+by)\s+([^)\]]+)[\)\]]", re.I)


def slugify(text):
    """'Cold Water Cycle' -> 'cold-water-cycle'"""
    text = re.sub(r"[^\w\s-]", "", str(text)).strip().lower()
    return re.sub(r"[\s_-]+", "-", text) or "untitled"


_DATE_FORMATS = [
    "%Y-%m-%d",       # 2026-11-07
    "%B %d, %Y",      # November 7, 2026
    "%B %d %Y",       # November 7 2026
    "%b %d, %Y",      # Nov 7, 2026
    "%b %d %Y",       # Nov 7 2026
    "%m/%d/%Y",       # 11/07/2026
    "%Y/%m/%d",       # 2026/11/07
    "%Y",             # 2026
]


def year_sort_key(year):
    """A "year" field sorts correctly on its own as plain text, but only if
    every entry is the same shape. This turns whatever got typed in — a bare
    year, or a full date with the month spelled out ("November 7, 2026"),
    or an ISO date ("2026-11-07") — into "YYYY-MM-DD" (or "YYYY" for a bare
    year) so chronological order comes out right regardless of how it was
    written. It only affects sorting: the field still displays exactly as
    typed everywhere else. Anything unrecognized is returned unchanged, so
    an unusual format just won't sort perfectly rather than breaking."""
    text = str(year or "").strip()
    if not text:
        return ""
    for fmt in _DATE_FORMATS:
        try:
            parsed = datetime.strptime(text, fmt)
        except ValueError:
            continue
        return f"{parsed.year:04d}" if fmt == "%Y" else parsed.strftime("%Y-%m-%d")
    return text


def _split_names(text):
    return [name.strip() for name in re.split(r",|&|\band\b", text) if name.strip()]


def _paragraphs(value):
    """Turn a pasted bio into a list of paragraphs.

    Blank lines split paragraphs; single line breaks inside a paragraph are
    ignored, so text that wraps mid-sentence still reads correctly. A list of
    strings works too, if you'd rather keep paragraphs separate yourself.
    """
    if not value:
        return []
    chunks = value if isinstance(value, list) else re.split(r"\n\s*\n", str(value).strip())
    out = []
    for chunk in chunks:
        chunk = " ".join(str(chunk).split())
        if chunk:
            out.append(chunk)
    return out





def _as_list(value):
    if not value:
        return []
    return value if isinstance(value, list) else [value]


def _pull_credits(title):
    """Read '(feat. X)' and '(prod. Y)' out of a track title."""
    features, producers = [], []

    for match in FEATURE_RE.finditer(title):
        features += _split_names(match.group(1))
    for match in PRODUCER_RE.finditer(title):
        producers += _split_names(match.group(1))

    clean = PRODUCER_RE.sub("", FEATURE_RE.sub("", title)).strip()
    return clean, features, producers


def _normalize_track(track, index):
    if isinstance(track, str):
        track = {"title": track}
    track = dict(track)

    title, features, producers = _pull_credits(track.get("title", ""))
    track["title"] = title
    track["features"] = _as_list(track.get("features")) or features
    track["producers"] = _as_list(track.get("producers")) or producers
    track["url"] = track.get("url", "")
    track["index"] = index
    track["number"] = index + 1
    track["slug"] = track.get("slug") or slugify(title)
    return track


def _normalize_project(project, index):
    project = dict(project)
    project["index"] = index
    project["slug"] = project.get("slug") or slugify(project.get("title", ""))
    project["kind"] = project.get("kind") or "Album"
    project["year"] = project.get("year", "")
    project["cover"] = project.get("cover", "")
    project["url"] = project.get("url", "")
    project["music_video"] = project.get("music_video", "")
    collab = project.get("collab", "")
    project["collab"] = _split_names(collab) if isinstance(collab, str) else [c for c in _as_list(collab) if str(c).strip()]
    project["bio"] = _paragraphs(project.get("bio"))
    project["tracks"] = [
        _normalize_track(t, i)
        for i, t in enumerate(project.get("tracks", []))
        if not (isinstance(t, str) and not t.strip())
    ]

    # Two tracks with the same title (a re-recording, an "Intro" on two
    # separate tapes, whatever) would otherwise collide on the same URL —
    # keep the first as-is and number the rest so every track's link stays
    # unique.
    seen = {}
    for track in project["tracks"]:
        base = track["slug"]
        seen[base] = seen.get(base, 0) + 1
        if seen[base] > 1:
            track["slug"] = f"{base}-{seen[base]}"

    return project


def _normalize_single(single, index):
    if isinstance(single, str):
        single = {"title": single}
    single = dict(single)

    title, features, producers = _pull_credits(single.get("title", ""))
    single["title"] = title
    single["features"] = _as_list(single.get("features")) or features
    single["producers"] = _as_list(single.get("producers")) or producers
    single["index"] = index
    single["slug"] = single.get("slug") or slugify(title)
    single["year"] = single.get("year", "")
    single["cover"] = single.get("cover", "")
    single["bio"] = _paragraphs(single.get("bio"))
    single["url"] = single.get("url", "")
    single["music_video"] = single.get("music_video", "")
    return single


def _normalize_artist(artist):
    artist = dict(artist)
    artist["slug"] = artist.get("slug") or slugify(artist.get("name", ""))
    artist["image"] = artist.get("image", "")
    artist["aliases"] = [a for a in _as_list(artist.get("aliases")) if str(a).strip()]
    artist["dob"] = artist.get("dob", "")
    artist["dead"] = str(artist.get("dead", "")).strip().lower() == "yes"
    artist["bio"] = _paragraphs(artist.get("bio"))
    artist["collectives"] = [c for c in _as_list(artist.get("collectives")) if str(c).strip()]

    links = artist.get("links") or {}
    artist["links"] = {
        "spotify": links.get("spotify", ""),
        "youtube_music": links.get("youtube_music", ""),
        "soundcloud": links.get("soundcloud", ""),
    }

    artist["projects"] = [
        _normalize_project(p, i)
        for i, p in enumerate(artist.get("projects", []))
        if p.get("title")
    ]
    artist["singles"] = [
        _normalize_single(s, i)
        for i, s in enumerate(artist.get("singles", []))
        if (s if isinstance(s, str) else s.get("title", "")).strip()
    ]

    # Two projects (or two singles) whose titles differ only in punctuation —
    # "SAVIOR" and "SAVIOR: +++" both slugify to "savior" — would otherwise
    # collide on the same URL and silently shadow one another. Keep the
    # first as-is and number the rest, same as duplicate track titles.
    for group in (artist["projects"], artist["singles"]):
        seen = {}
        for item in group:
            base = item["slug"]
            seen[base] = seen.get(base, 0) + 1
            if seen[base] > 1:
                item["slug"] = f"{base}-{seen[base]}"

    artist["initials"] = "".join(w[0] for w in artist["name"].split()[:2]).upper() or "?"
    return artist


def _normalize_collective(collective):
    collective = dict(collective)
    collective["slug"] = collective.get("slug") or slugify(collective.get("name", ""))
    collective["image"] = collective.get("image", "")
    collective["bio"] = _paragraphs(collective.get("bio"))
    collective["current_members"] = [
        m for m in _as_list(collective.get("current_members")) if str(m).strip()
    ]
    collective["former_members"] = [
        m for m in _as_list(collective.get("former_members")) if str(m).strip()
    ]
    return collective


def get_artists():
    """Every artist, alphabetical."""
    return sorted(
        (_normalize_artist(a) for a in ARTISTS if a.get("name")),
        key=lambda a: a["name"].lower(),
    )


def get_total_track_count():
    """Every track on every project, plus every single, across all artists —
    a clean count of every song in the catalog."""
    total = 0
    for artist in get_artists():
        for project in artist["projects"]:
            total += len(project["tracks"])
        total += len(artist["singles"])
    return total


def get_artist(slug):
    for artist in get_artists():
        if artist["slug"] == slug:
            return artist
    return None


def get_project(artist, project_slug):
    for project in artist["projects"]:
        if project["slug"] == project_slug:
            return project
    return None


def get_single(artist, single_slug):
    for single in artist["singles"]:
        if single["slug"] == single_slug:
            return single
    return None


def get_collectives():
    """Every collective, alphabetical."""
    return sorted(
        (_normalize_collective(c) for c in COLLECTIVES if c.get("name")),
        key=lambda c: c["name"].lower(),
    )


def get_collective(slug):
    for collective in get_collectives():
        if collective["slug"] == slug:
            return collective
    return None


# ---------------------------------------------------------------- name matching
#
# Used to turn a plain name (a collective member, a producer credit) into a
# link, if that name matches an existing artist. Matching is case-insensitive
# and checks aliases too, so "Nett" finds Nettspend's page.

def _name_key(name):
    return " ".join(str(name).split()).strip().lower()


def name_key(name):
    """Public wrapper for _name_key, used by app.py to line up templates
    with the same canonicalization used here."""
    return _name_key(name)


def build_artist_name_index():
    """normalized name/alias -> artist dict, for every artist."""
    index = {}
    for artist in get_artists():
        index[_name_key(artist["name"])] = artist
        for alias in artist["aliases"]:
            index.setdefault(_name_key(alias), artist)
    return index


def build_collective_name_index():
    """normalized collective name -> collective dict."""
    return {_name_key(c["name"]): c for c in get_collectives()}


def find_artist_by_name(name):
    return build_artist_name_index().get(_name_key(name))


def find_collective_by_name(name):
    return build_collective_name_index().get(_name_key(name))


# ---------------------------------------------------------------- duplicate songs
#
# The same song sometimes shows up more than once for one artist — as its
# own single AND as a track on an album ("The Whole World Is Free" is both),
# or on an album and again on that album's deluxe ("Roc" is on both High
# Anxiety and its deluxe, More Anxiety). Rather than showing/searching two
# pages for one song, every occurrence resolves to a single "canonical" one:
#
#   1. If the song exists as its own single, the single wins.
#   2. Otherwise, if it's on more than one project, the non-deluxe / original
#      one wins (a project counts as a deluxe if "deluxe" appears in its
#      "kind" or its title — so "More Anxiety" with kind "Deluxe" is caught
#      automatically). If more than one candidate is still non-deluxe, the
#      earliest year wins.
#   3. Otherwise, whichever occurrence came first.
#
# This only compares songs within the SAME artist — two different artists
# happening to title a song the same thing are not duplicates of each other.

def _project_is_deluxe(project):
    text = (str(project.get("kind") or "") + " " + str(project.get("title") or "")).lower()
    return "deluxe" in text


def build_canonical_track_map(artist):
    """normalized song title -> the one occurrence (a single, or a specific
    project + track) that every other occurrence of that title should point
    to instead of having its own page."""
    occurrences = {}

    for single in artist["singles"]:
        key = _name_key(single["title"])
        occurrences.setdefault(key, []).append({
            "is_single": True,
            "is_deluxe": False,
            "year": str(single.get("year") or ""),
            "descriptor": {"type": "single", "slug": single["slug"]},
        })

    for project in artist["projects"]:
        deluxe = _project_is_deluxe(project)
        for track in project["tracks"]:
            key = _name_key(track["title"])
            occurrences.setdefault(key, []).append({
                "is_single": False,
                "is_deluxe": deluxe,
                "year": str(project.get("year") or ""),
                "descriptor": {
                    "type": "track",
                    "project_slug": project["slug"],
                    "track_index": track["index"],
                    "track_slug": track["slug"],
                },
            })

    canonical = {}
    for key, occs in occurrences.items():
        if len(occs) == 1:
            canonical[key] = occs[0]["descriptor"]
            continue
        singles = [o for o in occs if o["is_single"]]
        if singles:
            canonical[key] = singles[0]["descriptor"]
            continue
        pool = [o for o in occs if not o["is_deluxe"]] or occs
        canonical[key] = sorted(pool, key=lambda o: year_sort_key(o["year"]))[0]["descriptor"]

    return canonical


def _is_canonical_track(canonical_map, title, project_slug, track_index):
    canon = canonical_map.get(_name_key(title))
    return (
        canon is not None
        and canon["type"] == "track"
        and canon["project_slug"] == project_slug
        and canon["track_index"] == track_index
    )


def _is_canonical_single(canonical_map, title, single_slug):
    canon = canonical_map.get(_name_key(title))
    return canon is not None and canon["type"] == "single" and canon["slug"] == single_slug


# ---------------------------------------------------------------- producer credits
#
# Scans every track and single in the catalog and groups them by producer
# name, so a producer credit can link to "every song they're credited on" —
# whether or not that producer also has their own artist page.

def build_producer_index():
    """normalized producer name -> {name, slug, artist_match, credits: [...]}"""
    artist_index = build_artist_name_index()
    index = {}

    def add_credit(producer_name, credit):
        key = _name_key(producer_name)
        if not key:
            return
        entry = index.setdefault(
            key, {"name": str(producer_name).strip(), "slug": slugify(producer_name), "credits": []}
        )
        entry["credits"].append(credit)

    for artist in get_artists():
        canonical = build_canonical_track_map(artist)
        for project in artist["projects"]:
            for track in project["tracks"]:
                if not _is_canonical_track(canonical, track["title"], project["slug"], track["index"]):
                    continue
                for producer in track["producers"]:
                    add_credit(producer, {
                        "kind": "track",
                        "artist_name": artist["name"],
                        "artist_slug": artist["slug"],
                        "project_title": project["title"],
                        "project_slug": project["slug"],
                        "track_title": track["title"],
                        "track_index": track["index"],
                        "track_slug": track["slug"],
                        "year": project["year"],
                        "url": track["url"],
                    })
        for single in artist["singles"]:
            for producer in single["producers"]:
                add_credit(producer, {
                    "kind": "single",
                    "artist_name": artist["name"],
                    "artist_slug": artist["slug"],
                    "single_title": single["title"],
                    "single_slug": single["slug"],
                    "year": single["year"],
                    "url": single["url"],
                })

    for key, entry in index.items():
        entry["artist_match"] = artist_index.get(key)

    return index


def get_producer(slug):
    for entry in build_producer_index().values():
        if entry["slug"] == slug:
            return entry
    return None


def get_top_producers(limit=5):
    """The producers with the most credits across the whole catalog, most
    credited first — powers the homepage's "Top 5 Producers" panel."""
    entries = list(build_producer_index().values())
    entries.sort(key=lambda e: len(e["credits"]), reverse=True)
    return entries[:limit]


def get_producer_credits_for_artist(artist):
    """Every track/single anywhere in the catalog where this artist (by
    name or alias) is credited as a producer — used for their Producer-mode
    view."""
    names = {_name_key(artist["name"])} | {_name_key(a) for a in artist["aliases"]}
    credits = []
    for key, entry in build_producer_index().items():
        if key in names:
            credits.extend(entry["credits"])
    credits.sort(key=lambda c: year_sort_key(c.get("year")), reverse=True)
    return credits


def get_featured_singles(artist):
    """Singles that belong to OTHER artists but credit this artist as a
    feature — so a song like Che's "KickAss (Pull Up Pls)" featuring
    Nettspend shows up on Nettspend's page too, linking to the same single
    page rather than a copy of it."""
    names = {_name_key(artist["name"])} | {_name_key(a) for a in artist["aliases"]}
    results = []
    for other in get_artists():
        if other["slug"] == artist["slug"]:
            continue
        for single in other["singles"]:
            if any(_name_key(f) in names for f in single["features"]):
                single = dict(single)
                single["owner_slug"] = other["slug"]
                single["owner_name"] = other["name"]
                results.append(single)
    return results


def get_collab_projects(artist):
    """Projects that belong to OTHER artists but list this artist as a
    collaborator ("collab") — so a joint project shows up on both artists'
    pages, linking to the same project page rather than a copy of it."""
    names = {_name_key(artist["name"])} | {_name_key(a) for a in artist["aliases"]}
    results = []
    for other in get_artists():
        if other["slug"] == artist["slug"]:
            continue
        for project in other["projects"]:
            if any(_name_key(c) in names for c in project["collab"]):
                project = dict(project)
                project["owner_slug"] = other["slug"]
                project["owner_name"] = other["name"]
                results.append(project)
    return results


def get_newest_releases(limit=3):
    """The most recently dated projects and singles across every artist,
    newest first — powers the homepage's "Newest Releases" panel. Each item
    carries enough to describe it on its own: artist, cover, kind/date, and
    for a single its features/producers (a whole project doesn't have one
    clear set of credits to show, since each of its tracks can differ)."""
    items = []
    for artist in get_artists():
        for project in artist["projects"]:
            items.append({
                "is_single": False,
                "title": project["title"],
                "artist_name": artist["name"],
                "artist_slug": artist["slug"],
                "cover": project["cover"],
                "year": project["year"],
                "kind_label": project["kind"],
                "track_count": len(project["tracks"]),
                "features": [],
                "producers": [],
                "slug": project["slug"],
            })
        for single in artist["singles"]:
            items.append({
                "is_single": True,
                "title": single["title"],
                "artist_name": artist["name"],
                "artist_slug": artist["slug"],
                "cover": single["cover"],
                "year": single["year"],
                "kind_label": "Single",
                "track_count": None,
                "features": single["features"],
                "producers": single["producers"],
                "slug": single["slug"],
            })

    items.sort(key=lambda i: year_sort_key(i["year"]), reverse=True)
    return items[:limit]