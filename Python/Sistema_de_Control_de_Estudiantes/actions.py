import re
import data

#**************** 1 ADD NEW STUDENT ******************************

#NEW STUDENT*****
#fill in new student logic
def create_new_student_main(existing_student_list,new_student_list, new_student_list_not_imported_yet):
    
    if existing_student_list == False:
        print('\nNo existe un archivo importado de estudiantes por lo que no se puede validar una nueva entrada. Importe un archivo primero')
        return None
    else:
        new_student_dictionary = {}

        print('\nAGREGAR NUEVO ESTUDIANTE ***')
        name = add_new_name()
        new_student_dictionary['name'] = name

        section = add_new_section()
        new_student_dictionary['section'] = section

        student_exists_in_existing_students_list =  student_exists_def(name,section,existing_student_list)
        if student_exists_in_existing_students_list == True:
            print('El estudiante ya existe en esta sección.')
            new_student_dictionary = False
            return new_student_dictionary

        student_exists_in_new_student_list = student_exists_in_new_student_list_def(name,section,new_student_list)
        if student_exists_in_new_student_list == True:
            print('El estudiante ya existe en esta nueva lista de nuevos alumnos aun no exportada')
            new_student_dictionary = False
            return new_student_dictionary

        student_exists_in_new_list_not_imported_yet = student_exists_in_new_student_list_not_imported_yet_def(name,section,new_student_list_not_imported_yet)
        if student_exists_in_new_list_not_imported_yet == True:
            print('El alumno ya existe en la lista en espera de ser exportada')
            new_student_dictionary = False
            return new_student_dictionary

        spanish_note = obtain_note('spanish')
        new_student_dictionary['spanish_note'] = spanish_note

        english_note = obtain_note('english')
        new_student_dictionary['english_note'] = english_note

        socials_note = obtain_note('socials')
        new_student_dictionary['socials_note'] = socials_note

        sciences_note = obtain_note('sciences')
        new_student_dictionary['sciences_note'] = sciences_note

        new_student_list
        return new_student_dictionary


#It creates a list of dictionaries of new students and returns it 
def create_new_student(existing_student_list,new_student_list_not_imported_yet):
    new_students_list = []
    if len(new_student_list_not_imported_yet) > 0:
        print(f'\nRecuerda que tienes una lista en espera de ser exportada, los alumnos de esa fila son:\n') 
        for number, student in enumerate(new_student_list_not_imported_yet, start=1):
                    print(f'Alumno {number}\n------------------\nnombre: {student['name']}\nsección: {student['section']}\nnota de español:{student['spanish_note']}\nnota de inglés:{student['english_note']}\nnota de sociales:{student['socials_note']}\nnota de ciencias:{student['sciences_note']}\n')
    
    while True:
        new_student_dictionary = create_new_student_main(existing_student_list, new_students_list, new_student_list_not_imported_yet)
        if new_student_dictionary == False:
            create_another_student = user_response()
            if create_another_student == 'no':
                new_student_list_not_imported_yet.extend(new_students_list)
                return new_student_list_not_imported_yet
        elif new_student_dictionary == None:
            return existing_student_list
        else: 
            new_students_list.append(new_student_dictionary)
            create_another_student = user_response()
            if create_another_student == 'no':
                new_student_list_not_imported_yet.extend(new_students_list)
                return new_student_list_not_imported_yet
        

#Do the user want to create a new student?
def user_response():
    while True:
        create_another_student = input('Quiere crear otro estudiante? SI/NO').lower()
        if create_another_student in ['si','no']:
            return create_another_student
        else:
            print('Respuesta invalida. Intenta de nuevo.')


#**************** 2 SHOW ALL STUDENTS ******************************


#obtains and prints all the students list
def obtain_all_students(existing_student_list):
    if existing_student_list == False:
        print('\nNo existe un archivo importado de estudiantes')
    elif len(existing_student_list) == 0:
        print(f'\nNo hay estudiantes para mostrar')
    else:
        print('\nMostrar todos los estudiantes*** \n')
        for number, student in enumerate(existing_student_list, start=1):
            print(f'Alumno {number}\n------------------\nnombre: {student['name']}\nsección: {student['section']}\nnota de español:{student['spanish_note']}\nnota de inglés:{student['english_note']}\nnota de sociales:{student['socials_note']}\nnota de ciencias:{student['sciences_note']}\n')


