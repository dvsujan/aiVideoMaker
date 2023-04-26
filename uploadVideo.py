from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.errors import HttpError
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

def upload_video_to_youtube(video_path, video_title, video_description, video_tags, video_category):
    # Authorization credentials
    CLIENT_SECRET_FILE = 'client_secret.json'
    SCOPES = ['https://www.googleapis.com/auth/youtube.upload']

    # Authentication flow
    flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRET_FILE, SCOPES)
    creds = flow.run_local_server(port=0)

    # YouTube API client
    youtube = build('youtube', 'v3', credentials=creds)

    # Video upload
    try:
        # Create a new video resource
        body = {
            'snippet': {
                'title': video_title,
                'description': video_description,
                'tags': video_tags,
                'categoryId': video_category
            },
            'status': {
                'privacyStatus': 'private'
            }
        }

        # Call the API to upload the video
        response = youtube.videos().insert(
            part='snippet,status',
            body=body,
            media_body=MediaFileUpload(video_path)
        ).execute()

        print('Video upload successful. Video ID:', response['id'])

    except HttpError as e:
        print('An HTTP error %d occurred:\n%s' % (e.resp.status, e.content))
    except Exception as e:
        print('An error occurred:\n%s' % str(e))
