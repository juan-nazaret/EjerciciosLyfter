import actions.add_new_student.new_student
import actions.see_all_students.see_all_students
import actions.obtain_highest_average.highest_average
import actions.see_all_averages.see_all_students_averages
import actions.delete_student.delete_student
import actions.see_failed_averages.see_failed_averages

#Mostrar menu
def show_menu():
    while True:
        print('\n \n***************** MENÚ *****************\n' \
        '1.- Ingresar un nuevo estudiante\n' \
        '2.- Ver todos los estudiantes\n' \
        '3.- Ver top 3 de promedios\n' \
        '4.- Ver promedio de todos los estudiantes\n' \
        '5.- Eliminar estudiante\n' \
        '6.- Ver los alumnos con materias reprobadas\n' \
        '7.- Salir\n')

        user_menu_selection = obtain_user_menu_selection()
        
        match user_menu_selection:  
            case 1:
                actions.add_new_student.new_student.create_new_student()
            case 2: 
                actions.see_all_students.see_all_students.obtain_all_students()
            case 3:
                actions.obtain_highest_average.highest_average.obtain_highest_average()
            case 4:
                actions.see_all_averages.see_all_students_averages.see_all_students_average()
            case 5: 
                actions.delete_student.delete_student.delete_student()
            case 6:
                actions.see_failed_averages.see_failed_averages.obtain_failed_averages()
            case 7:
                print('\n\n***SESIÓN TERMINADA***\n\n')
                break



#Obtener y verificar que la respuesta del menu sea valida
def obtain_user_menu_selection():
    while True: 
        try:
            user_menu_selection = int(input("\nIngrese su selección del menú: "))
            if user_menu_selection not in [1,2,3,4,5,6,7]:
                print('Ingrese una opción válida. Intente de nuevo')
            else:
                return user_menu_selection
        except ValueError as ex:
            print('Opción inválida. Intente de nuevo.')