#**************** 3 TOP 3 STUDENTS ******************************


def obtain_highest_average(existing_student_list):
    students_list_from_csv = existing_student_list
    if students_list_from_csv == False:
        print('No existe un archivo importado')
    else: 
        averages_list = create_all_students_average_dictionary(students_list_from_csv)
        averages_list.sort(reverse= True, key=sort_list)
        top_3_list = obtain_top_3(averages_list)
        print('\nTOP 3 ********\n_________________________\n')
        for number, index in enumerate (range(len(top_3_list)),start=1):
            try:
                print(f'{number}: nombre: {top_3_list[index]['name']}, sección: {top_3_list[index]['section']}, promedio: {top_3_list[index]['average_note']}')
            except KeyError as ex:
                print(f'{number}:')

def sort_list(data):
    return data['average_note']


def obtain_top_3(averages_list):
    top_3_list = []
    for index in range(0,3):
        try:
            top_3_list.append(averages_list[index])
        except IndexError as ex:
            top_3_list.append({})
    return top_3_list

    
#**************** 4 SHOW ALL STUDENTS AVERAGES ******************************


def see_all_students_average(existing_student_list):
    students_list_from_csv = existing_student_list
    if students_list_from_csv == False:
        print(f'\nNO hay un archivo importado de alumnos')
    elif len(students_list_from_csv) == 0:
        print('NO hay registros de estudiantes para mostrar')
    else:
        all_students_average_list = create_all_students_average_dictionary(students_list_from_csv)
        print(f'\n***Mostrar todos los promedios****\n-------------------------------------------')
        for number, index in enumerate(range(len(all_students_average_list)),start=1): 
            print(f'{number}.- name:{all_students_average_list[index]['name']} sección: {all_students_average_list[index]['section']} promedio: {all_students_average_list[index]['average_note']}')


#**************** 5 DELETE A STUDENT ******************************

def obtain_student_data():
    name = add_new_name()
    section = add_new_section()
    return name,section


def delete_student(existing_student_list):
    list_of_students_from_csv = existing_student_list
    if list_of_students_from_csv == False:
        print('\nNo existe un archivo importado, no hay alumnos para mostrar o eliminar\n')
        return
    elif len(list_of_students_from_csv) == 0:
        print(f'No hay registros para mostrar o eliminar\n')
        return
    else:
        name,section = obtain_student_data()
        for index in range(len(list_of_students_from_csv)):
            if list_of_students_from_csv[index]['name'].lower() == name.lower():
                if list_of_students_from_csv[index]['section'] == section:
                    print(f'El estudiante a eliminar nombre: {name} sección: {section}')
                    user_response = yes_or_no('Desea continuar? si/no: ')
                    if user_response == True:
                        list_of_students_from_csv.pop(index)
                        if len(list_of_students_from_csv) > 0:
                            data.save_students_dictionary_list_after_delete(list_of_students_from_csv,"LISTA ACTUALIZADA")
                        else:
                            data.save_students_dictionary_empty_list(['name','section','spanish_note','english_note','socials_note','sciences_note'])
                        print('   ***Alumno eliminado***')
                        return
                    else:
                        return
    print('\nEl estudiante no existe\n')


#**************** 6 SHOW FAILED NOTES ******************************


def obtain_failed_averages(existing_student_list):
    list_of_students_from_csv = existing_student_list
    if list_of_students_from_csv == False:
        print('\nNo existe un archivo exportado, no hay registros para mostrar\n')
    elif len(list_of_students_from_csv) == 0:
        print('\nNo hay registros para mostrar\n')
    else:
        failed_notes_list = create_failed_averages_dictionary(list_of_students_from_csv)
        print('\n*** Lista de alumnos con materias reprobadas ***\n--------------------------------------------')
        show_failed_notes_list(failed_notes_list)

