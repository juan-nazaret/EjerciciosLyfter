import data.data


def obtain_failed_averages():
    list_of_students_from_csv = data.data.obtain_list_from_csv()
    if list_of_students_from_csv == False:
        print('\nNo existe un archivo exportado, no hay registros para mostrar\n')
    elif len(list_of_students_from_csv) == 0:
        print('\nNo hay registros para mostrar\n')
    else:
        failed_notes_list = create_failed_averages_dictionary(list_of_students_from_csv)
        print(type(failed_notes_list))
        print('\n*** Lista de alumnos con materias reprobadas ***\n--------------------------------------------')
        show_failed_notes_list(failed_notes_list)

def create_failed_averages_dictionary(list_of_students_from_csv):
    failed_notes_list =[]
    for student in list_of_students_from_csv:
        failed_notes_student_dictionary = {}
        x(student,'spanish_note',failed_notes_student_dictionary)
        x(student,'english_note',failed_notes_student_dictionary)
        x(student,'socials_note',failed_notes_student_dictionary)
        x(student,'sciences_note',failed_notes_student_dictionary)
        failed_notes_list.append(failed_notes_student_dictionary)
    return failed_notes_list


def x(student,subject,failed_notes_student_dictionary):
    if int(student[subject]) < 60:
        failed_notes_student_dictionary['name'] = student['name']
        failed_notes_student_dictionary['section'] = student['section']
        failed_notes_student_dictionary[subject] = student[subject]

def show_failed_notes_list(failed_notes_list):
    for number, i in enumerate(range(len(failed_notes_list)), start=1):
        print(f'\n{number}.- ', end="")
        for concept, value1 in failed_notes_list[i].items():
            print(f'{concept}: {value1}')
