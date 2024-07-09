import requests
import urllib.parse
import json


movie_title = 'Inception'

request_params = {
    "api_key": "29b8108eb5cf6debcca1b3cca380b961"
}

# Search for the movie by title
search_url = f'https://api.themoviedb.org/3/search/movie?query={encoded_movie_title}'
search_response = requests.get(search_url, params=request_params)
search_results = search_response.json()


# # Get the movie details
# details_url = f'https://api.themoviedb.org/3/movie/Avatar'
# details_response = requests.get(details_url, params=request_params)
# movie_details = details_response.json()

# Print or process the movie details
print(f"DEBUG: W3W Data:\n{json.dumps(search_results['results'][0], indent=4)}")
