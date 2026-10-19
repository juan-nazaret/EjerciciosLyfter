import csv
import os
from actions import Student

file_path = os.path.join(os.path.dirname(__file__), "students.csv")

#reads the csv archive and returns a python list
def obtain_list_from_csv(new_students_list):
    try:
        with open(file_path,'r', encoding= 'utf-8') as file:
            students_list_from_csv = []
            reader = csv.DictReader(file)
            students_list_from_csv.extend(list(reader))
            objects_list_from_csv = from_dictionaries_to_objects(students_list_from_csv)
            if len(new_students_list) == 0:
                new_students_list.extend(objects_list_from_csv)
            else:
                avoid_duplicate_data(new_students_list, objects_list_from_csv)
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
        new_students_dictionary_list = object_to_dictionary(new_students_list)
        with open(file_path,'w',encoding='utf-8', newline='') as file:
            headers = new_students_dictionary_list[0].keys()
            writer = csv.DictWriter(file, fieldnames= headers)
            writer.writeheader()
            writer.writerows(new_students_dictionary_list)
            print(f'\n *** LISTA EXPORTADA *** ')
            return True


#Avoids function from duplicating data 
def avoid_duplicate_data(new_students_list, list_from_csv):
    for csv_student in list_from_csv:
        flag = False
        for list_student in new_students_list:
            if csv_student.name.lower() == list_student.name.lower():
                if csv_student.section == list_student.section:
                    flag = True
        if flag == False:
            new_students_list.append(csv_student)
    return 


#convert objects to dictionaries 
def object_to_dictionary(new_students_list):
    new_students_dictionary_list = []
    for student in new_students_list:
        student_dict = {}
        student_dict['name'] = student.name
        student_dict['section'] = student.section
        student_dict['spanish_note'] = student.spanish_note
        student_dict['english_note'] =  student.english_note
        student_dict['socials_note'] = student.socials_note
        student_dict['sciences_note'] = student.sciences_note
        new_students_dictionary_list.append(student_dict)
    return new_students_dictionary_list


#from dictionaries to objects list
def from_dictionaries_to_objects(students_list_from_csv):
    students_objects_list = []
    for student in students_list_from_csv:
        person1 = Student(student['name'],student['section'],student['spanish_note'],student['english_note'],student['socials_note'],student['sciences_note'])
        students_objects_list.append(person1)
    return students_objects_list