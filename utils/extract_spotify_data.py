import os 
import requests 
import pandas 
import datetime
import logging



# Database location

# User id spotify 
USER_ID=os.getenv('USER_SPOTIFY_ID')
# Token generated on spotify for developers
TOKEN=os.environ.get('SPOTIFY_TOKEN')


print(USER_ID)
print(TOKEN)
