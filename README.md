# OBSify - HTML Spotify Widget for OBS written in Python

## Introducing OBSify
OBSify is a Python App that hosts HTML Website (only on localhost IP) with Spotify Widget in it!  

## How to use?
1. Go to [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/)
2. Create an App
3. Open the App's Dashboard
4. Click **Edit Settings**
5. In **Redirect URLs** write **http://localhost:9000**
6. Copy **Redirect URL**, **Client ID** and **Client Secret**
7. Paste them into **config.json**
8. Open **start.bat**
9. A website should open with the Spotify Authorization, accept it
10. Open OBS Studio
11. Add **Browser Source** to scene
12. URL should be **http://localhost:8000** (Replace 8000 with the port that you set in **webserver_config.json**)
13. (Optional) Scroll down and enable **Shutdown source when not visible** and **Refresh browser when scene becomes ative**

## How does it look like?
![OBSifyScreenshot](https://i.imgur.com/t2gSTjt.png)
