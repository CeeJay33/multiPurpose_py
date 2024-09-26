from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

credentials = Credentials(
    token='ya29.a110AcM612xjwMjVehH9hTgtvJp7JHZJFwnybkbXxhRwutw8PcAnrODROMJkxnC4_EfHWKmnI6fzmTDoHBnTu9RWBpaYa69qlTXpyPAqmGNWiZ5BGEnVyBfjOGfUk7F3AiJWVuiDR-tFDiXq0LQUD87DkSKgKwDHrKxv5IE7NHfaaCgYKAUMSARISFQHGX2Mi_DRxXQG5RuUQjuF99Jl7wA0175',
    refresh_token='1//0113Qh2kjTsA9ItCgYIARAAGAMSNwF-L9IrJ1z18fSrPtsX06aNkt1uu75STlPTVUEO8oAn3oXrrj3tUdwgYjL4MtTSHLBLVW0cF8k',
    token_uri='https://oauth2.googleapis.com/token',
    client_id='1155604783383-b61981thmm0nq0859llkpgkdpfu9nqbq.apps.googleusercontent.com',
    client_secret='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'
)

youtube = build('youtube', 'v3', credentials=credentials)

channel_id = 'UCqlnazcN2bVcwRZGeDgz1Zw' 

email_addresses = [
    'atrucklogistics@gmail.com',
    'chrismiracle911@gmail.com',
]

for email in email_addresses:
    response = youtube.subscriptions().insert(
        part='snippet',
        body={
            'snippet': {
                'resourceId': {
                    'kind': 'youtube#channel',
                    'channelId': channel_id
                }
            }
        }
    ).execute()
    print(f"Subscribed to channel: {channel_id} for user authenticated with email.")
