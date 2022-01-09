import math
import spotipy
import random
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth

#secret will be made invalid on Monday, if you need it again lmk
id="2e7959faa85f44d6b2e859064f9dd1aa"
secrt="2514bb7ab37e449ba19db71e9f43bfc2"

def authentic_version(sp):

    results = sp.current_user_saved_tracks(limit=1, offset=0)
    n = results['total'] #gives number of saved tracks.
    search_length = 20 #how many random tracks to check, keep under a hundred
    hi_score_track = ""
    hi_score = 0
    #loop finds n random songs
    for i in range(search_length):
        #limit means grab 1 track @ a time
        #offset gets a random number from 0 to (n-1) which is the index of the track
        results = sp.current_user_saved_tracks(limit=1, offset=random.randrange(0,(n-1)))
        if (len(results) == 0): #failsafe for no liked songs
            break
        track = results['items'][0]['track'] # 'items' is a list of size 1 that contains a dict with a 'track' entry
        uri = track['uri'] #unique id of track
        af = sp.audio_features(uri)[0] #the audio features call to the API gets the audio features from a number of tracks, we pass 1
                                       #we get a list of size 1 so we access index 0
        #af is a dictionary with key-value pairs for each stat based on its name, which can be found on the spotify web api reference page
        v = af['valence']
        d = af['danceability']
        e = af['energy']
        #score formula
        score = 0.15*e+0.6*d+0.6*v
        #logic to figure out highest score, printout is to show program is running
        if (score > hi_score):
            hi_score_track = track['uri']
            hi_score = score
            print(i, '*')
        else:
            print(i)
    print(sp.track(hi_score_track)['artists'][0]['name'], " - ", sp.track(hi_score_track)['name'])
    print("score= {0:.3f}".format(hi_score))

def main():
    scopes = ["user-library-read", "playlist-modify-public"]
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope= scopes, client_id = id, client_secret = secrt, redirect_uri= 'http://localhost:8080'))
    authentic_version(sp)

main()