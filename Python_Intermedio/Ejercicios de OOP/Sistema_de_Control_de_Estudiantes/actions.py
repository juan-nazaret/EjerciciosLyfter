import re

#**************** 1 ADD NEW STUDENT ******************************

#NEW STUDENT*****
#fill in new student logic
def create_new_student_main(new_students_list):

    print('\nAGREGAR NUEVO ESTUDIANTE ***')
    name = add_new_name()

    section = add_new_section()

    student_exists_var =  student_exists(name,section, new_students_list)
    if student_exists_var == True:
        print('El estudiante ya existe en esta sección.')
        return False

    spanish_note = obtain_note('spanish')
    english_note = obtain_note('english')
    socials_note = obtain_note('socials')
    sciences_note = obtain_note('sciences')

    #creates the student object
    student_object = Student(name,section,spanish_note, english_note,socials_note,sciences_note)

    return student_object


#It creates a list of dictionaries of new students and returns it 
def create_new_student(new_students_list):
    while True:
        student_object = create_new_student_main(new_students_list)
        if student_object == False:
            create_another_student = user_response()
            if create_another_student == 'no':
                return 
        elif student_object == None:
            return 
        else: 
            new_students_list.append(student_object)
            create_another_student = user_response()
            if create_another_student == 'no':
                return 
        

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
def obtain_all_students(new_students_list):
    if len(new_students_list) == 0:
        print('\nNo hay registros para mostrar')
    else:
        print('\nMostrar todos los estudiantes*** \n')
        for number, student in enumerate(new_students_list, start=1):
            print(f'Alumno {number}\n------------------\nnombre: {student.name}\nsección: {student.section}\nnota de español:{student.spanish_note}\nnota de inglés:{student.english_note}\nnota de sociales:{student.socials_note}\nnota de ciencias:{student.sciences_note}\n')


#**************** 3 TOP 3 STUDENTS ******************************


def obtain_highest_average(new_students_list):
    if len(new_students_list) == 0 :
        print('\nNo hay archivos para mostrar')
        return 
    else: 
        averages_list = create_all_students_average_dictionary(new_students_list)
        averages_list.sort(reverse= True, key=sort_list)
        top_3_list = obtain_top_3(averages_list)
        print('\nTOP 3 ********\n_________________________\n')
        for number, student in enumerate(top_3_list, start=1):
            try:
                print(f'{number}: nombre: {student["name"]}, sección: {student["section"]}, promedio: {student["average_note"]}')
            except KeyError as ex:
                print(f'{number}:')

def sort_list(data):
    return data['average_note']


def obtain_top_3(averages_list):
    top_3_list = []
    for index in range(0,3):
        try:
            if averages_list[index] != None:
                top_3_list.append(averages_list[index])
        except IndexError as ex:
            continue
    return top_3_list

    
#**************** 4 SHOW ALL STUDENTS AVERAGES ******************************


def see_all_students_average(new_students_list):
    
    if len(new_students_list) == 0:
        print('NO hay registros de estudiantes para mostrar')
        return
    else:
        all_students_average_list = create_all_students_average_dictionary(new_students_list)
        print(f'\n***Mostrar todos los promedios****\n-------------------------------------------')
        for number, index in enumerate(range(len(all_students_average_list)),start=1): 
            print(f'{number}.- name:{all_students_average_list[index]["name"]} sección: {all_students_average_list[index]["section"]} promedio: {all_students_average_list[index]["average_note"]}')


#**************** 5 DELETE A STUDENT ******************************

def obtain_student_data():
    name = add_new_name()
    section = add_new_section()
    return name,section


def delete_student(new_students_list):
    if len(new_students_list) == 0:
        print(f'No hay registros para mostrar o eliminar\n')
        return
    else:
        name,section = obtain_student_data()
        for index in range(len(new_students_list)):
            if new_students_list[index].name.lower() == name.lower():
                if new_students_list[index].section == section:
                    print(f'El estudiante a eliminar ---> nombre: {name} sección: {section}')
                    user_response = yes_or_no('Desea continuar? si/no: ')
                    if user_response == True:
                        new_students_list.pop(index)
                        print('\n*** Alumno Eliminado ***')
                        return 
                    else:
                        print(f'\n*** Proceso de eliminación cancelado ***')
                        return
    print('\nEl estudiante no existe\n')


