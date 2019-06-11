import spotipy
import sys

from spotipy.oauth2 import SpotifyClientCredentials

client_credentials_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)

# taking spotify account from command line (for now)
user_id = sys.argv[1]



# If this works: should print all playlists of user

# what is this object type? linked list?
results = spotify.user_playlist(user_id)
playlists = results['items']

while results['next']:
    results = spotify.next(results)
    playlists.extend(results['items'])

for playlist in playlists:
    # is playlist also of dictionary type if you can index it?
    print(playlist['name'])

