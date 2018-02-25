from googleapiclient.discovery import build

API_SERVICE_NAME = 'youtube'
API_VERSION = 'v3'
API_KEY = 'AIzaSyBGvRcUjTaMQi9ry585d09nWdbed7rRdBs'


def get_authenticated_service():
    return build(API_SERVICE_NAME, API_VERSION, developerKey=API_KEY)


def channels_list_by_username(service, **kwargs):
    results = service.channels().list(
        **kwargs
    ).execute()

    print('This channel\'s ID is {}. Its title is {}, and it has {} views.'.format(
        results['items'][0]['id'],
        results['items'][0]['snippet']['title'],
        results['items'][0]['statistics']['viewCount']
    ))


if __name__ == '__main__':
    service = get_authenticated_service()
    channels_list_by_username(
        service,
        part='snippet,contentDetails,statistics',
        # forUsername='caseyneistat',
        id='UCeWxWWNHB2XTt8aKzoq9qbg',
    )
