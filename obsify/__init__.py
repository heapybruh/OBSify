from .config import Config, Widget
from .rest import Rest
from .spotify import Spotify
from .terminal import Terminal
import json
import os
from msvcrt import getch
import _thread
import asyncio

__version__ = "v1.0"

def start():
    os.system(f"title OBSify (Version: {__version__})")
    
    config = _load_config()
    _thread.start_new_thread(Rest(config, _login_spotify(config)).run, ())

    Terminal.print("OBSify loaded successfully, have fun using it!")
    Terminal.how_to_use()

    loop = asyncio.get_event_loop()

    try:
        loop.run_forever()
    finally:
        loop.close()

def _load_config() -> Config:
    with open("./config.json") as file:
        config = json.load(file)
        
        try:
            config = Config(config["client_id"], config["client_secret"], config["redirect_url"], Widget(config["widget"]["position"]))
            Terminal.success("Config: Loaded successfully")
        except:
            Terminal.error(f"Config: Couldn't load")
            _close()

        return config

def _login_spotify(config: Config) -> Spotify:
        try:
            spotify = Spotify(config.client_id, config.client_secret, config.redirect_url)
            user = spotify.current_user()["display_name"]
            Terminal.success(f"Spotify: Logged in as {user}")
        except:
            Terminal.error(f"Spotify: Couldn't log in")
            _close()

        return spotify

def _close():
    print("\nPress any key to exit...")
    getch()
    exit()