import data.data



#obtains and prints all the students list
def obtain_all_students():
    students_list_from_csv = data.data.obtain_list_from_csv()
    if students_list_from_csv == False:
        print('\nNo existe un archivo exportado de estudiantes')
    elif len(students_list_from_csv) == 0:
        print(f'\nNo hay estudiantes para mostrar')
    else:
        print('\nMostrar todos los estudiantes*** \n')
        for number, student in enumerate(students_list_from_csv, start=1):
            print(f'Alumno {number}\n------------------\nnombre: {student['name']}\nsección: {student['section']}\nnota de español:{student['spanish_note']}\nnota de inglés:{student['english_note']}\nnota de sociales:{student['socials_note']}\nnota de ciencias:{student['sciences_note']}\n')