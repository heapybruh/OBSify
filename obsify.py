import spotipy
from spotipy.oauth2 import SpotifyOAuth
from pathlib import Path
import os
import time
import json
import cursor
import colorama

colorama.init(autoreset=True, strip=True, convert=True)

os.system("cls")
os.remove(".cache")
os.remove(".cache-user-read-currently-playing")

cursor.hide()
class colors:
    green = colorama.Fore.GREEN
    red = colorama.Fore.RED
    reset = colorama.Fore.RESET

def obsify_print(message):
    print(f"[ OBSify ] {message}" + colors.reset)

obsify_print("Loading config...")

try:
    config_json = open("config.json", "r", encoding="utf-8")
    config = json.loads(config_json.read())
    obsify_print(colors.green + "Loaded config successfully")
except:
    obsify_print(colors.red + "An error has occurred while loading config.json")

create_file = Path("html/now_playing.json")
create_file.touch(exist_ok=True)

scope = "user-read-currently-playing"

obsify_print("Logging in...")
try:
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
                                                client_id=config["client_ID"],
                                                client_secret=config["client_SECRET"],
                                                redirect_uri=config["redirect_url"],
                                                scope=scope,
                                                open_browser=True
                                                ))
    obsify_print(colors.green + "Logged in successfully")
except Exception as e:
    obsify_print(colors.red + "An error has occurred while logging in")

current_song_id = None
while True:
    try:
        track_info = sp.current_user_playing_track()
    except:
        obsify_print(colors.red + "Couldn't get information about currently playing song")
        time.sleep(1)
        continue

    song_name = track_info["item"]["name"]
    song_id = track_info["item"]["id"]
    song_image = track_info["item"]["album"]["images"][1]["url"]
    artists = track_info["item"]["artists"]

    if current_song_id != song_id:
        artist_list = []
        for x in artists:
            artist_list.append(x["name"])

        artist_list = ", ".join(artist_list)

        now_playing = f"Now playing: \"{song_name}\" by {artist_list}"
        obsify_print(now_playing)

        data = {
            "song_name" : f"{song_name}",
            "song_id" : f"{song_id}",
            "song_image" : f"{song_image}",
            "artist_list" : f"{artist_list}"
        }

        text_file = open("html/now_playing.json", "w", encoding="utf-8")
        json.dump(data, text_file)
        text_file.close()
        current_song_id = song_id
    
    time.sleep(1)