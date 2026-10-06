import csv

#Obtiene una lista con los géneros encontrados
def obtain_genres_list(file_path):
    genres_list = []
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            genres_list.append(row['genre'])
    return genres_list


#Conteo de géneros
def genres_count(genres_list):
    d = dict.fromkeys(genres_list,0)
    for genre in genres_list:
        d[genre] = d[genre] +  1
    return d


#imprimir el diccionario de conteo
def show_counter(genres_list_count):
    print('Géneros encontrados: ')
    for genre, total in genres_list_count.items():
        print(f'{genre}: {total}')


file_path = 'video_games.csv'
genres_list = (obtain_genres_list(file_path))
genres_list_count = genres_count(genres_list)
show_counter(genres_list_count)
