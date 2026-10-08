import csv
import os
import sys




file_path = os.path.join(os.path.dirname(__file__), "students.csv")

#reads the csv archive and returns a python list
def obtain_list_from_csv():
    try:
        with open(file_path,'r', encoding= 'utf-8') as file:
            reader = csv.DictReader(file)
            students_list_from_csv = list(reader)
        return students_list_from_csv
    except FileNotFoundError as ex:
        print(ex)
        return False


#over writes the data OPTION 7 'EXPORTAR'
def save_students_dictionary_list(new_students_list):
    if len(new_students_list) == 0:
        print("\nLa lista de nuevos estudiantes esta vacía")
        return False
    else: 
        with open(file_path,'a',encoding='utf-8', newline='') as file:
            headers = new_students_list[0].keys()
            writer = csv.DictWriter(file, fieldnames= headers)
            if os.path.getsize(file_path) == 0:
                writer.writeheader()
            writer.writerows(new_students_list)
            print(f'\n ***LISTA EXPORTADA*** ')
            return True


#WRITES COLUMNS ONLY
def save_students_dictionary_empty_list(data):
    with open(file_path, 'w',encoding='utf-8') as file:
        writer = csv.DictWriter(file,data)
        writer.writeheader()

#Replaces all the document content, intended to be used after an student is deleted
def save_students_dictionary_list_after_delete(new_students_list,message): 
    with open(file_path,'w',encoding='utf-8', newline='') as file:
        headers = new_students_list[0].keys()
        writer = csv.DictWriter(file, fieldnames= headers)
        writer.writeheader()
        writer.writerows(new_students_list)
        print(f'\n   ***{message}*** ')
        return True
