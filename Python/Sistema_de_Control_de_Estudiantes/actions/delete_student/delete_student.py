import data.data
import actions.actions_utilities.actions_utilities



def obtain_student_data():
    name = actions.actions_utilities.actions_utilities.add_new_name()
    section = actions.actions_utilities.actions_utilities.add_new_section()
    return name,section


def delete_student():
    list_of_students_from_csv = data.data.obtain_list_from_csv()
    if list_of_students_from_csv == False:
        print('\nNo existe un archivo exportado, no hay alumnos para mostrar o eliminar\n')
        return
    elif len(list_of_students_from_csv) == 0:
        print(f'No hay registros para mostrar o eliminar\n')
        return
    else:
        name,section = obtain_student_data()
        for i in range(len(list_of_students_from_csv)):
            if list_of_students_from_csv[i]['name'].lower() == name.lower():
                if list_of_students_from_csv[i]['section'] == section:
                    print(f'Estudiante a eliminar: nombre:{name} sección:{section}')
                    user_response = actions.actions_utilities.actions_utilities.yes_or_no('Desea continuar? si/no: ')
                    if user_response == True:
                        list_of_students_from_csv.pop(i)
                        if len(list_of_students_from_csv) > 0:
                            data.data.save_students_dictionary_list(list_of_students_from_csv)
                        else:
                            data.data.save_students_dictionary_empty_list(['name','section','spanish_note','english_note','socials_note','sciences_note'])
                        print('***Alumno eliminado***')
                        return
                    else:
                        return
    print('\nEl estudiante no existe\n')
