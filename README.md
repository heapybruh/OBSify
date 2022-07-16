# OBSify - Spotify Widget for OBS written in HTML and Python

## Introducing OBSify
OBSify is a Script that checks which song is being played in your Spotify Client and creates a Spotify Widget inside a .html file by using HTML & Python!  

## Requirements
- Python 3.X
- Brain 👍

## How to use?
1. Go to [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/)
2. Create an App
3. Open the App's Dashboard
4. Click **Edit Settings**
5. Set **Redirect URLs** to `http://localhost:9000`
6. Copy **Redirect URL**, **Client ID**, **Client Secret** and paste them into [config.json](https://github.com/Heapy1337/OBSify/blob/main/config.json)
7. Open **install_requirements.bat**
8. Open **start.bat**
9. A website should open with the Spotify Authorization, accept it
10. Open OBS Studio
11. Add **Browser Source** to scene and open it's **Properties**
13. Check **local file** option and use **index.html** which is in ["html" folder](https://github.com/Heapy1337/OBSify/tree/main/html)
14. Done!

## Optional settings
- Enable **Shutdown source when not visible** and **Refresh browser when scene becomes active** in **Properties** of a **Browser Source**
- You can change position of the widget by setting **Position** option (in [widget_config.json](https://github.com/Heapy1337/OBSify/blob/main/html/widget_config.json)) to :
  - LEFT (leftup, leftcenter, leftdown)
  - CENTER (centerup, center, centerdown)
  - RIGHT (rightup, rightcenter, rightdown)

## How does it look like?
![OBSifyScreenshot](https://i.imgur.com/t2gSTjt.png)
