import os 
import requests 
import pandas as pd 
import datetime
import logging
from dotenv import load_dotenv
from tokens.refresh_spotify_token import get_access_token
import json 
# Recover env variables 
load_dotenv()

# Database location

# User id spotify 
USER_ID=os.getenv('SPOTIFY_USER_ID')
# Token generated on spotify for developers
TOKEN=get_access_token()

## define exract_data function

def extract_data() : 
    """
    Function that allowed retrieved data from spotify_token account
    """ 

    ## prepare headers ##
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization' : f'Bearer {TOKEN}'
    }

    # perform requests 
    try : 
        r = requests.get(
            f"https://api.spotify.com/v1/me/player/recently-played?limit=50", 
            headers=headers
        )
    except: 
        raise Exception(f'The spotify went wrong')
    
    if r.status_code!=200: 
        raise Exception(f'Something in the Spotify request went wrong : {r.status_code}')
    
    # Extract the data 
    data = r.json()
    
    # Inisialize the flields we are looking for
    song_names_list = []
    played_at_list = []
    artist_name_list = []
    external_utl_list = []
    popularity_list = []
    track_number_list = []
    track_type_list = []
    timestamps = []
    ids_list = []
    ### Loop through each song to get the info we want ##
    for song in data['items']:
        ids_list.append(song['track']['id'])
        played_at_list.append(song['played_at']) 
        song_names_list.append(song['track']['name'])
        artist_name_list.append(song['track']['album']['artists'][0]['name'])
        external_utl_list.append(song['track']['external_urls']['spotify'])
        popularity_list.append(song['track']['popularity'])
        track_number_list.append(song['track']['track_number'])
        track_type_list.append(song['track']['type'])
        timestamps.append(song['played_at'][0:10])

    song_dict = {
        'song_id': ids_list,
        'song_name': song_names_list,
        'artist_name': artist_name_list,
        'played_at': played_at_list,
        'timestmap': timestamps,
        'url': external_utl_list,
        'popularity' : popularity_list,
        'track_number': track_number_list,
        'track_type': track_type_list, 
        'timestamp': timestamps

    }
    
    song_df = pd.DataFrame(
        song_dict,
        columns=list(song_dict.keys())
    )

    logging.info(song_df)
    return song_df.sort_values(by='played_at')

print(extract_data())
