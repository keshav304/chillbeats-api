from flask import Flask, jsonify

app = Flask(__name__)

songs = [
    {
        "name": "Today Feels Like Everyday",
        "artist": "Mama Aiuto ",
        "audio": "https://mp3.chillhop.com/serve.php/?mp3=9908",
        "cover": "https://i.scdn.co/image/ab67616d00004851d48d24735fd4af023ede3aa1"
    },
    {
        "name": "Inverno",
        "artist": "Cloudchord ",
        "audio": "https://mp3.chillhop.com/serve.php/?mp3=9734",
        "cover": "https://i.scdn.co/image/ab67616d0000485135db1818ab7690078ebd38f0"
    },
    {
        "name": "With Time",
        "artist": "Leavv, The Field Tapes ",
        "audio": "https://mp3.chillhop.com/serve.php/?mp3=9547",
        "cover": "https://i.scdn.co/image/ab67616d000048519dcdf7b88cb45810b19a7895"
    },
    {
        "name": "Loving Someone You Lost",
        "artist": "The Field Tapes, tender spring, Nuum ",
        "audio": "https://mp3.chillhop.com/serve.php/?mp3=9789",
        "cover": "https://i.scdn.co/image/ab67616d000048513d2e66180f92ab0df64dae93"
    },
    {
        "name": "Upstate",
        "artist": "Philanthrope, Brock Berrigan, The Field Tapes ",
        "audio": "https://mp3.chillhop.com/serve.php/?mp3=9653",
        "cover": "https://i.scdn.co/image/ab67616d000048517ba1bea501d32e1d0e464240"
    },
    {
        "name": "There and Back",
        "artist": "Shopan ",
        "audio": "https://mp3.chillhop.com/serve.php/?mp3=9709",
        "cover": "https://i.scdn.co/image/ab67616d00004851323572cf8cbe8220b9f1c624"
    },
    {
        "name": "Sodium",
        "artist": "Philanthrope, Tesk ",
        "audio": "https://mp3.chillhop.com/serve.php/?mp3=5664",
        "cover": "https://i.scdn.co/image/ab67616d00004851f963b0b01c5a4822976a9fcb"
    },
    {
        "name": "Snowland Sunset",
        "artist": "Stan Forebee, The Field Tapes, Josh Jacobson, Kennebec ",
        "audio": "https://mp3.chillhop.com/serve.php/?mp3=9730",
        "cover": "https://i.scdn.co/image/ab67616d0000485168a6ad6e704c4df456045555"
    },
    {
        "name": "Paved Paths",
        "artist": "Leavv ",
        "audio": "https://mp3.chillhop.com/serve.php/?mp3=9544",
        "cover": "https://i.scdn.co/image/ab67616d000048519dcdf7b88cb45810b19a7895"
    },
    {
        "name": "Lilo",
        "artist": "Middle School, The Field Tapes ",
        "audio": "https://mp3.chillhop.com/serve.php/?mp3=9785",
        "cover": "https://i.scdn.co/image/ab67616d000048513d2e66180f92ab0df64dae93"
    },
    {
        "name": "Bliss",
        "artist": "Misha, Jussi Halme ",
        "audio": "https://mp3.chillhop.com/serve.php/?mp3=9590",
        "cover": "https://i.scdn.co/image/ab67616d000048514dbbff68622228d0949f9803"
    },
    {
        "name": "A Deeper Understanding",
        "artist": "Aso, Aviino ",
        "audio": "https://mp3.chillhop.com/serve.php/?mp3=9703",
        "cover": "https://i.scdn.co/image/ab67616d00004851167060f24de584b9f5cfbb68"
    },
    {
        "name": "Clockwork",
        "artist": "Philanthrope, tusken. ",
        "audio": "https://mp3.chillhop.com/serve.php/?mp3=5658",
        "cover": "https://i.scdn.co/image/ab67616d0000485104d722d62d4b30479ce68509"
    },
    {
        "name": "Bloom",
        "artist": "Blue Wednesday, Shopan ",
        "audio": "https://mp3.chillhop.com/serve.php/?mp3=9901",
        "cover": "https://i.scdn.co/image/ab67616d00004851a6edabcbfde28527f5ea0db8"
    },
    {
        "name": "You and I",
        "artist": "Melodiesinfonie ",
        "audio": "https://mp3.chillhop.com/serve.php/?mp3=9725",
        "cover": "https://i.scdn.co/image/ab67616d00004851c0444c84c0c9cfd2b9278a6c"
    },
    {
        "name": "Hidden Structure",
        "artist": "Leavv, Flitz&Suppe ",
        "audio": "https://mp3.chillhop.com/serve.php/?mp3=9541",
        "cover": "https://i.scdn.co/image/ab67616d000048519dcdf7b88cb45810b19a7895"
    },
    {
        "name": "Magenta Forever",
        "artist": "Aviino ",
        "audio": "https://mp3.chillhop.com/serve.php/?mp3=9749",
        "cover": "https://i.scdn.co/image/ab67616d0000485181f81abf4a6f8c3a23aaca1a"
    },
    {
        "name": "Perfume",
        "artist": "Nymano, sadtoi ",
        "audio": "https://mp3.chillhop.com/serve.php/?mp3=9576",
        "cover": "https://i.scdn.co/image/ab67616d0000485185ec9cf30c620e93e742f292"
    },
    {
        "name": "Les Mouvements d'Hiver",
        "artist": "L'IndÃ©cis, sadtoi ",
        "audio": "https://mp3.chillhop.com/serve.php/?mp3=9697",
        "cover": "https://i.scdn.co/image/ab67616d000048510ee1824cd2cc8038b7a53b1b"
    },
    {
        "name": "DÃ©jÃ\\xa0 Vu",
        "artist": "Blue Wednesday, Shopan ",
        "audio": "https://mp3.chillhop.com/serve.php/?mp3=9898",
        "cover": "https://i.scdn.co/image/ab67616d00004851a6edabcbfde28527f5ea0db8"
    },
    {
        "name": "Not A Cloud In Sight",
        "artist": "Aviino ",
        "audio": "https://mp3.chillhop.com/serve.php/?mp3=9745",
        "cover": "https://i.scdn.co/image/ab67616d0000485181f81abf4a6f8c3a23aaca1a"
    },
    {
        "name": "Sunday Mornings",
        "artist": "Nymano, JK the Sage ",
        "audio": "https://mp3.chillhop.com/serve.php/?mp3=9572",
        "cover": "https://i.scdn.co/image/ab67616d0000485185ec9cf30c620e93e742f292"
    },
    {
        "name": "Oasis",
        "artist": "Makzo ",
        "audio": "https://mp3.chillhop.com/serve.php/?mp3=9811",
        "cover": "https://i.scdn.co/image/ab67616d00004851ef41dca876323ddef2d211a3"
    },
    {
        "name": "Willow",
        "artist": "Philanthrope, Brock Berrigan, The Field Tapes ",
        "audio": "https://mp3.chillhop.com/serve.php/?mp3=9660",
        "cover": "https://i.scdn.co/image/ab67616d000048517ba1bea501d32e1d0e464240"
    },
    {
        "name": "Such Great Heights",
        "artist": "Middle School, Aviino ",
        "audio": "https://mp3.chillhop.com/serve.php/?mp3=9894",
        "cover": "https://i.scdn.co/image/ab67616d00004851a8f7de2a74868f13d1a92e67"
    },
    {
        "name": "Our Star",
        "artist": "niquo ",
        "audio": "https://mp3.chillhop.com/serve.php/?mp3=9721",
        "cover": "https://i.scdn.co/image/ab67616d0000485135db1818ab7690078ebd38f0"
    },
    {
        "name": "Rest Until Dark",
        "artist": "Sleepy Fish ",
        "audio": "https://mp3.chillhop.com/serve.php/?mp3=9515",
        "cover": "https://i.scdn.co/image/ab67616d00004851959318b95ce2797f3d6e5548"
    },
    {
        "name": "Slim Bobby",
        "artist": "Aviino ",
        "audio": "https://mp3.chillhop.com/serve.php/?mp3=9742",
        "cover": "https://i.scdn.co/image/ab67616d0000485181f81abf4a6f8c3a23aaca1a"
    },
    {
        "name": "One Last Call",
        "artist": "Nymano, Kanisan, Mau ",
        "audio": "https://mp3.chillhop.com/serve.php/?mp3=9567",
        "cover": "https://i.scdn.co/image/ab67616d0000485185ec9cf30c620e93e742f292"
    },
    {
        "name": "Hereafter",
        "artist": "Makzo ",
        "audio": "https://mp3.chillhop.com/serve.php/?mp3=9808",
        "cover": "https://i.scdn.co/image/ab67616d00004851ef41dca876323ddef2d211a3"
    },
    {
        "name": "Droplets",
        "artist": "Philanthrope ",
        "audio": "https://mp3.chillhop.com/serve.php/?mp3=9657",
        "cover": "https://i.scdn.co/image/ab67616d000048517ba1bea501d32e1d0e464240"
    },
    {
        "name": "Vivid.",
        "artist": "chromonicci ",
        "audio": "https://mp3.chillhop.com/serve.php/?mp3=9889",
        "cover": "https://i.scdn.co/image/ab67616d000048517ad3d29b2bb029dc51b30c19"
    },
    {
        "name": "Cruisin",
        "artist": "Loop Schrauber, TRIBEZ. ",
        "audio": "https://mp3.chillhop.com/serve.php/?mp3=9715",
        "cover": "https://i.scdn.co/image/ab67616d0000485135db1818ab7690078ebd38f0"
    },
    {
        "name": "Envision",
        "artist": "dryhope ",
        "audio": "https://mp3.chillhop.com/serve.php/?mp3=8437",
        "cover": "https://i.scdn.co/image/532390784e57d2391f67671f268365351adb58b6"
    },
    {
        "name": "Where The Streets Are Cold & Lonely",
        "artist": "Mama Aiuto ",
        "audio": "https://mp3.chillhop.com/serve.php/?mp3=9909",
        "cover": "https://i.scdn.co/image/ab67616d00004851d48d24735fd4af023ede3aa1"
    },
    {
        "name": "Almost Tomorrow",
        "artist": "Liphe ",
        "audio": "https://mp3.chillhop.com/serve.php/?mp3=9735",
        "cover": "https://i.scdn.co/image/ab67616d00004851e98e0e15aa0eb6b7af70bac9"
    },
    {
        "name": "Zenith",
        "artist": "Leavv ",
        "audio": "https://mp3.chillhop.com/serve.php/?mp3=9548",
        "cover": "https://i.scdn.co/image/ab67616d000048519dcdf7b88cb45810b19a7895"
    },
    {
        "name": "Cloud Carpets",
        "artist": "The Field Tapes, Ezzy, Wowflower ",
        "audio": "https://mp3.chillhop.com/serve.php/?mp3=9791",
        "cover": "https://i.scdn.co/image/ab67616d000048513d2e66180f92ab0df64dae93"
    },
    {
        "name": "Trenches",
        "artist": "Philanthrope, Sleepy Fish ",
        "audio": "https://mp3.chillhop.com/serve.php/?mp3=9654",
        "cover": "https://i.scdn.co/image/ab67616d00004851ff6a7a75706206f36433f3a0"
    },
    {
        "name": "Limitless.",
        "artist": "chromonicci ",
        "audio": "https://mp3.chillhop.com/serve.php/?mp3=9886",
        "cover": "https://i.scdn.co/image/ab67616d000048517ad3d29b2bb029dc51b30c19"
    },
    {
        "name": "5 am",
        "artist": "Ruck P, Shuko ",
        "audio": "https://mp3.chillhop.com/serve.php/?mp3=9710",
        "cover": "https://i.scdn.co/image/ab67616d00004851722571008347f858d8ef2947"
    },
    {
        "name": "Foggy Road",
        "artist": "Toonorth ",
        "audio": "https://mp3.chillhop.com/serve.php/?mp3=7868",
        "cover": "https://i.scdn.co/image/ab67616d0000485162321e7f629cdf49f5eb01b9"
    },
    {
        "name": "Exhale",
        "artist": "Blue Wednesday, tender spring ",
        "audio": "https://mp3.chillhop.com/serve.php/?mp3=9732",
        "cover": "https://i.scdn.co/image/ab67616d0000485135db1818ab7690078ebd38f0"
    },
    {
        "name": "Aqueduct",
        "artist": "Leavv ",
        "audio": "https://mp3.chillhop.com/serve.php/?mp3=9545",
        "cover": "https://i.scdn.co/image/ab67616d000048519dcdf7b88cb45810b19a7895"
    },
    {
        "name": "Harbor",
        "artist": "Stan Forebee, The Field Tapes, azula, Francis ",
        "audio": "https://mp3.chillhop.com/serve.php/?mp3=9786",
        "cover": "https://i.scdn.co/image/ab67616d000048513d2e66180f92ab0df64dae93"
    },
    {
        "name": "Maple Leaf Pt.2",
        "artist": "Philanthrope ",
        "audio": "https://mp3.chillhop.com/serve.php/?mp3=9651",
        "cover": "https://i.scdn.co/image/ab67616d000048517ba1bea501d32e1d0e464240"
    },
    {
        "name": "Unlisted",
        "artist": "Amparo ",
        "audio": "https://mp3.chillhop.com/serve.php/?mp3=9704",
        "cover": "https://i.scdn.co/image/ab67616d00004851b78b75ee79dbfb1eca1ff50c"
    },
    {
        "name": "The End",
        "artist": "Philanthrope, Fujitsu ",
        "audio": "https://mp3.chillhop.com/serve.php/?mp3=5327",
        "cover": "https://i.scdn.co/image/ab67616d00004851f963b0b01c5a4822976a9fcb"
    },
    {
        "name": "Lax Incense",
        "artist": "Mama Aiuto, DaphnÃ© ",
        "audio": "https://mp3.chillhop.com/serve.php/?mp3=9905",
        "cover": "https://i.scdn.co/image/ab67616d00004851d48d24735fd4af023ede3aa1"
    },
    {
        "name": "Hau Nalu",
        "artist": "FloFilz, Kostral One ",
        "audio": "https://mp3.chillhop.com/serve.php/?mp3=9726",
        "cover": "https://i.scdn.co/image/ab67616d00004851909d5a384e9a6b9bceaa7d32"
    },
    {
        "name": "Dancing Droplets",
        "artist": "Leavv ",
        "audio": "https://mp3.chillhop.com/serve.php/?mp3=9542",
        "cover": "https://i.scdn.co/image/ab67616d000048519dcdf7b88cb45810b19a7895"
    },
    {
        "name": "Still Life Dreamtime",
        "artist": "Aviino ",
        "audio": "https://mp3.chillhop.com/serve.php/?mp3=9750",
        "cover": "https://i.scdn.co/image/ab67616d0000485181f81abf4a6f8c3a23aaca1a"
    },
    {
        "name": "Cold Outside",
        "artist": "Nymano ",
        "audio": "https://mp3.chillhop.com/serve.php/?mp3=9577",
        "cover": "https://i.scdn.co/image/ab67616d0000485185ec9cf30c620e93e742f292"
    },
    {
        "name": "Going Back",
        "artist": "SwÃ¸rn ",
        "audio": "https://mp3.chillhop.com/serve.php/?mp3=9699",
        "cover": "https://i.scdn.co/image/ab67616d00004851c461983cf7468082540becb2"
    },
    {
        "name": "Day One",
        "artist": "Blue Wednesday, Shopan ",
        "audio": "https://mp3.chillhop.com/serve.php/?mp3=9899",
        "cover": "https://i.scdn.co/image/ab67616d00004851a6edabcbfde28527f5ea0db8"
    },
    {
        "name": "Yesterdays",
        "artist": "xander. ",
        "audio": "https://mp3.chillhop.com/serve.php/?mp3=9723",
        "cover": "https://i.scdn.co/image/ab67616d0000485135db1818ab7690078ebd38f0"
    },
    {
        "name": "Witch Hat",
        "artist": "Sleepy Fish ",
        "audio": "https://mp3.chillhop.com/serve.php/?mp3=9516",
        "cover": "https://i.scdn.co/image/ab67616d00004851959318b95ce2797f3d6e5548"
    },
    {
        "name": "Bluetooth Ringtone (interlude)",
        "artist": "Aviino ",
        "audio": "https://mp3.chillhop.com/serve.php/?mp3=9746",
        "cover": "https://i.scdn.co/image/ab67616d0000485181f81abf4a6f8c3a23aaca1a"
    },
    {
        "name": "Distance",
        "artist": "Nymano, Ouska, Anetta Morozova ",
        "audio": "https://mp3.chillhop.com/serve.php/?mp3=9573",
        "cover": "https://i.scdn.co/image/ab67616d0000485185ec9cf30c620e93e742f292"
    },
    {
        "name": "Longing",
        "artist": "Makzo ",
        "audio": "https://mp3.chillhop.com/serve.php/?mp3=9812",
        "cover": "https://i.scdn.co/image/ab67616d00004851ef41dca876323ddef2d211a3"
    },
    {
        "name": "Anemone",
        "artist": "Philanthrope, Dotlights ",
        "audio": "https://mp3.chillhop.com/serve.php/?mp3=9661",
        "cover": "https://i.scdn.co/image/ab67616d000048517ba1bea501d32e1d0e464240"
    },
    {
        "name": "Flashback",
        "artist": "Blue Wednesday, Shopan ",
        "audio": "https://mp3.chillhop.com/serve.php/?mp3=9896",
        "cover": "https://i.scdn.co/image/ab67616d00004851a6edabcbfde28527f5ea0db8"
    },
    {
        "name": "Creswick",
        "artist": "Aviino ",
        "audio": "https://mp3.chillhop.com/serve.php/?mp3=9743",
        "cover": "https://i.scdn.co/image/ab67616d0000485181f81abf4a6f8c3a23aaca1a"
    },
    {
        "name": "False Hope",
        "artist": "Nymano, Pandrezz ",
        "audio": "https://mp3.chillhop.com/serve.php/?mp3=9570",
        "cover": "https://i.scdn.co/image/ab67616d0000485185ec9cf30c620e93e742f292"
    },
    {
        "name": "Seascape",
        "artist": "Makzo ",
        "audio": "https://mp3.chillhop.com/serve.php/?mp3=9809",
        "cover": "https://i.scdn.co/image/ab67616d00004851ef41dca876323ddef2d211a3"
    },
    {
        "name": "Plants",
        "artist": "Philanthrope, Ian Ewing, Sleepy Fish ",
        "audio": "https://mp3.chillhop.com/serve.php/?mp3=9658",
        "cover": "https://i.scdn.co/image/ab67616d000048517ba1bea501d32e1d0e464240"
    },
    {
        "name": "Reality.",
        "artist": "chromonicci ",
        "audio": "https://mp3.chillhop.com/serve.php/?mp3=9890",
        "cover": "https://i.scdn.co/image/ab67616d000048517ad3d29b2bb029dc51b30c19"
    },
    {
        "name": "Bandwidth",
        "artist": "Gustav Gustav, Dave Kellner ",
        "audio": "https://mp3.chillhop.com/serve.php/?mp3=9718",
        "cover": "https://i.scdn.co/image/ab67616d0000485135db1818ab7690078ebd38f0"
    },
    {
        "name": "Du Bassin au Muret",
        "artist": "sadtoi ",
        "audio": "https://mp3.chillhop.com/serve.php/?mp3=8960",
        "cover": "https://i.scdn.co/image/ab67616d00004851f24b2d91590ce7fbf131c27c"
    },
    {
        "name": "Getting Stronger",
        "artist": "Montell Fish ",
        "audio": "https://mp3.chillhop.com/serve.php/?mp3=9736",
        "cover": "https://i.scdn.co/image/ab67616d0000485135db1818ab7690078ebd38f0"
    },
    {
        "name": "Mirage",
        "artist": "Nymano, j'san ",
        "audio": "https://mp3.chillhop.com/serve.php/?mp3=9565",
        "cover": "https://i.scdn.co/image/ab67616d00004851a257c0b8d09962756161f882"
    },
    {
        "name": "Flowers",
        "artist": "The Field Tapes, xander. ",
        "audio": "https://mp3.chillhop.com/serve.php/?mp3=9793",
        "cover": "https://i.scdn.co/image/ab67616d000048513d2e66180f92ab0df64dae93"
    },
    {
        "name": "Serendipity",
        "artist": "Philanthrope, The Field Tapes ",
        "audio": "https://mp3.chillhop.com/serve.php/?mp3=9655",
        "cover": "https://i.scdn.co/image/ab67616d000048517ba1bea501d32e1d0e464240"
    },
    {
        "name": "Fantasy.",
        "artist": "chromonicci ",
        "audio": "https://mp3.chillhop.com/serve.php/?mp3=9887",
        "cover": "https://i.scdn.co/image/ab67616d000048517ad3d29b2bb029dc51b30c19"
    },
    {
        "name": "Frozen Firs",
        "artist": "goosetaf, xander., Anbuu ",
        "audio": "https://mp3.chillhop.com/serve.php/?mp3=9712",
        "cover": "https://i.scdn.co/image/ab67616d0000485135db1818ab7690078ebd38f0"
    },
    {
        "name": "Lost Love",
        "artist": "Toonorth ",
        "audio": "https://mp3.chillhop.com/serve.php/?mp3=7869",
        "cover": "https://i.scdn.co/image/ab67616d0000485118533c653909fa2091f2b8ae"
    },
    {
        "name": "Small Town Palm Trees",
        "artist": "Mama Aiuto ",
        "audio": "https://mp3.chillhop.com/serve.php/?mp3=9907",
        "cover": "https://i.scdn.co/image/ab67616d00004851d48d24735fd4af023ede3aa1"
    },
    {
        "name": "Riverside Drive",
        "artist": "auv ",
        "audio": "https://mp3.chillhop.com/serve.php/?mp3=9733",
        "cover": "https://i.scdn.co/image/ab67616d00004851d6b4363236623e456c74eb9e"
    },
    {
        "name": "What Was Before",
        "artist": "Philanthrope, Leavv ",
        "audio": "https://mp3.chillhop.com/serve.php/?mp3=9546",
        "cover": "https://i.scdn.co/image/ab67616d000048519dcdf7b88cb45810b19a7895"
    },
    {
        "name": "Peaches",
        "artist": "Philanthrope, The Field Tapes ",
        "audio": "https://mp3.chillhop.com/serve.php/?mp3=9788",
        "cover": "https://i.scdn.co/image/ab67616d000048513d2e66180f92ab0df64dae93"
    },
    {
        "name": "Wildlife",
        "artist": "Philanthrope, chromonicci ",
        "audio": "https://mp3.chillhop.com/serve.php/?mp3=9652",
        "cover": "https://i.scdn.co/image/ab67616d000048517ba1bea501d32e1d0e464240"
    },
    {
        "name": "Snowstalgia",
        "artist": "invention_ ",
        "audio": "https://mp3.chillhop.com/serve.php/?mp3=9708",
        "cover": "https://i.scdn.co/image/ab67616d0000485135db1818ab7690078ebd38f0"
    },
    {
        "name": "Murmuration",
        "artist": "Blue Wednesday, Shopan ",
        "audio": "https://mp3.chillhop.com/serve.php/?mp3=6526",
        "cover": "https://i.scdn.co/image/fd52c9201ea0d1ebd75c7fd0ec374cf7db6d3fef"
    },
    {
        "name": "Frozen in Time",
        "artist": "Kendall Miles ",
        "audio": "https://mp3.chillhop.com/serve.php/?mp3=9729",
        "cover": "https://i.scdn.co/image/ab67616d0000485135db1818ab7690078ebd38f0"
    },
    {
        "name": "Flushing the Stairs",
        "artist": "Leavv ",
        "audio": "https://mp3.chillhop.com/serve.php/?mp3=9543",
        "cover": "https://i.scdn.co/image/ab67616d0000485109e54abaf147550b81b535c0"
    },
    {
        "name": "Sugarless",
        "artist": "The Field Tapes, Aviino ",
        "audio": "https://mp3.chillhop.com/serve.php/?mp3=9784",
        "cover": "https://i.scdn.co/image/ab67616d000048513d2e66180f92ab0df64dae93"
    },
    {
        "name": "Blurry",
        "artist": "Nymano, Hyume ",
        "audio": "https://mp3.chillhop.com/serve.php/?mp3=9578",
        "cover": "https://i.scdn.co/image/ab67616d0000485185ec9cf30c620e93e742f292"
    },
    {
        "name": "String Along",
        "artist": "MiscÃ©l ",
        "audio": "https://mp3.chillhop.com/serve.php/?mp3=9702",
        "cover": "https://i.scdn.co/image/ab67616d00004851ff6a7a75706206f36433f3a0"
    },
    {
        "name": "Flke",
        "artist": "Philanthrope ",
        "audio": "https://mp3.chillhop.com/serve.php/?mp3=5248",
        "cover": "https://i.scdn.co/image/ab67616d00004851f963b0b01c5a4822976a9fcb"
    },
    {
        "name": "Home Court",
        "artist": "Blue Wednesday, Shopan ",
        "audio": "https://mp3.chillhop.com/serve.php/?mp3=9900",
        "cover": "https://i.scdn.co/image/ab67616d00004851a6edabcbfde28527f5ea0db8"
    },
    {
        "name": "Back When Marmots Used to Smoke",
        "artist": "Mr. KÃ¤fer, Flitz&Suppe ",
        "audio": "https://mp3.chillhop.com/serve.php/?mp3=9724",
        "cover": "https://i.scdn.co/image/ab67616d0000485135db1818ab7690078ebd38f0"
    },
    {
        "name": "Butterfly",
        "artist": "Sleepy Fish ",
        "audio": "https://mp3.chillhop.com/serve.php/?mp3=9517",
        "cover": "https://i.scdn.co/image/ab67616d00004851959318b95ce2797f3d6e5548"
    },
    {
        "name": "Hotel Lobby Birthday Party",
        "artist": "Aviino, Oliv ",
        "audio": "https://mp3.chillhop.com/serve.php/?mp3=9747",
        "cover": "https://i.scdn.co/image/ab67616d0000485181f81abf4a6f8c3a23aaca1a"
    },
    {
        "name": "New Horizons",
        "artist": "Nymano, Epektase ",
        "audio": "https://mp3.chillhop.com/serve.php/?mp3=9575",
        "cover": "https://i.scdn.co/image/ab67616d0000485185ec9cf30c620e93e742f292"
    },
    {
        "name": "Departure",
        "artist": "Makzo ",
        "audio": "https://mp3.chillhop.com/serve.php/?mp3=9813",
        "cover": "https://i.scdn.co/image/ab67616d00004851ef41dca876323ddef2d211a3"
    },
    {
        "name": "Habitat",
        "artist": "Philanthrope, Kendall Miles ",
        "audio": "https://mp3.chillhop.com/serve.php/?mp3=9662",
        "cover": "https://i.scdn.co/image/ab67616d000048517ba1bea501d32e1d0e464240"
    },
    {
        "name": "Toofpick",
        "artist": "Blue Wednesday, Shopan ",
        "audio": "https://mp3.chillhop.com/serve.php/?mp3=9897",
        "cover": "https://i.scdn.co/image/ab67616d00004851a6edabcbfde28527f5ea0db8"
    },
    {
        "name": "Deeper",
        "artist": "Aviino ",
        "audio": "https://mp3.chillhop.com/serve.php/?mp3=9744",
        "cover": "https://i.scdn.co/image/ab67616d0000485181f81abf4a6f8c3a23aaca1a"
    },
    {
        "name": "The Ride Home (interlude)",
        "artist": "Nymano ",
        "audio": "https://mp3.chillhop.com/serve.php/?mp3=9571",
        "cover": "https://i.scdn.co/image/ab67616d0000485185ec9cf30c620e93e742f292"
    },
    {
        "name": "Melancholy",
        "artist": "Makzo ",
        "audio": "https://mp3.chillhop.com/serve.php/?mp3=9810",
        "cover": "https://i.scdn.co/image/ab67616d00004851ef41dca876323ddef2d211a3"
    },
    {
        "name": "Soil",
        "artist": "Philanthrope, Guillaume Muschalle ",
        "audio": "https://mp3.chillhop.com/serve.php/?mp3=9659",
        "cover": "https://i.scdn.co/image/ab67616d000048517ba1bea501d32e1d0e464240"
    },
    {
        "name": "Casual",
        "artist": "Middle School ",
        "audio": "https://mp3.chillhop.com/serve.php/?mp3=9893",
        "cover": "https://i.scdn.co/image/ab67616d00004851ccd44b174bb9ed0f929377e9"
    },
    {
        "name": "Tuesday",
        "artist": "Comodo ",
        "audio": "https://mp3.chillhop.com/serve.php/?mp3=9720",
        "cover": "https://i.scdn.co/image/ab67616d0000485135db1818ab7690078ebd38f0"
    },
    {
        "name": "Tumbling",
        "artist": "SwÃ¸rn ",
        "audio": "https://mp3.chillhop.com/serve.php/?mp3=9188",
        "cover": "https://i.scdn.co/image/ab67616d000048519f0f86b54e7ca8870fac0ede"
    },
    {
        "name": "Constance",
        "artist": "fantompower ",
        "audio": "https://mp3.chillhop.com/serve.php/?mp3=9737",
        "cover": "https://i.scdn.co/image/ab67616d0000485135db1818ab7690078ebd38f0"
    },
    {
        "name": "Train Ride",
        "artist": "Nymano, Philanthrope ",
        "audio": "https://mp3.chillhop.com/serve.php/?mp3=9566",
        "cover": "https://i.scdn.co/image/ab67616d0000485185ec9cf30c620e93e742f292"
    },
    {
        "name": "Through Trees",
        "artist": "Sleepy Fish, The Field Tapes ",
        "audio": "https://mp3.chillhop.com/serve.php/?mp3=9794",
        "cover": "https://i.scdn.co/image/ab67616d000048513d2e66180f92ab0df64dae93"
    },
    {
        "name": "Pine and Oak",
        "artist": "Philanthrope, The Field Tapes ",
        "audio": "https://mp3.chillhop.com/serve.php/?mp3=9656",
        "cover": "https://i.scdn.co/image/ab67616d000048517ba1bea501d32e1d0e464240"
    },
    {
        "name": "Parallel.",
        "artist": "chromonicci ",
        "audio": "https://mp3.chillhop.com/serve.php/?mp3=9888",
        "cover": "https://i.scdn.co/image/ab67616d000048517ad3d29b2bb029dc51b30c19"
    },
    {
        "name": "Ocean View",
        "artist": "G Mills, Kyle McEvoy, Luke Otwell ",
        "audio": "https://mp3.chillhop.com/serve.php/?mp3=9713",
        "cover": "https://i.scdn.co/image/ab67616d0000485135db1818ab7690078ebd38f0"
    },
    {
        "name": "Ful Off",
        "artist": "Nokiaa, Nofeels ",
        "audio": "https://mp3.chillhop.com/serve.php/?mp3=7947",
        "cover": "https://i.scdn.co/image/8921d86bb0819ff728291ad21d1ebf121db7598b"
    }
]




@app.route('/', methods=['GET'])
def index():
    songs_list = jsonify(results=songs)
    return songs_list


@app.route('/<int:no>', methods=['GET'])
def definiteSongs(no):
    if no > 111:
        return "oops! maximum song that can be selected are 111"
    song = songs[0:no]
    songs_list = jsonify(results=song)
    return songs_list

