# OBSify - Spotify Widget for OBS written in HTML and Python

## Introducing OBSify
OBSify is a Script that checks which song is being played in your Spotify Client and creates a Spotify Widget inside a .html file by using HTML & Python!  

## How to use?
1. Go to [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/)
2. Create an App
3. Open the App's Dashboard
4. Click **Edit Settings**
5. In **Redirect URLs** write http://localhost:9000
6. Copy **Redirect URL**, **Client ID** and **Client Secret**
7. Paste them into **config.json**
8. Open **start.bat**
9. A website should open with the Spotify Authorization, accept it
10. Open OBS Studio
11. Add **Browser Source** to scene
12. Check **local file** and use **index.html** which is in [html folder](https://github.com/Heapy1337/OBSify/tree/main/html)
13. Done!

## Optional settings
- Enable **Shutdown source when not visible** and **Refresh browser when scene becomes active** in **Properties** of a **Browser Source**
- You can change positions of the widget by setting **Position** option to **"leftup"**, **"leftdown"**, **"center"**, **"rightup"** or **"rightdown"** in [widget_config.json](https://github.com/Heapy1337/OBSify/blob/main/html/widget_config.json)

## How does it look like?
![OBSifyScreenshot](https://i.imgur.com/t2gSTjt.png)
