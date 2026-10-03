import csv

def save_video_games_ranking(file_path, data):
    with open(file_path, 'w', encoding='utf-8', newline='') as file:

        #Obtenemos los nombres de las columnas con las lla]es del primer registro
        headers = ['name','genre','developer','classification']

        #Inicializamos el escritor indicando el archivo destino  y los encabezados
        writer = csv.DictWriter(file, fieldnames=headers,delimiter='\t')

        #escribimos la primera fila en el documento con los títulos
        writer.writeheader()

        #Insertamos la lista completa 
        writer.writerows(data)


def obtain_data():
    flag = False
    flag_2= False    
    video_games = []
    list_of_keys = ['name','genre','developer','classification']
    while flag == False:
            info={}
            flag_2 = False
            while flag_2 == False:
                    info[list_of_keys[0]] = input('Ingrese el nombre del video juego: ')
                    flag_2 = is_not_a_number(info[list_of_keys[0]])
            flag_2 = False
            while flag_2 == False:
                    info[list_of_keys[1]] = input('Ingrese el género del video juego: ')
                    flag_2 = is_not_a_number(info[list_of_keys[1]])
            flag_2 = False
            while flag_2 == False:
                    info[list_of_keys[2]] = input('Ingrese el desarrollador del video juego: ')
                    flag_2 = is_not_a_number(info[list_of_keys[2]])
            flag_2 = False
            while flag_2 == False:
                    info[list_of_keys[3]] = input('Ingrese la clasificación ESRB: ').upper()
                    classification = info[list_of_keys[3]]
                    if classification in ['EC','E','E 10+','T','M','AO','RP']:
                        video_games.append(info)
                        flag_2 = True
                        flag = insert_another_video_game()
                        
                    else:
                        print("Los datos ingresados no están entre 'EC','E','E 10+','T','M','AO' o 'RP'. Ingresa una clasificación correcta ")
    return video_games


def is_not_a_number(text):
    flag = False
    try:
        float(text)
        print("El dato ingresado es u numero, intente de nuevo con una cadena: ")
    except ValueError as ex:
        flag = True
    return flag


def insert_another_video_game():
    flag = False
    user_selection = ''
    while user_selection not in ['SI','NO']:
        user_selection = input('Quieres ingresar otro video juego? SI/NO').upper()
        if user_selection == 'NO':
            flag = True
        elif user_selection not in ['SI','NO']:
            print('La respuesta recibida no es valida, intente de nuevo.')
    return flag


file_path = 'video_games.csv'
data = obtain_data()
save_video_games_ranking(file_path, data)