<div align="center">
 <h1>OBSify</h1>
 <p>Spotify Widget for OBS written in HTML, JavaScript and Python</p>
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
1. Go to [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/)
2. Create an App
3. Go to App's dashboard and edit its settings
4. Set **"Redirect URLs"** to `http://localhost:9000`
5. Copy **"Redirect URLs"**, **"Client ID"**, **"Client secret"** and paste them into [config.json](./config.json)
6. Install Python modules by using `pip install -r requirements.txt`
7. Start **main.py** by using `python main.py`
8. A website should open with the Spotify authorization, accept it
9. Open OBS Studio
10. Add **"Browser"** source to the scene and open its properties
11. Check **"Local file"** option
12. Click **"Browse"** and use [index.html](./html/index.html) which is in **"html"** folder
13. Done!

## Optional settings
- Enable **"Shutdown source when not visible"** and **"Refresh browser when scene becomes active"** in source's properties
- You can change position of the widget by setting **"position"** option (in [config.json](./config.json)) to:
  - LEFT (leftup, leftcenter, leftdown)
  - CENTER (centerup, center, centerdown)
  - RIGHT (rightup, rightcenter, rightdown)
