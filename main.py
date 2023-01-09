import spotipy
from spotipy.oauth2 import SpotifyOAuth
import time

scope = "playlist-modify-public"
username = ""

token = SpotifyOAuth(scope=scope, username=username)
spotifyObject = spotipy.Spotify(auth_manager=token)

playlist_name = input("Enter playlist name: ")
playlist_description = input("Enter playlist description: ")

spotifyObject.user_playlist_create(user=username, name=playlist_name, public=True, description=playlist_description)

prePlaylist = spotifyObject.user_playlists(user=username)
playlist = prePlaylist['items'][0]['id']

my_file = open("uris.txt", "r")
data = my_file.read()
data_into_list = data.split("\n")
my_file.close()

# chunks = [data_into_list[x:x+100] for x in range(0, len(data_into_list), 100)]

for uri in data_into_list:
    spotifyObject.user_playlist_add_tracks(user=username, playlist_id=playlist, tracks=[uri])
    time.sleep(1)

print("done")


# with open("uris.txt") as songs:
#     for url in songs:
        # spotifyObject.playlist_add_items(playlist_id=playlist, items=[url], position=None)
        # spotifyObject.user_playlist_add_tracks(user=username, playlist_id=playlist, tracks=[url])