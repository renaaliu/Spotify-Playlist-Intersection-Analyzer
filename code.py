# Rena Liu

# export SPOTIPY_CLIENT_ID='af520fd93a334f3a8d3b5bb024095f48'
# export SPOTIPY_CLIENT_SECRET='53ce2af7f47b4c6db890b61b0a48f790'
# export SPOTIPY_REDIRECT_URI='http://google.com/'

import spotipy
import sys
import spotipy.util as util

spotify = spotipy.Spotify()

scope = 'user-library-read'

if len(sys.argv) > 1:
    username = sys.argv[1]
else:
    print("Usage: %s username" % (sys.argv[0],))
    sys.exit()     

token = util.prompt_for_user_token(username, scope)

if token:
    sp = spotipy.Spotify(auth=token)
    results = sp.current_user_saved_tracks()
    for item in results['items']:
        track = item['track']
        print(track['name'] + ' - ' + track['artists'][0]['name'])
else:
    print("Can't get token for", username)