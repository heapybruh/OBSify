# OBSify - Spotify Widget for OBS written in HTML, JavaScript & Python

## Introducing OBSify
OBSify is a script that checks which song is being played in your Spotify Client and creates a Spotify Widget inside a .html file!  

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
3. Open the App's dashboard
4. Click **"Edit Settings"**
5. Set **"Redirect URLs"** to `http://localhost:9000`
6. Copy **"Redirect URL"**, **"Client ID"**, **"Client Secret"** and paste them into [config.json](./config.json)
7. Install Python modules by using ``pip install -r requirements.txt``
8. Start **main.py** by using ``python main.py``
9. A website should open with the Spotify Authorization, accept it
10. Open OBS Studio
11. Add **Browser** source to the scene and open its **properties**
13. Check **Local file** option
14. Click "Browse" and use [index.html](./html/index.html)
15. Done!

## Optional settings
- Enable **"Shutdown source when not visible"** and **"Refresh browser when scene becomes active"** in **properties**
- You can change position of the widget by setting **"position"** option (in [config.json](./config.json)) to:
  - LEFT (leftup, leftcenter, leftdown)
  - CENTER (centerup, center, centerdown)
  - RIGHT (rightup, rightcenter, rightdown)
