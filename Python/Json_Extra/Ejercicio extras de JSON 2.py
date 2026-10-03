import json


#Leer el archivo json
def read_json():
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = json.load(file)
    return reader


#Pedir al usuario un tipo de pokemon. Retorna el tipo de pokemon que el usuario quiere buscar
def ask_type():
    flag = False
    while flag == False:
        pokemon_type = input(f'Ingrese el tipo de pokemon que busca: ').lower()
        try: 
            float(pokemon_type)
            print('El tipo no puede ser un numero. Intente de nuevo')
        except ValueError as ex:
            flag = True
            return pokemon_type


#Comparar la entrada del usuario con los elementos de la lista
def compare_elements_to_type(reader,pokemon_type):
    pokemon_type_list = []
    print(f'\nLos pokemones que existen del tipo {pokemon_type} son:')
    for pokemon in reader:
        if pokemon['type'].lower() == pokemon_type:
            print(pokemon['name'])
            pokemon_type_list.append(pokemon['name'])
            
    if len(pokemon_type_list) == 0:
        print(f'No hay pokemones del tipo {pokemon_type}')


file_path = 'JSON/pokemon.json'
reader = read_json()
pokemon_type = ask_type()


compare_elements_to_type(reader,pokemon_type)