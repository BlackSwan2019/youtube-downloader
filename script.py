"""Script for downloading many YouTube videos"""

import subprocess
from bs4 import BeautifulSoup

HTML_FILEPATH = r'C:\Users\Ben\Documents\Development\youtube-download\fullSource.html'

htmlFile = open(HTML_FILEPATH, 'r', encoding='utf8')

htmlContent = htmlFile.read()

parsedHtml = BeautifulSoup(htmlContent, 'html.parser')

containerElement = parsedHtml.find('div', id="contents")

if containerElement:
    videoList = containerElement.find_all(id='video-title')

    if videoList:
        for video in videoList:
            videoTitle = video.get_text().strip(' \n')
            videoHref = video['href']

            print(f' ============================================ \n Downloading {
                videoTitle} \n ============================================')

            YT_DLP_COMMAND = r'C:\Users\Ben\Desktop\yt-dlp.exe'
            OUTPUT_PATH = r'C:\Users\Ben\Documents\Development\youtube-download\downloads'

            videoUrl = 'https://youtube.com' + videoHref

            subprocess.run(
                [YT_DLP_COMMAND, '-x', '--audio-format', 'mp3', '--paths', OUTPUT_PATH, videoUrl], check=True)
    else:
        print('No videos found in container element.')
else:
    print('Container element not found.')
