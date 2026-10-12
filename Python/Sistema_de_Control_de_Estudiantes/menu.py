import actions
import data


#To show MAIN MENU
def show_menu():
    is_there_an_exported_list = False
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
                actions.create_new_student(new_students_list)
            case 2: 
                actions.obtain_all_students(new_students_list)
            case 3:
                actions.obtain_highest_average(new_students_list)
            case 4:
                actions.see_all_students_average(new_students_list)
            case 5: 
                actions.delete_student(new_students_list)
            case 6:
                actions.obtain_failed_averages(new_students_list)
            case 7: 
                data.save_students_dictionary_list(new_students_list)
            case 8:
                data.obtain_list_from_csv(new_students_list)
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

