import spotipy
from spotipy.oauth2 import SpotifyOAuth
from threading import Thread
from pathlib import Path
from getpass import getpass
import os
import time
import json

config_json = open("config.json", "r", encoding="utf-8")
config = json.loads(config_json.read())

clear = lambda: os.system("cls")
clear()

try:
    os.remove("html/now_playing.json")
    create_file = Path("html/now_playing.json")
    create_file.touch(exist_ok=True)
except:
    create_file = Path("html/now_playing.json")
    create_file.touch(exist_ok=True)

scope = "user-read-currently-playing"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
                                            client_id=config["client_ID"],
                                            client_secret=config["client_SECRET"],
                                            redirect_uri=config["redirect_url"],
                                            scope=scope,
                                            open_browser=True
                                            ))

current_song_id = None
while True:
    track_info = sp.current_user_playing_track()

    song_name = track_info["item"]["name"]
    song_id = track_info["item"]["id"]
    artists = track_info["item"]["artists"]

    if current_song_id != song_id:
        artist_list = []
        for x in artists:
            artist_list.append(x["name"])

        artist_list = ", ".join(artist_list)

        now_playing = f"Now playing: \"{song_name}\" by {artist_list}"
        print(now_playing)

        data = {
            "song_name" : f"{song_name}",
            "song_id" : f"{song_id}",
            "artist_list" : f"{artist_list}"
        }

        text_file = open("html/now_playing.json", "w", encoding="utf-8")
        json.dump(data, text_file)
        text_file.close()
        current_song_id = song_id
    
    time.sleep(1)