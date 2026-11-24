def numbers_only(function):
    def wrapper(list_of_numbers):
        if len(list_of_numbers) == 0:
            raise ValueError ('Error: La lista esta vacía')
        if  not all(isinstance(x, (int,float)) for x in list_of_numbers):
            raise ValueError('Error: La lista contiene elementos no numéricos')
        return function(list_of_numbers)
    return wrapper




@numbers_only
def bubble_sort(list_to_sort):
    iteration_counter = 0
    changes_counter = 0
    for outer_index in range(0, len(list_to_sort )- 1):
            iteration_counter += 1
            for index in range(0,(len(list_to_sort) -1)-outer_index):
                current_item = list_to_sort[index]
                next_item = list_to_sort[index + 1]
                if current_item > next_item:
                    changes_counter += 1
                    list_to_sort[index] = next_item
                    list_to_sort[index + 1] = current_item
    return list_to_sort,iteration_counter,changes_counter


def bubble_sorting(list_to_sort):
    try:
        list1,iteration_counter, changes_counter = bubble_sort(list_to_sort)
        print(f'Lista ordenada: {list1}\n'\
        f'Iteraciones: {iteration_counter}\n'\
        f'Intercambios: {changes_counter}')
    except ValueError as x:
        print(x)

list1 = [10,5,3,9,8,6,5,1,2.8]
list2 =  [10,5,3,9,8,'hola',5,1,25,8]
list3 = []

print('lista 1: ')
bubble_sorting(list1)
print('\nlista 2: ')
bubble_sorting(list2)
print('\nlista 3: ')
bubble_sorting(list3)




