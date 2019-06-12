# If this works: should print all playlists of user
# import spotipy
# import sys

# from spotipy.oauth2 import SpotifyClientCredentials

# client_credentials_manager = SpotifyClientCredentials()
# sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)

# # taking spotify account from command line (for now)
# user_id = sys.argv[1]

# # what is this object type? linked list?
# results = spotify.user_playlist(user_id)
# playlists = results['items']

# while results['next']:
#     results = spotify.next(results)
#     playlists.extend(results['items'])

# for playlist in playlists:
#     # is playlist also of dictionary type if you can index it?
#     print(playlist['name'])



# Add tracks to 'Your Collection' of saved tracks
# import pprint
# import sys

# import spotipy
# import spotipy.util as util

# scope = 'user-library-modify'

# if len(sys.argv) > 1:
#     username = sys.argv[1]
#     # tids = track id
#     # tids = sys.argv[2:]
# else:
#     print("Usage: %s username track-id ..." % (sys.argv[0],))
#     sys.exit()

# token = util.prompt_for_user_token(username, scope)

# if token:
#     sp = spotipy.Spotify(auth=token)
#     sp.trace = False
#     # results = sp.current_user_saved_tracks_add(tracks=tids)
#     pprint.pprint(results)
# else:
#     print("Can't get token for", username)


# Print search results?
# import spotipy
# name = 'Halsey'
# spotify = spotipy.Spotify()
# results = spotify.search(q='artist:' + name, type='artist')
# print(results)

# Print albums from given artist
# import spotipy
# birdy_uri = 'spotify:artist:2WX2uTcsvV5OnS0inACecP'
# spotify = spotipy.Spotify()

# results = spotify.artist_albums(birdy_uri, album_type='album')
# albums = results['items']
# while results['next']:
#     results = spotify.next(results)
#     albums.extend(results['items'])

# for album in albums:
#     print(album['name'])


# album art from given artist
import os
import sys
import json
import spotipy
import webbrowser
import spotipy.util as util
from json.decoder import JSONDecodeError
# Get the username from terminal
username = sys.argv[1]
scope = 'user-read-private user-read-playback-state user-modify-playback-state'
# Erase cache and prompt for user permission
try:
    token = util.prompt_for_user_token(username)
    #, scope) # add scope
except (AttributeError, JSONDecodeError):
    os.remove(f".cache-{username}")
    token = util.prompt_for_user_token(username)
    #, scope) # add scope
# Create our spotify object with permissions
spotifyObject = spotipy.Spotify(auth=token)


