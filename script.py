"""Script for downloading many YouTube videos"""

import subprocess
from bs4 import BeautifulSoup

HTML_FILEPATH = r'C:\Users\Ben\Documents\Development\youtube-download\source.html'

htmlFile = open(HTML_FILEPATH, 'r', encoding='utf8')

htmlContent = htmlFile.read()

parsedHtml = BeautifulSoup(htmlContent, 'html.parser')

element = parsedHtml.find('div', id="contents")

if element:
    childElements = element.find_all(id='video-title')

    for htmlNode in childElements:
        # print(htmlNode)
        # print('\n\n')

        videoTitle = htmlNode.get_text().strip(' \n')
        videoHref = htmlNode['href']

        print('============================================\n' + 'Downloading ' +
              videoTitle + '\n============================================')

        videoUrl = 'https://youtube.com' + videoHref

        subprocess.run(
            [r'C:\Users\Ben\Desktop\yt-dlp.exe', videoUrl], check=True)
