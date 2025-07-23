import requests

def get_json(url, headers=None):
    response = requests.get(url, headers=headers or {})
    response.raise_for_status()
    return response.json()
