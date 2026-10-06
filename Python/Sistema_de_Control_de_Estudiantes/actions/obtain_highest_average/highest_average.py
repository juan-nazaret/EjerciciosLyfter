import data.data
import actions.actions_utilities.actions_utilities

def obtain_highest_average():
    students_list_from_csv = data.data.obtain_list_from_csv()
    if students_list_from_csv == False:
        print('No existe un archivo exportado')
    else: 
        averages_list = actions.actions_utilities.actions_utilities.create_all_students_average_dictionary(students_list_from_csv)
        averages_list.sort(reverse= True, key=myFunc)
        top_3_list = obtain_top_3(averages_list)
        print('\nTOP 3 ********\n_________________________\n')
        for number, i in enumerate (range(len(top_3_list)),start=1):
            try:
                print(f'{number}: nombre: {top_3_list[i]['name']}, sección: {top_3_list[i]['section']}, promedio: {top_3_list[i]['average_note']}')
            except KeyError as ex:
                print(f'{number}:')

def myFunc(e):
    return e['average_note']


def obtain_top_3(averages_list):
    print(f'averages list: {averages_list}')
    top_3_list = []
    for i in range(0,3):
        try:
            top_3_list.append(averages_list[i])
        except IndexError as ex:
            top_3_list.append({})
    return top_3_list
    


