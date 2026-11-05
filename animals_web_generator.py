import json
import os

import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("NINJAS_API_KEY")

API_URL = "https://api.api-ninjas.com/v1/animals"

headers = {"X-Api-Key": API_KEY}
params = {"name": "Fox"}


def load_data(file_path):
    """Loads a JSON file"""
    with open(file_path, "r", encoding="utf-8") as handle:
        return json.load(handle)


def serialize_animal(animal_obj):
    output = ""

    output += '<li class="cards__item">'
    name = animal_obj.get("name")
    diet = animal_obj.get("characteristics", {}).get("diet")
    locations = animal_obj.get("locations", [])
    animal_type = animal_obj.get("characteristics", {}).get("type")

    if name:
        output += f'<div class="card__title">{name}</div>\n'
        output += '<p class="card__text">\n'

    if diet:
        output += f'<strong>Diet:</strong> {diet}<br/>\n'

    if locations:
        output += f'<strong>Location:</strong> {locations[0]}<br/>\n'

    if animal_type:
        output += f'<strong>Type:</strong> {animal_type}<br/>\n'

    output += "</p>\n"
    output += "</li>\n"

    return output


response = requests.get(API_URL, headers=headers, params=params)
response.raise_for_status()
animals_data = response.json()

output = ""

for animal in animals_data:
    output += serialize_animal(animal)


with open("animals_template.html", "r", encoding="utf-8") as file:
    template = file.read()

html = template.replace("__REPLACE_ANIMALS_INFO__", output)

with open("animals.html", "w", encoding="utf-8") as file:
    file.write(html)
