"""Script for downloading many YouTube videos"""

import subprocess
import time
from bs4 import BeautifulSoup


def create_string(char, n):
    """Create a string of same chars N chars long"""
    return char * n


def download_videos():
    """Download the list of videos"""

    start_time = time.time()

    html_filepath = 'source.html'

    html_file = open(html_filepath, 'r', encoding='utf8')

    html_content = html_file.read()

    parsed_html = BeautifulSoup(html_content, 'html.parser')

    container_element = parsed_html.find('div', id="contents")

    if container_element:
        video_list = container_element.find_all(id='video-title')

        if video_list:
            for index, video in enumerate(video_list):
                video_title = video.get_text().strip(' \n')
                video_href = video['href']
                message = f'{index + 1}. Downloading {video_title}'
                equal_signs = create_string('=', len(message))

                print(f' {equal_signs} \n {message} \n {equal_signs}')

                yt_dlp_command = 'yt-dlp.exe'
                output_path = 'downloads'

                video_url = 'https://youtube.com' + video_href

                subprocess.run(
                    [yt_dlp_command, '-x', '--audio-format', 'mp3', '--paths', output_path, video_url], check=True)

            end_time = time.time()

            elapsed_time = end_time - start_time

            hours = int(elapsed_time // 3600)
            minutes = int((elapsed_time % 3600) // 60)
            seconds = int(elapsed_time % 60)

            print(f'Elapsed time: {hours}h {minutes}m {seconds}s')
        else:
            print('No videos found in container element.')
    else:
        print('Container element not found.')


download_videos()
