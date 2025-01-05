from xml.dom import IndexSizeErr

from dotenv import dotenv_values
import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

#SPOTIFY CREDENTIALS
secrets = dotenv_values(".env") # type->dict

scope = "playlist-modify-private"

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope=scope, 
        redirect_uri="http://example.com",
        client_id=secrets.get("CLIENT_ID"), # .get() does not produce KeyError
        client_secret=secrets.get("CLIENT_SECRET_CODE"),
        show_dialog=True,
        cache_path="token.txt",
        username=secrets.get("USER_NAME"),
    )
)
user_id = sp.current_user()["id"] #unique user id of the spotify user

#scraping the billboard website
date = input("Which year do you want to travel to? Type the date in the format YYYY-MM-DD : ")
year = date.split('-')[0] #YYYY

URL = f"https://www.billboard.com/charts/hot-100/{date}/"
head =  {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}
response = requests.get(URL, headers = head)
# print(response.text)

soup = BeautifulSoup(response.text, "html.parser")

# song_list = [title.getText().replace("\n\n\t\n\t\n\t\t\n\t\t\t\t\t", "").replace("\t\t\n\t\n", "") for title in soup.select("li ul li h3")]
song_list = [song.getText().strip() for song in soup.select("li ul li h3")]
print(song_list)

with open(f"song_list_{date}.txt", mode = "w") as file:
    for song in song_list:
        file.write(f"{song}\n")

song_uris = []
for song in song_list:
    result = sp.search(q = f"track:{song} year:{year}", type = "track")
    # print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"Song: '{song}' is not in the spotify. Skipped.")

print(song_uris)

#creating a private playlist
playlist = sp.user_playlist_create(user = user_id, name = f"top100songfrom{date}", public = False, description="Created using Python")
sp.playlist_add_items(playlist_id = playlist["id"], items = song_uris)

print(f"successfully added all the top 100 Track from {date}")
