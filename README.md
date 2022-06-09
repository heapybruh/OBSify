# OBSify - HTML Spotify Widget for OBS written in Python

## Introducing OBSify
OBSify is a Python App that hosts HTML Website (only on localhost IP) with Spotify Widget in it!  

## How to use?
### 1st Method (Using **OBSify.py** and **webserver.py**)
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
14. (Optional) Scroll down and enable **Shutdown source when not visible** and **Refresh browser when scene becomes active**

### 2nd Method (Using only **OBSify.py** - RECOMMENDED)
1. Go to [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/)
2. Create an App
3. Open the App's Dashboard
4. Click **Edit Settings**
5. In **Redirect URLs** write **http://localhost:9000**
6. Copy **Redirect URL**, **Client ID** and **Client Secret**
7. Paste them into **config.json**
8. Open **start_only_obsify.bat**
9. A website should open with the Spotify Authorization, accept it
10. Open OBS Studio
11. Add **Browser Source** to scene
12. Check **local file** and use **index.html** which is in **html** folder
14. (Optional) Scroll down and enable **Shutdown source when not visible** and **Refresh browser when scene becomes active**

## How does it look like?
![OBSifyScreenshot](https://i.imgur.com/t2gSTjt.png)
