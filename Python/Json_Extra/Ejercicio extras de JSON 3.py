import json


#Leer el archivo json
def read_json():
    with open(file_path,'r',encoding='utf-8') as file:
        reader =  json.load(file)

        return reader


#Imprimir los stats de los pokemones
def show_pokemon_stats(reader):
    for pokemon in reader:
        print(f'\nNombre: {pokemon['name']}')
        for stat, value in pokemon['stats'].items():  
            if stat in ['attack','defense', 'speed']:
                print(f'{stat}: {value}')  


file_path = 'JSON/pokemon.json'
reader = read_json()
show_pokemon_stats(reader)