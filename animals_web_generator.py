import data_fetcher

animal_name = input("Enter an animal name: ")


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


animals_data = data_fetcher.fetch_data(animal_name)

output = ""

if not animals_data:
    output = f'<h2 style="text-align: center;">The animal "{animal_name}" doesn\'t exist.</h2>'
else:
    for animal in animals_data:
        output += serialize_animal(animal)


with open("animals_template.html", "r", encoding="utf-8") as file:
    template = file.read()

html = template.replace("__REPLACE_ANIMALS_INFO__", output)

with open("animals.html", "w", encoding="utf-8") as file:
    file.write(html)
