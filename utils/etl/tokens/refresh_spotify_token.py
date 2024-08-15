import os 
import time 
import requests
from dotenv import load_dotenv

# Load environnement variables 
load_dotenv()

client_id = os.getenv('SPOTIFY_CLIENT_ID')
client_secret = os.getenv('SPOTIFY_CLIENT_SECRET')
refresh_token = os.getenv('SPOTIFY_REFRESH_TOKEN')
token_url = "https://accounts.spotify.com/api/token"


# Globals to store token and expiration time 
access_token = None 
token_expiration_time = 0

# create function that refreshed token 
def refresh_access_token():
    """
    Function allow to refresh spotify expired token
    """
    global access_token, token_expiration_time

    token_data = {
        "grant_type": "refresh_token",
        "refresh_token": refresh_token,
        "client_id": client_id,
        "client_secret": client_secret,
    }

    token_headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }

    r = requests.post(token_url, data=token_data, headers=token_headers)
    response_data = r.json()

    # Update the global access token and expiration time
    access_token = response_data["access_token"]
    expires_in = response_data.get("expires_in", 3600)  # Default is 1 hour
    token_expiration_time = time.time() + expires_in

    #print(f"Access token refreshed. New token: {access_token}")

# create functin that check if acces token is expired and refresh it
def get_access_token():
    """
    Function allow to check if token was expired and if refresh if so
    """
    global access_token, token_expiration_time

    # If the token has expired or is not set, refresh it
    if access_token is None or time.time() >= token_expiration_time:
        refresh_access_token()

    return access_token

# create function to get spotify profile with refreshed token  
def get_spotify_user_profile():
    token = get_access_token()
    headers = {
        "Authorization": f"Bearer {token}"
    }

    user_profile_url = "https://api.spotify.com/v1/me"
    r = requests.get(user_profile_url, headers=headers)
    return r.json()

# # Example usage
# profile = get_spotify_user_profile()
# print(profile)

