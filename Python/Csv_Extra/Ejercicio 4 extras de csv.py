import csv


#Obtener el iterador
def obtain_document(file_path,user_choice):
    counter = 0
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for number,game in enumerate(reader):
            if game['developer'] == user_choice:
                print(f'{game['name']} (Clasificación: {game['classification']}, Género: {game['genre']})')
                counter += 1 
        if counter == 0:
            print('No hay video juegos para mostrar ')
        new_search(file_path)
    return counter


#Pedir al usuario el nombre del desarrollador
def obtain_user_choice():
    flag = True
    while flag == True:
        user_choice = input("Ingrese el nombre del desarrollador a buscar: ")
        try:
            float(user_choice)
            print("El nombre del desarrollador no puede ser un número. Intente de nuevo  ")
        except ValueError as ex:    
            flag = False
            return user_choice


#preguntar si quiere hacer otra búsqueda
def new_search(file_path):
    user_answer = ''
    while user_answer not in ['SI','NO']:
        user_answer = input("Desea hacer otra búsqueda? (SI/NO): ").upper()
        if user_answer not in ['SI', 'NO']:
            print('Respuesta inválida, intente de nuevo')
        elif user_answer == 'SI':
            user_choice = obtain_user_choice()
            obtain_document(file_path,user_choice)
        else: 
            print('***************programa finalizado******************')
            exit()


#Main
file_path = 'video_games.csv'
user_choice = obtain_user_choice()
obtain_document(file_path,user_choice)