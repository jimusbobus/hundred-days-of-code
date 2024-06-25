import requests
import json


class What3Words:
    W3W_API_KEY = "RUC3QKHS"

    def __init__(self, w3w="mocked.frame.blunders"):
        # Home W3W
        w3w_params = {
            "words": w3w,
            "key": What3Words.W3W_API_KEY
        }
        # Make a GET request to the What3words API
        response = requests.get('https://api.what3words.com/v3/convert-to-coordinates', params=w3w_params)
        response.raise_for_status()
        w3w_data = response.json()
        print(f"DEBUG: W3W Data:\n{json.dumps(w3w_data, indent=4)}")
        # Extract latitude and longitude from the response
        self.latitude = w3w_data['coordinates']['lat']
        self.longitude = w3w_data['coordinates']['lng']
        print(f'DEBUG: W3W: Latitude: {self.latitude}, Longitude: {self.longitude}')
