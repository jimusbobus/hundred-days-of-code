import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# date_choice = input("Enter Date e.g. '2000-08-12'")
date_choice = "1993-06-12"

URL = f"https://www.billboard.com/charts/hot-100/{date_choice}/"

response = requests.get(URL)
response.raise_for_status()
soup = BeautifulSoup(response.text, "html.parser")

titles = [title.find_all('h3', id='title-of-a-story', class_="c-title")[0].getText().lstrip().rstrip() + '\n' for title
          in soup.find_all('div', class_="o-chart-results-list-row-container")]

print(len(titles))
print(titles)

# Replace these variables with your own data
USERNAME = '31jqz3lihjzoegbfihlcizoz7yam'
CLIENT_ID = 'f06a9a258abe4b8cbdb7921185187dc2'
CLIENT_SECRET = '2d363ae240fa4fb18f4c0f0cca5103d3'
REDIRECT_URI = 'https://jamesdr.neocities.org/'  # Must be added to your app settings on the Spotify Developer Dashboard
SCOPE = 'playlist-modify-private'  # Use 'playlist-modify-private' if you want to create a private playlist

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        username=USERNAME,
        scope=SCOPE,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        redirect_uri=REDIRECT_URI,
        open_browser=False,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]
print(user_id)

spotify_uris = []
spotify_uris_array = []


for title in titles:
    # Search for a track by name
    track_query = f"track: {title} year: {date_choice.split('-')[0]}"
    results = sp.search(q=track_query, limit=1, type='track')
    if len(results['tracks']['items']) == 0:
        print(f"{title} not available.")
        continue

    items_uri_ = results['tracks']['items'][0]['uri']
    spotify_uris_array.append(items_uri_)
    uri_ = {
        'title': title,
        'uri': items_uri_
    }
    spotify_uris.append(uri_)
    print(uri_)

playlist_name = f"{date_choice} Billboard 100"
playlist_description = "My new playlist created with the Spotify API and Python"

try:
    new_playlist = sp.user_playlist_create(user=USERNAME, name=playlist_name, public=False,
                                           description=playlist_description)
    print(f"Playlist created successfully! Playlist ID: {new_playlist['id']}")
    sp.playlist_add_items(new_playlist['id'], spotify_uris_array)
except spotipy.SpotifyException as e:
    print(f"An error occurred: {e}")
