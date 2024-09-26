import os
from flask import Flask, request, redirect
import google_auth_oauthlib.flow
import google.oauth2.credentials
import googleapiclient.discovery
from google.auth.transport.requests import Request

app = Flask(__name__)

# Set the OAuth 2.0 scopes (YouTube Data API scope for accessing YouTube)
scopes = ['https://www.googleapis.com/auth/youtube.readonly']

# Path to the client secrets file
CLIENT_SECRETS_FILE = 'client_secrets.json'

# Create the OAuth flow
flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(
    CLIENT_SECRETS_FILE,
    scopes=scopes
)

flow.redirect_uri = 'http://localhost:5000/callback'

@app.route('/')
def index():
    return 'Welcome to the YouTube OAuth 2.0 authentication example. <a href="/authorize">Authorize</a>'

@app.route('/authorize')
def authorize():
    authorization_url, state = flow.authorization_url(
        access_type='offline',  # Ensure we get a refresh token
        prompt='consent',  # Force consent screen every time
        include_granted_scopes='true'
    )
    return redirect(authorization_url)

@app.route('/callback')
def callback():
    try:
        code = request.args.get('code')
        if not code:
            return "No code provided in the callback URL."

        flow.fetch_token(code=code)
        credentials = flow.credentials

        access_token = credentials.token
        refresh_token = credentials.refresh_token

        print(f"Access Token: {access_token}")
        print(f"Refresh Token: {refresh_token}")

        with open('tokens.json', 'w') as token_file:
            token_data = {
                "access_token": access_token,
                "refresh_token": refresh_token
            }
            json.dump(token_data, token_file)

        return "Authorization completed. You can close this window."
    except Exception as e:
        print(f"Authorization failed: {str(e)}")
        return "Authorization failed. Please check the logs."


if __name__ == '__main__':
    app.run('localhost', 5000, debug=True)
