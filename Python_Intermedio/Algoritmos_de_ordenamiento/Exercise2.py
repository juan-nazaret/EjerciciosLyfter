def bubble_sort(list_to_sort):
    for outer_index in range(0, len(list_to_sort )- 1):
        print(outer_index)
        for index in range((len(list_to_sort))-1, 0 + outer_index,-1):
            print(f' {index}')

            
            current_item = list_to_sort[index]
            next_item = list_to_sort[index - 1]
            print(f'current item: {current_item}, next item: {next_item} ')
            if current_item < next_item:
                print('current item es mayor que el next item, se van a intercambiar')
                list_to_sort[index] = next_item
                list_to_sort[index - 1] = current_item
            print(list_to_sort)
            

list1 = [10,5,3,9,8,6,5,1,25,-9]
bubble_sort(list1)
print(list1)