"""Script for downloading many YouTube videos"""

import os
import sys
import subprocess
import time
import pickle
import google_auth_oauthlib.flow
import googleapiclient.errors
import googleapiclient.discovery


def get_credentials():
    """Get Google API OAuth credentials"""
    creds = None

    # Check if the token.pickle file exists
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)

    return creds


def get_video_list():
    """Get list of videos from playlist"""
    scopes = ["https://www.googleapis.com/auth/youtube.readonly"]

    # credentials = get_credentials()

    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    # os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "oauth2.json"

    # # Get credentials and create an API client
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes)
    credentials = flow.run_local_server()

    print(credentials)

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials)

    video_list = []
    next_page_token = None

    while True:
        request = youtube.playlistItems().list(
            part="snippet",
            playlistId="LL",
            maxResults=50,
            pageToken=next_page_token
        )
        response = request.execute()

        video_list.extend(response['items'])

        next_page_token = response.get('nextPageToken')

        if not next_page_token:
            break

    return video_list


def create_string(char, n):
    """Create a string of same chars N chars long"""
    return char * n


def download_videos():
    """Download the list of videos"""

    start_time = time.time()

    video_list = get_video_list()

    if not video_list:
        print("No videos found. Exiting script.")
        sys.exit()

    for index, video in enumerate(video_list):
        video_data = video['snippet']
        video_title = video_data['title']
        video_id = video_data['resourceId']['videoId']

        message = f'{index + 1}. Downloading {video_title}'
        equal_signs = create_string('=', len(message))

        print(f' {equal_signs} \n {message} \n {equal_signs}')

        yt_dlp_command = 'yt-dlp.exe'
        output_path = 'downloads'

        video_url = 'https://youtube.com/watch?v=' + video_id

        subprocess.run(
            [yt_dlp_command, '-x', '--audio-format', 'mp3', '--paths', output_path, video_url], check=True)

    end_time = time.time()

    elapsed_time = end_time - start_time

    hours = int(elapsed_time // 3600)
    minutes = int((elapsed_time % 3600) // 60)
    seconds = int(elapsed_time % 60)

    print(f'Elapsed time: {hours}h {minutes}m {seconds}s')


download_videos()
