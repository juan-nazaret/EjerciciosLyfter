import csv
import os

def save_students_dictionary(data):
    with open(file_path,'a',encoding='utf-8') as file:

        #obtenemos los nombres de las columnas con las llaves del primer registro
        headers = data.keys()

        #iniciamos el escritor indicando el archivo destino y los encabezados 
        writer = csv.DictWriter(file, fieldnames= headers)

        #escribimos la primera fila en el documento con los títulos
        if os.path.getsize(file_path) == 0:
            writer.writeheader()

        #insertamos la lista completa de nuestras series
        writer.writerow(data)


file_path = os.path.join(os.path.dirname(__file__), "students.csv")


#lee el archivo csv y lo regresa en una lista python 
def obtain_list_from_csv():
    try:
        with open(file_path,'r', encoding= 'utf-8') as file:
            reader = csv.DictReader(file)
            students_list_from_csv = list(reader)
        return students_list_from_csv
    except FileNotFoundError as ex:
        return False


#sobre escribir el código
def save_students_dictionary_list(data):
    with open(file_path,'w',encoding='utf-8') as file:

        #obtenemos los nombres de las columnas con las llaves del primer registro
        headers = data[0].keys()

        #iniciamos el escritor indicando el archivo destino y los encabezados 
        writer = csv.DictWriter(file, fieldnames= headers)

        writer.writeheader()

        #insertamos la lista completa de nuestras series
        writer.writerows(data)


#escribir solo columnas
def save_students_dictionary_empty_list(data):
    with open(file_path, 'w',encoding='utf-8') as file:
        writer = csv.DictWriter(file,data)
        writer.writeheader()