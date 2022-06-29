
import spotipy
from spotipy.oauth2 import SpotifyOAuth

from pathlib import Path
from getpass import getpass

import sys
import os
import time
import json
import cursor

class NoError:
    def write(self, msg):
        pass

sys.stderr = NoError()

clear = lambda: os.system("cls")
clear()

cursor.hide()

class colors:
    green = '\033[92m'
    red = '\033[91m'
    reset = '\033[0m'

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
    track_info = sp.current_user_playing_track()
    obsify_print(colors.green + "Logged in successfully")
except:
    obsify_print(colors.red + "An error has occurred while logging in")

current_song_id = None
while True:
    try:
        track_info = sp.current_user_playing_track()
    except:
        obsify_print(colors.red + "Couldn't get information about currently playing song")

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