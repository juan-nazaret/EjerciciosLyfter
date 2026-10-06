import actions.add_new_student.new_name
import actions.add_new_student.new_section
import actions.add_new_student.new_spanish_note
import actions.add_new_student.new_english_note
import actions.add_new_student.new_socials_note
import actions.add_new_student.new_sciences_note
import actions.add_new_student.new_student_utilities
import data.data


#Lógica de llenar el nuevo estudiante
def create_new_student_main():
    student_dictionary = {}

    print('\nNUEVO ESTUDIANTE ***')
    name = actions.add_new_student.new_name.add_new_name()
    student_dictionary['name'] = name

    section = actions.add_new_student.new_section.add_new_section()
    student_dictionary['section'] = section

    student_exists =  actions.add_new_student.new_student_utilities.student_exists(name,section)
    if student_exists == True:
        print('El estudiante ya existe en esta sección.')
        return 

    spanish_note = actions.add_new_student.new_spanish_note.add_spanish_note()
    student_dictionary['spanish_note'] = spanish_note

    english_note = actions.add_new_student.new_english_note.add_new_english_note()
    student_dictionary['english_note'] = english_note

    socials_note = actions.add_new_student.new_socials_note.add_new_socials_note()
    student_dictionary['socials_note'] = socials_note

    sciences_note = actions.add_new_student.new_sciences_note.add_new_sciences_note()
    student_dictionary['sciences_note'] = sciences_note

    
    data.data.save_students_dictionary(student_dictionary)
    

    


#Crear un nuevo estudiante
def create_new_student():
    while True:
        create_new_student_main()
        create_another_student = user_response()
        if create_another_student == 'no':
            break

#Verificar si el usuario quiere crear un nuevo estudiante
def user_response():
    while True:
        create_another_student = input('Quiere crear otro estudiante? SI/NO').lower()
        if create_another_student in ['si','no']:
            return create_another_student
        else:
            print('Respuesta invalida. Intenta de nuevo.')





