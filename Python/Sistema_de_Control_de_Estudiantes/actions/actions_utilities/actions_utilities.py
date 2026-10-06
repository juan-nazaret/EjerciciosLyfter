import re


def create_all_students_average_dictionary(students_list_from_csv):
    averages_list = []
    for student in students_list_from_csv:
        average_dictionary = {}
        average = (int(student['spanish_note']) + int(student['english_note']) + int(student['socials_note']) + int(student['sciences_note'])) / 4
        average_dictionary['name'] = student['name']
        average_dictionary['section'] = student['section']
        average_dictionary['average_note'] = average
        averages_list.append(average_dictionary)
    return averages_list


def add_new_name():
    while True:
        name = input('Ingrese el nombre del estudiante: ')
        is_name_valid = is_valid_name(name)
        if is_name_valid == True:
            return name

#Validar si el nombre es valido: que no tenga números ni este vacío
def is_valid_name(name):
    if name == "":
        print('El campo de nombre no puede estar vacío. Intente de nuevo.')
        return False
    if any(char.isdigit() for char in name) ==  True:
        print('El nombre no puede contener números. Ingrese un nombre válido')
        return False
    return True


#función que agregará la sección del estudiante
def add_new_section():
    while True:
        section = input('Ingrese la sección del estudiante: ').strip()
        is_section_valid = is_valid_section(section)
        if is_section_valid == True:
            return section


#valida si la sección es válida
def is_valid_section(section):
    pattern = r'^\d{2}+[A-Z]$'
    if re.match(pattern, section):
        return True
    else:
        print('Formato incorrecto, debe ser dos numero enteros seguidos de una letra mayúscula. Intenta de nuevo')


#pedir una respuesta si o no del usuario
def yes_or_no(mensaje):
    while True:
        user_response = input(mensaje).lower()
        if user_response in ['si', 'no']:
            if user_response == 'si':
                return True
            else: 
                return False