import requests
import json

TRIVIA_API_URL = f"https://opentdb.com/api.php"
trivia_params = {
    "amount": 10,
    "difficulty": "easy",
    "type": "boolean"
}

# Make a GET request to the What3words API
response = requests.get(TRIVIA_API_URL, params=trivia_params)
response.raise_for_status()
question_data = response.json()['results']
# print(f"DEBUG: Quiz Data:\n{json.dumps(question_data, indent=4)}")
