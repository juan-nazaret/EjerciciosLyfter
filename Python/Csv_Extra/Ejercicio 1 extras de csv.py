import csv

def obtain_csv_text(file_path):
    with open(file_path, 'r', encoding='utf-8', newline='') as file:
        reader = csv.DictReader(file)

        for number, series in enumerate(reader, start=1):
            print(f'{number}:\n Nombre: {series['name']}\nGénero: {series['genre']}\nDesarrollador: {series['developer']}\nClasificación: {series['classification']}')
    return 


obtain_csv_text('video_games.csv')