def create_failed_averages_dictionary(list_of_students_from_csv):
    failed_notes_list =[]
    for student in list_of_students_from_csv:
        failed_notes_student_dictionary = {}
        create_dictionary_of_failed_notes(student,'spanish_note',failed_notes_student_dictionary)
        create_dictionary_of_failed_notes(student,'english_note',failed_notes_student_dictionary)
        create_dictionary_of_failed_notes(student,'socials_note',failed_notes_student_dictionary)
        create_dictionary_of_failed_notes(student,'sciences_note',failed_notes_student_dictionary)
        if not failed_notes_student_dictionary:
            continue
        else:
            failed_notes_list.append(failed_notes_student_dictionary)
    return failed_notes_list


def create_dictionary_of_failed_notes(student,subject,failed_notes_student_dictionary):
    if int(student[subject]) < 60:
        failed_notes_student_dictionary['name'] = student['name']
        failed_notes_student_dictionary['section'] = student['section']
        failed_notes_student_dictionary[subject] = student[subject]
        

def show_failed_notes_list(failed_notes_list):
    for number, index in enumerate(range(len(failed_notes_list)), start=1):
        print(f'\n{number}.- ', end="")
        for concept, value1 in failed_notes_list[index].items():
            print(f'{concept}: {value1}')


#ACTIONS UTILITIES **************************************

def create_all_students_average_dictionary(students_list_from_csv):
    averages_list = []
    for number, student in enumerate(students_list_from_csv):
        average_dictionary = {}
        average = (int(student['spanish_note']) + int(student['english_note']) + int(student['socials_note']) + int(student['sciences_note'])) / 4
        average_dictionary['name'] = student['name']
        average_dictionary['section'] = student['section']
        average_dictionary['average_note'] = average
        averages_list.append(average_dictionary)
    return averages_list

#It adds a new name
def add_new_name():
    while True:
        name = input('Ingrese el nombre del estudiante: ')
        is_name_valid = is_valid_name(name)
        if is_name_valid == True:
            return name

#It Validates name: makes sure it doesn't have numbers in it
def is_valid_name(name):
    if name == "":
        print('El campo de nombre no puede estar vacío. Intente de nuevo.')
        return False
    if any(char.isdigit() for char in name) ==  True:
        print('El nombre no puede contener números. Ingrese un nombre válido')
        return False
    return True


#It Will add student section
def add_new_section():
    while True:
        section = input('Ingrese la sección del estudiante: ').strip()
        is_section_valid = is_valid_section(section)
        if is_section_valid == True:
            return section


#it validates section
def is_valid_section(section):
    pattern = r'^\d{2}+[A-Z]$'
    if re.match(pattern, section):
        return True
    else:
        print('Formato incorrecto, debe ser dos numero enteros seguidos de una letra mayúscula. Intenta de nuevo')


#it asks for a yes or no answer form the user
def yes_or_no(mensaje):
    while True:
        user_response = input(mensaje).lower()
        if user_response in ['si', 'no']:
            if user_response == 'si':
                return True
            else: 
                print('\nOpción inválida, intente de nuevo\n')
                return False



#STUDENT UTILITIES *************************



#Obtain a note from the user and validate it
def obtain_note(subject):
    while True:
            try:
                note = int(input(f'Ingrese la nota de {subject}: '))
                if note >= 0 and note <= 100:
                    return note
                else:
                    print('La nota debe ser un número entero entre 0 y 100')
            except ValueError as ex:
                print('La nota debe ser un número entero entre 0 y 100')


#Validates wether the name and section exist already
def student_exists_def(name, section,existing_student_list):
    
    if existing_student_list == False:
        return False
    else:
        for student in existing_student_list:
            if student['name'].lower() == name.lower():
                if student['section'] == section:
                    return True 
    return False


def student_exists_in_new_student_list_def(name,section,new_students_list):
    for student in  new_students_list:
                if student['name'].lower() == name.lower():
                    if student['section'] == section:
                        return True 
    return False


def student_exists_in_new_student_list_not_imported_yet_def(name,section,new_student_list_not_imported_yet):
    for student in  new_student_list_not_imported_yet:
                if student['name'].lower() == name.lower():
                    if student['section'] == section:
                        return True 
    return False