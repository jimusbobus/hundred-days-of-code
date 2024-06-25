import os
import requests
import json
from datetime import datetime

try:
    sheety_bearer = os.environ["SHEETY_BEARER"]
except KeyError:
    # If not found, raise an error with a custom message
    raise EnvironmentError(f"Environment variable '{sheety_bearer}' not found.")



NUTRITIONIX_APP_ID = "967cb348"
NUTRITIONIX_API_KEY = "61254280d9d330aaf3ca09f5b3a40d39"

NUTRITIONIX_HEADERS = {
    "Content-Type": "application/json",
    "x-app-id": NUTRITIONIX_APP_ID,
    "x-app-key": NUTRITIONIX_API_KEY
}

NUTRITIONIX_HOST = "https://trackapi.nutritionix.com"
NUTRITIONIX_NLP_URL = f"{NUTRITIONIX_HOST}/v2/natural/exercise"

input_query = input(f"What exercise do you want to log? ")
GENDER = "male"
WEIGHT_KG = 71
HEIGHT_CM = 170
AGE = 47

query = {
    "query": input_query,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(url=NUTRITIONIX_NLP_URL, headers=NUTRITIONIX_HEADERS, json=query)
response.raise_for_status()
data = response.json()
print(f"DEBUG: Data:\n{json.dumps(data, indent=4)}")
print(f"DEBUG: Text:\n{response.text}")

exercise_date = datetime.now().strftime('%d/%m/%Y')
print(f"DEBUG: Date: {exercise_date}")
exercise_time = datetime.now().strftime('%H:%M:%S')
print(f"DEBUG: Time: {exercise_time}")
exercise_name = data['exercises'][0]['name'].title()
print(f"DEBUG: Exercise: {exercise_name}")
exercise_duration = data['exercises'][0]['duration_min']
print(f"DEBUG: Duration: {exercise_duration}")
exercise_calories = data['exercises'][0]['nf_calories']
print(f"DEBUG: Calories: {exercise_calories}")


GOOGLE_DOC = "myWorkouts"
GOOGLE_DOC_SHEET = "tracker"
SHEETY_URL = f"https://api.sheety.co/6fc6d5d26d4e0d7c845360622bc44463/{GOOGLE_DOC}/{GOOGLE_DOC_SHEET}"



SHEETY_AUTH_HEADER = {
    "Content-Type": "application/json",
    "Authorization": sheety_bearer
}
sheety_post_params = {
    GOOGLE_DOC_SHEET: {
       "date": exercise_date,
       "time": exercise_time,
       "exercise": exercise_name,
       "duration": exercise_duration,
       "calories": exercise_calories
    }
}
response = requests.post(url=SHEETY_URL, headers=SHEETY_AUTH_HEADER, json=sheety_post_params)
response.raise_for_status()
data = response.json()
print(f"DEBUG: Data:\n{json.dumps(data, indent=4)}")
print(f"DEBUG: Text:\n{response.text}")