#**************** 6 SHOW FAILED NOTES ******************************


def obtain_failed_averages(new_students_list):
    if len(new_students_list) == 0:
        print('\nNo hay registros para mostrar\n')
    else:
        failed_notes_list = create_failed_averages_dictionary(new_students_list)
        if len(failed_notes_list) == 0:
            print('\n*** no hay datos para mostrar ***')
        else:
            print('\n*** Lista de alumnos con materias reprobadas ***\n--------------------------------------------')
            show_failed_notes_list(failed_notes_list)

def create_failed_averages_dictionary(new_students_list):
    failed_notes_list =[]
    for student in new_students_list:
        failed_notes_student_dictionary = {}
        create_dictionary_of_failed_notes(student,failed_notes_student_dictionary)
        if not failed_notes_student_dictionary:
            continue
        else:
            failed_notes_list.append(failed_notes_student_dictionary)
    print(f'failed notes list {failed_notes_list}')
    return failed_notes_list


def create_dictionary_of_failed_notes(student,failed_notes_student_dictionary):
    
    if int(student.spanish_note) < 60:
        failed_notes_student_dictionary['name'] = student.name
        failed_notes_student_dictionary['section'] = student.section
        failed_notes_student_dictionary['spanish_note'] = student.spanish_note
    if int(student.english_note) < 60:
        failed_notes_student_dictionary['name'] = student.name
        failed_notes_student_dictionary['section'] = student.section
        failed_notes_student_dictionary['english_note'] = student.english_note
    if int(student.socials_note) < 60:
        failed_notes_student_dictionary['name'] = student.name
        failed_notes_student_dictionary['section'] = student.section
        failed_notes_student_dictionary['socials_note'] = student.socials_note
    if int(student.sciences_note) < 60:
        failed_notes_student_dictionary['name'] = student.name
        failed_notes_student_dictionary['section'] = student.section
        failed_notes_student_dictionary['sciences_note'] = student.sciences_note

def show_failed_notes_list(failed_notes_list):
    for number, index in enumerate(range(len(failed_notes_list)), start=1):
        print(f'\n{number}.- ', end="")
        for concept, value1 in failed_notes_list[index].items():
            print(f'{concept}: {value1}')


#ACTIONS UTILITIES **************************************

def create_all_students_average_dictionary(new_students_list):
    averages_list = []
    for number, student in enumerate(new_students_list):
        average_dictionary = {}
        average = (int(student.spanish_note) + int(student.english_note) + int(student.socials_note) + int(student.sciences_note)) / 4
        average_dictionary['name'] = student.name
        average_dictionary['section'] = student.section
        average_dictionary['average_note'] = average
        averages_list.append(average_dictionary)
        print()
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
    pattern = r'^\d{2}[A-Z]$'
    if re.match(pattern, section):
        return True
    else:
        print('Formato incorrecto, debe ser dos numero enteros seguidos de una letra mayúscula. Intenta de nuevo')


#it asks for a yes or no answer form the user
def yes_or_no(message):
    while True:
        user_response = input(message).lower()
        if user_response in ['si', 'no']:
            if user_response == 'si':
                return True
            else:
                return False
        else: 
            print('\nOpción inválida, intente de nuevo\n')



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
def student_exists(name, section,new_students_list):
    if len(new_students_list) == 0:
        return False
    else:
        for student in new_students_list:
            if student.name.lower() == name.lower():
                if student.section == section:
                    return True 
    return False


class Student():
    def __init__(self, name,section,spanish_note, english_note,socials_note,sciences_note):
        self.name = name
        self.section = section
        self.spanish_note = spanish_note
        self.english_note = english_note
        self.socials_note = socials_note
        self.sciences_note = sciences_note