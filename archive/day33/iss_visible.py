import smtplib
from datetime import datetime
from math import radians, cos, sin, asin, sqrt
import requests
import json
from library.What3Words import What3Words


def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great-circle distance between two points
    on the Earth (specified in decimal degrees)
    """
    # Convert decimal degrees to radians
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # Haversine formula
    d_lon = lon2 - lon1
    d_lat = lat2 - lat1
    a = sin(d_lat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(d_lon / 2) ** 2
    c = 2 * asin(sqrt(a))

    # Radius of Earth in kilometers. Use 3956 for miles
    r = 6371

    # Calculate the result
    return c * r


w3w = What3Words()

# Make a GET request to the ISS API
response = requests.get("http://api.open-notify.org/iss-now.json")
response.raise_for_status()
iss_data = response.json()
print(f"DEBUG: ISS Data:\n{json.dumps(iss_data, indent=4)}")
iss_latitude = iss_data['iss_position']['latitude']
iss_longitude = iss_data['iss_position']['longitude']
print(f'DEBUG: ISS: Latitude: {iss_latitude}, Longitude: {iss_longitude}')

parameters = {
    "lat": w3w.latitude,
    "lng": w3w.longitude,
    "formatted": 0
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
sunrise_sunset_data = response.json()
print(f"DEBUG: Sunrise-Sunset Data:\n{json.dumps(sunrise_sunset_data, indent=4)}")
format_string = '%Y-%m-%dT%H:%M:%S%z'
sunrise = datetime.strptime(sunrise_sunset_data['results']['sunrise'], format_string).hour
sunset = datetime.strptime(sunrise_sunset_data['results']['sunset'], format_string).hour
print(f"DEBUG: sunrise={sunrise}, sunset={sunset}")

now_hour = datetime.now().hour
is_dark = False

if (now_hour < sunrise) and (now_hour > sunset):
    print(f"DEBUG: The hour is {now_hour}, and it is dark.")
    is_dark = True
else:
    print(f"DEBUG: The hour is {now_hour}, and it is light.")

threshold = 1665  # 1 timezone width
distance = haversine(lon1=float(w3w.longitude), lat1=float(w3w.latitude),
                     lon2=float(iss_longitude), lat2=float(iss_latitude))

if (distance < threshold) and is_dark:
    msg = "Go Outside - You can see the ISS"
    print(msg)
    # my_email = "jimusbobus@gmail.com"
    # pwd = "fqlt fhjb pqae sjjc"
    #
    # with smtplib.SMTP("smtp.gmail.com") as connection:
    #     connection.starttls()
    #     connection.login(user=my_email, password=pwd)
    #     connection.sendmail(
    #         from_addr=my_email,
    #         to_addrs="jimusbobus@hotmail.com",
    #         msg=f"Subject:ISS Visible!!\n\n{msg}")
else:
    print("No ISS visible")
