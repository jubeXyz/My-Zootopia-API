import os

import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("NINJAS_API_KEY")
API_URL = "https://api.api-ninjas.com/v1/animals"

HEADERS = {"X-Api-Key": API_KEY}


def fetch_data(animal_name):
    """
    Fetches animal data for the given animal name.
    Returns a list of animal dictionaries.
    """
    params = {"name": animal_name}
    response = requests.get(API_URL, headers=HEADERS, params=params)
    response.raise_for_status()
    return response.json()

