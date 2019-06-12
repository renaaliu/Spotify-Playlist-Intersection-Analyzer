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

# ask spotify for user's playlists
playlists1 = spotifyObject.current_user_playlists()

# eventually: spotifyObject.current_user_saved_tracks()

# display autheticated user's playlists (or all saved songs)
print(playlists)

# allow for user to select one


# ask spotify for all the songs in that playlist, save it in code
spotifyObject.user_playlist_track(user, playlist_id=None, fields=None, limit=100, offset=0, market=None)

# authentication process for second person
# display second person's playlists
# allow second person to select
# ask spotify for all the songs in that playlist, save it in code

# compare the saved songs on the two playlists
    if (spotifyObject.current_user_saved_tracks_contains(song) 
        && spotifyObject2.current_user_saved_tracks_contains(song)) {
        intersection.add(song)
    }

# create new/display shared playlist of intersections
