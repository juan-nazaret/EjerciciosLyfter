import actions.actions_utilities.actions_utilities
import data.data

def see_all_students_average():
    students_list_from_csv = data.data.obtain_list_from_csv()
    if students_list_from_csv == False:
        print(f'\nNO hay un archivo exportado de alumnos')
    elif len(students_list_from_csv) == 0:
        print('NO hay registros de estudiantes para mostrar')
    else:
        all_students_average_list = actions.actions_utilities.actions_utilities.create_all_students_average_dictionary(students_list_from_csv)
        print(f'\n***Mostrar todos los promedios****\n-------------------------------------------')
        for number, i in enumerate(range(len(all_students_average_list)),start=1): 
            print(f'{number}.- name:{all_students_average_list[i]['name']} sección: {all_students_average_list[i]['section']} promedio: {all_students_average_list[i]['average_note']}')