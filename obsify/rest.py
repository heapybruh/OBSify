from .config import Config
from .spotify import Spotify
from flask import Flask
from flask_cors import CORS
import logging

class Rest():
    def __init__(self, config: Config, spotify: Spotify):
        self._config = config
        self._spotify = spotify
        self._flask = Flask("OBSify")
        self._flask.add_url_rule("/spotify", "spotify", self._get_song, methods=["GET"])
        self._flask.add_url_rule("/config", "config", self._get_config, methods=["GET"])

    def _get_song(self):
        try:
            return self._spotify.now_playing().to_dict()
        except:
            return self._flask.aborter(404)
        
    def _get_config(self):
        try:
            return self._config.to_dict()
        except:
            return self._flask.aborter(404)

    def run(self):
        CORS(self._flask)
        logging.getLogger("werkzeug").disabled = True
        self._flask.run(debug=False, host="127.0.0.1", port="7777")