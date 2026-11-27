def numbers_only(func):
    def wrapper(input_list):
        if not all(isinstance(x,(int,float)) for x in input_list) or any(isinstance(x,bool) for x in input_list):
            raise TypeError('Only numbers are allowed')
        return func(input_list)
    return wrapper

def lists_only(func):
    def wrapper(input_list):
        if not isinstance(input_list,list):
            raise TypeError('Only list type objects are allowed')
        return func(input_list)
    return wrapper


@lists_only
@numbers_only
def bubble_sort(list_to_sort):
    for outer_index in range(0, len(list_to_sort )- 1):
        for index in range(0,(len(list_to_sort) -1)-outer_index):
            current_item = list_to_sort[index]
            next_item = list_to_sort[index + 1]
            print(f'current item: {current_item}, next item: {next_item} ')
            if current_item > next_item:
                print('current item es mayor que el next item, se van a intercambiar')
                list_to_sort[index] = next_item
                list_to_sort[index + 1] = current_item
    return list_to_sort


list1 = [10,5,3,9,8,6,5,1,7]
try:
    bubble_sort(list1)
    print(list1)
except TypeError as ex:
    print(ex)