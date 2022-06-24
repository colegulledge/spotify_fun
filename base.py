import os
import json
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util
import pandas as pd

print('hi cole')
cid ="xxxx"
secret = "xxx"

os.environ['SPOTIPY_CLIENT_ID']= cid
os.environ['SPOTIPY_CLIENT_SECRET']= secret
os.environ['SPOTIPY_REDIRECT_URI']='http://localhost:8889/callback'

username = "colegulledge"
client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
scope = 'user-top-read'
#scope = 'user-library-read'
token = util.prompt_for_user_token(username, scope)


if token:
    sp = spotipy.Spotify(auth=token)
    results = sp.audio_features(tracks = ['spotify:track:4KGyQfes7t5BiaoBvs380e', 'spotify:track:7LpApBtRMSNREMhddGSAXo', 'spotify:track:1yOc6FBOVD6zBwOMxiSEEv', 'spotify:track:72OxJJsVrZN5JHIdcciKeT', 'spotify:track:7BaDRi8gmRnOducT6KaOfc', 'spotify:track:1X6Egb4TC623Dml93iU1xX', 'spotify:track:7zPxIh1c3kJaNwmjdZ3GQX', 'spotify:track:7wi9bON987aTdTtU3oHrBB', 'spotify:track:2RpMHnKzl9tUM8I7DBsjqJ', 'spotify:track:2oAtisBiEx0HeRYu4xo3bT', 'spotify:track:3JMfsPV8XU4xDozJA5pStN', 'spotify:track:4svzXvwon2jxvQnSo6NOdF', 'spotify:track:34u64KvdcABENtNpPOMONw', 'spotify:track:7nzsY8vlnKdvGOEE0rjAXZ', 'spotify:track:2CbtdkBeW9Znt4vXTOafAl', 'spotify:track:7ne867SdHbopGYjxVNyRFM', 'spotify:track:1VdTDxpoYvKIALowR8Bxdo', 'spotify:track:43QhrhgRrH9NWy6eoUro4X', 'spotify:track:2wb2FptR9dbAw9TIQpMfZ1', 'spotify:track:1420BGhbXGkIJtbtBlfpYE', 'spotify:track:0p5eZCY0R7uNCZS1YDtIYI', 'spotify:track:0seTertVGvHrEJu7hlIWRq', 'spotify:track:4fPBB44eDH71YohayI4eKV', 'spotify:track:7gsArdm7rk6X6wsMr2QKWS', 'spotify:track:7npKbWXEH9hapuitQa03ch', 'spotify:track:0IiQ3gvsK7OTYoDvBUKukm', 'spotify:track:4CQNoWzcxealvmuGGzZmpQ', 'spotify:track:4OkPamOn5GofkOQu64Z4eR', 'spotify:track:6NGvyhGjKSKkyN3yc4YNhD', 'spotify:track:1ONWW6AtqqwjhMdQ74n2fM', 'spotify:track:4M2kErclJ5eWkjXxy8qDYp', 'spotify:track:5ruzrDWcT0vuJIOMW7gMnW', 'spotify:track:0wD5f13PbeI08AwwuDeNrV', 'spotify:track:608xszaAxVh4m7NcKJiAbF', 'spotify:track:08l9WKDuRyGeStQ9ojTlFh', 'spotify:track:1AsNfUfuGmQGXbrjoPQl8j', 'spotify:track:3Y4rUyw7XBCK6hGHCOt6rp', 'spotify:track:0lY7lvNeBASEoAzPj4Des1', 'spotify:track:4Ig9HspUaKy2cz6YA8pb6O', 'spotify:track:5l4K6OAwpIUlAsItJoZwYr', 'spotify:track:1TYRcvY3JTYoLVhADPpDH5', 'spotify:track:4iwpCp7qdDLngGI3gsVTza', 'spotify:track:4m6uJViB1sb3OXErHUkkWk', 'spotify:track:2O07FF1DMc1oRDlkIo33FC', 'spotify:track:2TY2GcWmTmcE6L40jYC9Xv', 'spotify:track:7bfocP7GYoLOutUYpTI8tx', 'spotify:track:4atMrAadB7dS8xn9vfk9PQ', 'spotify:track:6MIo2NS5cx125JqauDiFvP', 'spotify:track:5U2hi2KoW2iknnBXxspglI', 'spotify:track:0jBE7Fn78EAvmIs3dCd6GO'])
    for song in range(500):
        list = []
        list.append(results)
        with open('top_100_tracks_features.json', 'w', encoding='utf-8') as f:
            json.dump(list, f, ensure_ascii=False, indent=4)
    print('donezo slut')
else:
    print("Can't get token for", username)