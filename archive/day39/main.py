# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

# fd = DataManager()


import requests

url = "https://booking-com15.p.rapidapi.com/api/v1/flights/getMinPrice"

querystring = {
    "fromId": "BOM.AIRPORT",
    "toId": "DEL.AIRPORT",
    "departDate": "2024-05-07",
    "currency_code": "GBP"
}

headers = {
    "X-RapidAPI-Key": "092ab25253msh6d2e601911ff1bap10973fjsn5ea5452f55b0",
    "X-RapidAPI-Host": "booking-com15.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())
