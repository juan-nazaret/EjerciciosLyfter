import json
import csv

#Convertir el objeto json a un diccionario python 
def obtain_py_dict(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        pokemon_dict_from_json = json.load(file)
    return pokemon_dict_from_json


#Leer el archivo CSV y obtener la lista de pokemones
def obtain_pokemon_csv(file_path_csv):
    pokemon_names_list_from_csv = []
    with open(file_path_csv,'r',encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            pokemon_names_list_from_csv.append(row['pokemon'])
    return pokemon_names_list_from_csv


#Obtener y validar una cadena
def obtain_string(pokemon_info):
    flag = False
    while flag ==  False:
        pokemon_data = input(f'Ingrese el {pokemon_info} del pokemon: ')
        try:
            float(pokemon_data)
            print(f'El {pokemon_info} no puede ser un numero. Intenta de nuevo.')
        except ValueError as ex:
            flag =  True
            return pokemon_data


#Obtener y validar un numero entero
def obtain_an_int(pokemon_info):
    flag = False
    while flag == False:
        try: 
            pokemon_level = int(input(f'Ingrese el {pokemon_info} del pokemon: '))
            flag = True
            return pokemon_level
        except ValueError as ex: 
            print(f'El {pokemon_info} debe ser un numero entero, intenta de nuevo. ')


#quiere agregar otro elemento?
def wish_to_add_another_item(item):
    flag = False
    while flag == False:
        wish_to_add_another_item = input(f'Te gustaria agregar otro {item}? (SI/NO)').upper()
        if wish_to_add_another_item not in ['SI','NO']:
            print('respuesta invalida, intente d nuevo')
        else: 
            flag = True
            return wish_to_add_another_item


#Obtener el nuevo nombre del pokemon
def new_name(pokemon_names_list_from_csv,pokemon_dict_from_json):
    flag = False
    while flag == False:
        name = input('Ingrese el nombre de un pokemon unicamente de la primera generación: ')
        try:
            float(name)
            print('El nombre no puede ser un numero. Intente de nuevo')
        except ValueError as ex:
            if name in pokemon_names_list_from_csv:
                    if any(pokemon_name['name'] == name for pokemon_name in pokemon_dict_from_json):
                        print('el nombre ya existe, intente con otro nombre')
                    else:
                        flag = True
            else:
                print('el nombre del pokemon no es de la primera generación, intente de nuevo ')
    return name

#Obtener el type
def obtain_type():
    pokemon_type = obtain_string('tipo')
    return pokemon_type

#Obtener el nivel del pokemon
def obtain_pokemon_level():
    pokemon_level = obtain_an_int('level')
    return pokemon_level

#Obtener que objeto lleva el pokemon
def obtain_pokemon_held_item():
    pokemon_item = obtain_string('objeto que lleva')
    return pokemon_item
        

#Obtener el peso del pokemon
def obtain_pokemon_weight():
    flag = False
    while flag == False:
        try: 
            pokemon_level = float(input('Ingrese el peso del pokemon: '))
            flag = True
            return pokemon_level
        except ValueError as ex: 
            print('El peso debe ser un numero, intenta de nuevo. ')


#Obtener si el pokemon brilla (BOOLEAN)
def obtain_pokemon_shine():
    flag = False
    while flag == False:
        is_shiny = input('El pokemon brilla? (True/False): ').lower()
        if is_shiny in ['true', 'false']:
            flag = True
            return is_shiny == 'true'
        else: 
            print('La respuesta solo puede ser "True" o "False". Intenta de nuevo. ')


#Obtener la lista de skills 
def obtain_skills():
    pokemon_skills_list = []
    flag = True
    while flag == True:
        new_skill = obtain_string('skill')
        pokemon_skills_list.append(new_skill)
        wish_to_add_another_skill = wish_to_add_another_item('skill')
        if wish_to_add_another_skill == 'NO':
            flag = False
            return pokemon_skills_list


#Crear el nuevo diccionario de stats
def obtaining_pokemon_stats():
    lits_of_stats = ['hp','attack','defense','sp_attack','sp_defense','speed']
    stats = dict.fromkeys(lits_of_stats, "")
    for stat in lits_of_stats:
        stat_value = obtain_an_int(stat)
        stats[stat] = stat_value
    return stats


#Llenar el nuevo pokemon
#Retorna también el diccionario con el nuevo pokemon listo para ser convertido al json
def create_new_pokemon(pokemon_dict_from_json,file_path,pokemon_names_list_from_csv):
    new_pokemon = {}
    new_pokemon['name'] = new_name(pokemon_names_list_from_csv, pokemon_dict_from_json)
    new_pokemon['type'] = obtain_type()
    new_pokemon['level'] = obtain_pokemon_level()
    new_pokemon['weight_kg'] = obtain_pokemon_weight()
    new_pokemon['is_shiny'] = obtain_pokemon_shine()
    new_pokemon['held_item'] = obtain_pokemon_held_item()
    new_pokemon['skills'] = obtain_skills()
    new_pokemon['stats'] = obtaining_pokemon_stats()
    
    #Agregamos el nuevo diccionario a la lista de diccionarios python
    pokemon_dict_from_json.append(new_pokemon)

    #Aquí llamamos la función para sobre escribir el documento json 
    overwrite_json(file_path, pokemon_dict_from_json)
    print(f'Nuevo pokemon agregado exitosamente ')

    return new_pokemon


#Escribir el nuevo pokemon (ya convertido a JSON) sobre pokemon.json
def overwrite_json(file_path,new_pokemon):
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(new_pokemon, file, indent=4)


def main():
    flag = True
    while flag == True:
        print(f'******Vamos a agregar un nuevo pokemon *******')
        file_path = 'JSON/pokemon.json'
        pokemon_dict_from_json =  obtain_py_dict(file_path)
        pokemon_names_list_from_csv = obtain_pokemon_csv('JSON/pokemon_generacion_1.csv')
        create_new_pokemon(pokemon_dict_from_json,file_path,pokemon_names_list_from_csv)
        answer = wish_to_add_another_item('pokemon')
        if answer == 'NO':
            flag = False
    print(f'El archivo de pokemones actualizado es {pokemon_dict_from_json}')

main()
print('CLOSE')
3