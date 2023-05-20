from .song import Song
from .terminal import Terminal
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os

class Spotify():
    def __init__(self, client_id: str, client_secret: str, redirect_url: str):
        self._clear_cache()
        self._client = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_url, scope="user-read-currently-playing", open_browser=True))
        self._now_playing = Song()

    def now_playing(self) -> Song:
        song = self._client.current_user_playing_track()

        artists = [artist["name"] for artist in song["item"]["artists"]]
        title = song["item"]["name"]
        id = song["item"]["id"]
        image_url = song["item"]["album"]["images"][1]["url"]

        song = Song(artists, title, id, image_url)

        if self._now_playing.id != song.id:
            self._now_playing = song
            artists_joined = ", ".join(song.artists)
            Terminal.print(f"Now playing: \"{song.title}\" by {artists_joined}")

        return Song(artists, title, id, image_url)
    
    def current_user(self):
        return self._client.current_user()
    
    def _clear_cache(self):
        try:    
            os.remove(".cache")
        except: 
            pass

        try:    
            os.remove(".cache-user-read-currently-playing")
        except: 
            pass
