# Note: This script will redirect you to the specified REDIRECT_URI twice during execution. 
# This is required to obtain access tokens for the specified scopes.

# Importing Dependencies
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import dotenv_values

# Loading Secrets and Constant
secrets = dotenv_values(".env")
NO_OF_TRACKS = 30 # set no. of tracks you want

# Defining variables
scope = ["user-top-read", "playlist-modify-private"]
REDIRECT_URI = "http://localhost:8080"

my_top_tracks = []
my_top_tracks_uris = []

for i in range(2):
        # Authentication and API Connection
        spoa = SpotifyOAuth(
                scope=scope[i],
                client_id=secrets.get("CLIENT_ID"),
                client_secret=secrets.get("CLIENT_SECRET"),
                redirect_uri=REDIRECT_URI,
                username = secrets.get("USER_NAME"),
                show_dialog=True,
                cache_path="token.txt", # Use spotipy.SpotifyOAuth.get_access_token() to access the Token
        )
        sp = spotipy.Spotify(
            auth_manager=spoa
        )
        user_id = sp.current_user()["id"]

        if i == 0:
                # Fetching Top Tracks
                for  track in sp.current_user_top_tracks(limit = NO_OF_TRACKS)["items"]:
                        my_top_tracks.append(track["name"])
                        my_top_tracks_uris.append(track["uri"])
                print("Your Top Tracks : ")
                print(my_top_tracks)
                print(my_top_tracks_uris)
                print()
        else:
                # Creating a Playlist and Adding Tracks
                name = input("Enter name for the your top tracks playlist: ")
                playlist = sp.user_playlist_create(user= user_id, name = name, public = False, description="Created using Python")
                sp.playlist_add_items(playlist_id = playlist["id"], items = my_top_tracks_uris)

print("Your playlist is created !")