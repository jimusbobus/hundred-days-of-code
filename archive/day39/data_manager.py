import requests
import json


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    HEADER = {
        "Content-Type": "application/json",
        "Authorization": "Bearer 3Vt)9y[TN^#cU=@&{~LA[,L(o37NVp-j"
    }
    URL = "https://api.sheety.co/6fc6d5d26d4e0d7c845360622bc44463/flightDeals/prices"

    def __init__(self):
        response = requests.get(url=DataManager.URL, headers=DataManager.HEADER)
        response.raise_for_status()
        self.prices = response.json()['prices']
        print(self.prices)
