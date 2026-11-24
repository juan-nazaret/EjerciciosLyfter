def bubble_sort(list_to_sort):
    iteration_counter = 0
    changes_counter = 0
    changes_happened =  False
    for outer_index in range(0, len(list_to_sort )- 1):
            iteration_counter += 1
            for index in range(0,(len(list_to_sort) -1)-outer_index):
                current_item = list_to_sort[index]
                next_item = list_to_sort[index + 1]
                if current_item > next_item:
                    changes_happened = True
                    changes_counter += 1
                    list_to_sort[index] = next_item
                    list_to_sort[index + 1] = current_item
            if changes_happened == False:
                            break
                
    return list_to_sort,iteration_counter,changes_counter

list1 = [True,2,3,4,5]
list1,iteration_counter, changes_counter = bubble_sort(list1)
print(f'Lista ordenada: {list1}\n'\
    f'Iteraciones: {iteration_counter}\n'\
    f'Intercambios: {changes_counter}')