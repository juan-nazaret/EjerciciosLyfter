import json

def obtain_pokemon_info():
    with open(file_path,'r', encoding='utf-8') as file:
        reader = json.load(file)
        
        for pokemon in reader:
            print(f'nombre: {pokemon['name']}, tipo: {pokemon['type']}, nivel: {pokemon['level']}')



file_path = 'JSON/pokemon.json'
obtain_pokemon_info()