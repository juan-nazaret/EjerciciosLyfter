import csv
import os

file_path = os.path.join(os.path.dirname(__file__), "students.csv")

#reads the csv archive and returns a python list
def obtain_list_from_csv(new_students_list):
    try:
        with open(file_path,'r', encoding= 'utf-8') as file:
            students_list_from_csv = []
            reader = csv.DictReader(file)
            students_list_from_csv.extend(list(reader))
            if len(new_students_list) == 0:
                new_students_list.extend(students_list_from_csv)
            else:
                avoid_duplicate_data(new_students_list, students_list_from_csv)
            print('\n*** LISTA IMPORTADA ***')
            return
    except FileNotFoundError as ex:
        print('el archivo no existe')
        return new_students_list


#over writes the data OPTION 7 'EXPORTAR'
def save_students_dictionary_list(new_students_list):
    if len(new_students_list) == 0:
        print('\n*** no hay datos para exportar ***')
        return False
    else: 
        with open(file_path,'w',encoding='utf-8', newline='') as file:
            headers = new_students_list[0].keys()
            writer = csv.DictWriter(file, fieldnames= headers)
            writer.writeheader()
            writer.writerows(new_students_list)
            print(f'\n *** LISTA EXPORTADA *** ')
            return True


#Avoids function from duplicating data 
def avoid_duplicate_data(new_students_list, list_from_csv):
    for csv_student in list_from_csv:
        flag = False
        for list_student in new_students_list:
            if csv_student['name'].lower() == list_student['name'].lower():
                if csv_student['section'] == list_student['section']:
                    flag = True
        if flag == False:
            new_students_list.append(csv_student)
    return 