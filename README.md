# Purpose

This script will download all the videos in a YouTube liked-list (only the audio right now).

# How to use

1. Open up your YouTube liked-videos list. Example [here](https://www.youtube.com/playlist?list=LL).
2. Open Chrome webtools and inspect HTML.
3. Look for the element that has an ID of "contents".
4. Copy the element.
5. Create a source.html file in the root of the project with the copied contents.
6. Run `python script.py`
7. Script will download each video and extract audio, placing each file in the "downloads" folder.
