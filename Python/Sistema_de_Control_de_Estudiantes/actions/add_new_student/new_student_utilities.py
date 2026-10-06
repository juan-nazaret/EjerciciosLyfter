import data.data



#Pedir una nota y validar si es valida
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


#Valida si el nombre y la sección ya existen
def student_exists(name, section):
    student_list_from_csv = data.data.obtain_list_from_csv()
    if student_list_from_csv == False:
        return False
    else:
        for student in student_list_from_csv:
            if student['name'].lower() == name.lower():
                if student['section'] == section:
                    return True 
    return False

#Pide y valida el nombre