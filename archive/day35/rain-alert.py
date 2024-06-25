import requests
# import json
# from twilio.rest import Client

from library.What3Words import What3Words

w3w = What3Words()

OWM_API_KEY = "77d096f76d97a0f547448930f0c1d23b"

OWM_API_URL = "https://api.openweathermap.org/data/2.5/forecast"

owm_api_params = {
    "lat": w3w.latitude,
    "lon": w3w.longitude,
    "appid": OWM_API_KEY,
    "cnt": 4
}

response = requests.get(OWM_API_URL, params=owm_api_params)
response.raise_for_status()
owm_data = response.json()
# print(f"DEBUG: Open Weather Data:\n{json.dumps(owm_data, indent=4)}")
will_cloud = False
will_rain = False
for hour_data in owm_data['list']:
    print(hour_data['weather'])
    condition_code = hour_data['weather'][0]['id']
    print(condition_code)
    if condition_code in [800, 802, 802, 803, 804]:
        will_cloud = True
    if 500 <= condition_code <= 531:
        will_rain = True

SMS_NUMBER = "+447441368107"
SMS_SID = "AC958b6ac8e38724bbe258b079122cc63a"
SMS_AUTH_ID = "725fbbd9420a93e6b6cf2906081dbcfc"
if will_rain:
    print("bring a brolly")
    # client = Client(SMS_SID, SMS_AUTH_ID)
    # message = client.messages.create(body="It's going to rain, bring a brolly.",
    #                                  from_=SMS_NUMBER,
    #                                  to='07803605128'
    #                                  )
    # print(message.sid)
