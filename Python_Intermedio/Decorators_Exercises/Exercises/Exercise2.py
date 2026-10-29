def numbers_only(func):
    def wrapper(*args):
        if not all(isinstance(item,(int,float)) for item in args):
            raise ValueError('Not all items are numbers')
        func(*args)
    return wrapper

@numbers_only
def show_numbers(*args):
    print(*args)

try:
    show_numbers(1,5,6,'p',6,3,9,3)
except ValueError as ex:
    print(ex)