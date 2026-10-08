import actions
import data


#To show MAIN MENU
def show_menu():
    existing_student_list = False
    new_students_list=[]
    while True:

        print('\n \n***************** MENÚ *****************\n' \
        '1.- Ingresar un nuevo estudiante\n' \
        '2.- Ver todos los estudiantes\n' \
        '3.- Ver top 3 de promedios\n' \
        '4.- Ver promedio de todos los estudiantes\n' \
        '5.- Eliminar estudiante\n' \
        '6.- Ver los alumnos con materias reprobadas\n' \
        '7.- Exportar lista de nuevos alumnos\n' \
        '8.- Importar archivo de lista de alumnos existentes\n'
        '9.- Salir\n')

        user_menu_selection = obtain_user_menu_selection()
        
        match user_menu_selection:  
            case 1:
                new_students_list = actions.create_new_student(existing_student_list,new_students_list)
                print('***LISTA IMPORTADA***')
            case 2: 
                actions.obtain_all_students(existing_student_list)
            case 3:
                actions.obtain_highest_average(existing_student_list)
            case 4:
                actions.see_all_students_average(existing_student_list)
            case 5: 
                actions.delete_student(existing_student_list)
                existing_student_list = data.obtain_list_from_csv()
            case 6:
                actions.obtain_failed_averages(existing_student_list)
            case 7: 
                list_was_exported = data.save_students_dictionary_list(new_students_list)
                if list_was_exported == True:
                    new_students_list.clear()
                existing_student_list = data.obtain_list_from_csv()
            case 8:
                existing_student_list = data.obtain_list_from_csv()
            case 9:
                print('\n\n***SESIÓN TERMINADA***\n\n')
                break



#Verifies the users entry 
def obtain_user_menu_selection():
    while True: 
        try:
            user_menu_selection = int(input("\nIngrese su selección del menú: "))
            if user_menu_selection not in [1,2,3,4,5,6,7,8,9]:
                print('Ingrese una opción válida. Intente de nuevo')
            else:
                return user_menu_selection
        except ValueError as ex:
            print('Opción inválida. Intente de nuevo.')

