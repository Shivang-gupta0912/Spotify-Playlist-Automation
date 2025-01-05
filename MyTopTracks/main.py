# Note : This code redirect you 2 times to given REDIRECT_URI, for taking access for the given scopes
# you can name your playlist here also...

import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import dotenv_values

secrets = dotenv_values(".env")

NO_OF_TRACKS = 30 # set no. of tracks you want

scope = ["user-top-read", "playlist-modify-private"]
REDIRECT_URI = "http://localhost:8080"

my_top_tracks = []
my_top_tracks_uris = []

for i in range(2):
        spoa = SpotifyOAuth(
                scope=scope[i],
                client_id=secrets.get("CLIENT_ID"),
                client_secret=secrets.get("CLIENT_SECRET"),
                redirect_uri=REDIRECT_URI,
                username = secrets.get("USER_NAME"),
                show_dialog=True,
                cache_path="token.txt", #use spotipy.SpotifyOAuth.get_access_token() to access the token
        )
        sp = spotipy.Spotify(
            auth_manager=spoa
        )
        user_id = sp.current_user()["id"]

        if i == 0:
                # find top tracks
                for  track in sp.current_user_top_tracks(limit = NO_OF_TRACKS)["items"]:
                        my_top_tracks.append(track["name"])
                        my_top_tracks_uris.append(track["uri"])
                print("Your Top Tracks : ")
                print(my_top_tracks)
                print(my_top_tracks_uris)
                print()
        else:
                # create playlist and add tracks
                name = input("Enter name for the your top tracks playlist: ")
                playlist = sp.user_playlist_create(user= user_id, name = name, public = False, description="Created using Python")
                sp.playlist_add_items(playlist_id = playlist["id"], items = my_top_tracks_uris)

print("Your playlist is created !")