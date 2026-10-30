from datetime import datetime

def log_call(func):
    def wrapper(*args):
        print(f'func:{func.__name__} - args:{args} - {datetime.now()} -  {func(*args)}')
    return wrapper


def validate_numbers(func):
    def wrapper(*args):
        if all(isinstance(x,(int,float)) for x in args):
            func(*args)
        else:
            raise ValueError('No todos los argumentos son números')
    return wrapper

@validate_numbers
@log_call
def multiply(*args):
    result = args[0] * args[1]
    return f'Resultado: {result}'


try:
    multiply(2,'p')
except ValueError as ex:
    print(ex)
