# Purpose

This script will download all the videos in your "Liked videos" playlist (only the audio right now).

# Requirements

* OAuth 2.0 Client ID for YouTube in your Google developer account.
* A local-only oauth2.json file with the OAuth 2.0 client ID token information. Download from the developer dashboard.

# How to use

1. Run `python script.py`
2. Script will engage OAuth 2.0 flow in Chrome. Allow Youtube Downloader access to your YouTube account.
2. Script will download each video from the "Liked videos" playlist and extract audio, placing each file in a "downloads" folder inside the project.
