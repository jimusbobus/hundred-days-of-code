import requests
import json
from datetime import datetime, timedelta

PIXELA_URL = "https://pixe.la/v1/users"
USERNAME = "jimusbobus"
PASSWORD = "=r8o|;gDN6Ok$INS"
AUTH_HEADER = {
    "X-USER-TOKEN": PASSWORD
}
RUNNING_GRAPH_ID = "jb-running-graph"


def create_user():
    pixela_create_user_params = {
        "token": PASSWORD,
        "username": USERNAME,
        "agreeTermsOfService": "yes",
        "notMinor": "yes"
    }

    response = requests.post(PIXELA_URL, json=pixela_create_user_params)
    response.raise_for_status()
    data = response.json()
    print(f"DEBUG: Data:\n{json.dumps(data, indent=4)}")
    print(f"DEBUG: Text:\n{response.text}")


def create_graph():
    pixela_create_graph_params = {
        "id": RUNNING_GRAPH_ID,
        "name": "Running Graph",
        "unit": "km",
        "type": "float",
        "color": "sora"
    }

    response = requests.post(f"{PIXELA_URL}/{USERNAME}/graphs", json=pixela_create_graph_params, headers=AUTH_HEADER)
    response.raise_for_status()
    data = response.json()
    print(f"DEBUG: Data:\n{json.dumps(data, indent=4)}")
    print(f"DEBUG: Text:\n{response.text}")


def post_to_graph():
    today = datetime.now()
    yesterday = datetime.now() - timedelta(days=1)
    # Format the date in 'yyyyMMdd' format
    post_graph_params = {
        "date": yesterday.strftime('%Y%m%d'),
        "quantity": "2.4"
    }

    response = requests.post(f"{PIXELA_URL}/{USERNAME}/graphs/{RUNNING_GRAPH_ID}", json=post_graph_params,
                             headers=AUTH_HEADER)
    response.raise_for_status()
    data = response.json()
    print(f"DEBUG: Data:\n{json.dumps(data, indent=4)}")
    print(f"DEBUG: Text:\n{response.text}")


def update_pixel():
    update_pixel_params = {
        "quantity": "5.25"
    }
    today = datetime.now()
    response = requests.put(f"{PIXELA_URL}/{USERNAME}/graphs/{RUNNING_GRAPH_ID}/{today.strftime('%Y%m%d')}",
                            json=update_pixel_params,
                            headers=AUTH_HEADER)
    response.raise_for_status()
    data = response.json()
    print(f"DEBUG: Data:\n{json.dumps(data, indent=4)}")
    print(f"DEBUG: Text:\n{response.text}")


def delete_pixel():
    yesterday = datetime.now() - timedelta(days=1)
    response = requests.delete(f"{PIXELA_URL}/{USERNAME}/graphs/{RUNNING_GRAPH_ID}/{yesterday.strftime('%Y%m%d')}",
                               headers=AUTH_HEADER)
    response.raise_for_status()
    data = response.json()
    print(f"DEBUG: Data:\n{json.dumps(data, indent=4)}")
    print(f"DEBUG: Text:\n{response.text}")


# create_user()
# create_graph()
# post_to_graph()
# update_pixel()
delete_pixel()