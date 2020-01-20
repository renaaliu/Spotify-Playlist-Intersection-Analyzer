# Rena Liu
# Rena's Side Project Spotify account: sdb66l96nr80vo0q97urr06fo
'''
export SPOTIPY_CLIENT_ID='af520fd93a334f3a8d3b5bb024095f48'
export SPOTIPY_CLIENT_SECRET='53ce2af7f47b4c6db890b61b0a48f790'
export SPOTIPY_REDIRECT_URI='http://0.0.0.0:8000/'
'''

'''
part II

'''

import spotipy
import sys
import spotipy.util as util

spotify = spotipy.Spotify()

scope = 'user-library-read'

if len(sys.argv) > 2:
    username = sys.argv[1]
    # playlist = sys.argv[2]
    username2 = sys.argv[2]
else:
    # print("Please enter %s username and a playlist to analyze" % (sys.argv[0],))
    print("Please enter %s both user's usernames" % (sys.argv[0],))
    sys.exit()

token = util.prompt_for_user_token(username, scope)

if token:
    sp = spotipy.Spotify(auth=token)
    results = sp.current_user_saved_tracks(limit = 10)
    print(username + "'s Saved Tracks:" + '\n')
    for item in results['items']:
        track = item['track']
        print(track['name'] + ' - ' + track['artists'][0]['name'])
    print('\n')
else:
    print("Can't get token for", username)


token2 = util.prompt_for_user_token(username2, scope)

if token2:
    sp2 = spotipy.Spotify(auth=token2)
    results2 = sp2.current_user_saved_tracks(limit = 10)
    print('\n'+ username2 + "'s Saved Tracks:" + '\n')
    for item2 in results2['items']:
        track2 = item2['track']
        print(track2['name'] + ' - ' + track2['artists'][0]['name'])
    print('\n')
else:
    print("Can't get token for", username2)

# newPlaylist = [item for item in results if item in results2]
print("Playlist Intersection:" + "\n")
for item in results['items']:
    if item in results2['items']:
        track = item['track']
        print(track['name'] + ' - ' + track['artists'][0]['name'])
print('\n')

# scope2 = 'playlist-modify-public'
# token2 = util.prompt_for_user_token(username, scope2)

# if token2:
#     sp2 = spotipy.Spotify(auth=token2)
#     sp2.trace = False
#     results2 = sp2.user_playlist_tracks(username, playlist)
#     print("User 1's Tracks on" + playlist + "Playlist:" + '\n')
#     for item in results2['items']:
#         track = item['track']
#         print(track['name'] + ' - ' + track['artists'][0]['name'])
# else:
#     print("Can't get token for", username)      

# 



