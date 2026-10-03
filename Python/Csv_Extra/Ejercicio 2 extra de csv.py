import csv

def select_user():
    user_selection = ""
    while user_selection not in ['EC','E','E 10+','T','M','AO','RP']:
        user_selection = input('ingrese el género que esta buscando: ').upper()
        if user_selection not in ['EC','E','E 10+','T','M','AO','RP']:
            print(f"Los datos ingresados no son validos. Ingrese un género válido ('EC','E','E 10+','T','M','AO','RP') ")
        else:
            return user_selection


def obtain_video_game(file_path, user_selection):
    counter = 0
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file,delimiter=',')
        for row in reader:
            if row['classification'] ==  user_selection:
                print(f'Titulo: {row['name']} by {row['developer']}')


user_selection = select_user()
file_path = 'video_games.csv'
counter = obtain_video_game(file_path,user_selection)
