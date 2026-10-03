import json

def erase_pokemones():
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = json.load(file) 

        reader.pop(-1)
        return reader

def update_pokemon_json(new_list):
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(new_list, file, indent = 4)


file_path = 'JSON/pokemon.json'
new_list = erase_pokemones()
update_pokemon_json(new_list)