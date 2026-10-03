import json


#Leer el archivo JSON
def read_json():
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = json.load(file)

    return reader


#Crear diccionario de tipos
def sort_pokemon_by_group(reader):
    list_of_types = []
    for pokemon in reader:
        type1 = pokemon['type'].lower()
        list_of_types.append(type1)
    dictionary_type = dict.fromkeys(list_of_types, [0,0])
    return dictionary_type


#Llenar el diccionario con la suma de los tipos de pokemon y con el conteo para calcular el promedio 
def count_types(dictionary_type, reader):
    for pokemon in reader:
        type1 = pokemon['type'].lower()
        for type2 in dictionary_type.keys():
            if type2 == type1:
                dictionary_type[type2] = [(dictionary_type[type2][0] + pokemon['level']),(dictionary_type[type2][1]+1)]
    calculate_average(dictionary_type)
    return dictionary_type


#Calcular el promedio del cada tipo
def calculate_average(dictionary_type):
    for type1 in dictionary_type.keys():
        dictionary_type[type1][0] = dictionary_type[type1][0] / dictionary_type[type1][1]
    return dictionary_type


#Mostrar 
def show_type_average(dictionary_type):
    for type1, average in dictionary_type.items():
        print(f'Tipo: {type1} -> Promedio de nivel: {average[0]}')
        #print(f'{type1}: {average}')


file_path = 'JSON/pokemon.json'
reader = read_json()
dictionary_type = (sort_pokemon_by_group(reader))
count_types(dictionary_type, reader)
show_type_average(dictionary_type)
