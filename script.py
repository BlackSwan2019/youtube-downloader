# import subprocess
from bs4 import BeautifulSoup

htmlFile = open(
    r'C:\Users\Ben\Documents\Development\youtube-download\source.html', 'r', encoding='utf8')

htmlContent = htmlFile.read()

parsedHtml = BeautifulSoup(htmlContent, 'html.parser')

element = parsedHtml.find('div', id="contents")

if element:
    childElements = element.find_all(id='video-title')

    for htmlNode in childElements:
        # print(htmlNode)
        videoTitle = htmlNode.get_text().strip(' \n')
        videoHref = htmlNode['href']
        print('Video: ' + videoTitle)
        print('URL: ' + 'https://youtube.com' + videoHref)

# subprocess.run(["C:\\Users\Ben\Desktop\yt-dlp.exe", "https://youtube.com/watch?v=d-FWb0qROIg&amp;list=LL&amp;index=694&amp;pp=gAQBiAQB8AUB"])
