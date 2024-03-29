<div align="center">
 <h1>OBSify</h1>
 <p>Spotify Widget for OBS written in HTML, JavaScript and Python.</p>
</div>

## Requirements
- Python 3.x
- Python modules:

  ```
  colorama
  cursor
  Flask
  Flask_Cors
  spotipy
  ```

## How to use?
1. Go to [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/).
2. Create an App.
3. Go to App's dashboard and edit its settings.
4. Set `Redirect URLs` to `http://localhost:9000`.
5. Rename `config.json.example` to `config.json`.
6. Copy `Redirect URLs`, `Client ID`, `Client secret` and paste them into `config.json`.
7. Install Python modules with `pip install -r requirements.txt --user`.
8. Start the script by using `python main.py`.
9. A website should open with the Spotify authorization, accept it.
10. Open OBS Studio.
11. Add `Browser` source to the scene and open its properties.
12. Check `Local file` option.
13. Click `Browse` and select file: [html/index.html](./html/index.html).

## Optional settings
- Enable `Shutdown source when not visible` and `Refresh browser when scene becomes active` in source's properties.
- You can change position of the widget by setting `position` option (in your config) to:
  - `LEFT` (leftup, leftcenter, leftdown)
  - `CENTER` (centerup, center, centerdown)
  - `RIGHT` (rightup, rightcenter, rightdown)
