from datetime import datetime

def log_call(func):
    def wrapper(*args):
        result = func(*args)
        print(f'func:{func.__name__} - args:{args} - {datetime.now()} -  {func(*args)}')
        return result
    return wrapper


def validate_numbers(func):
    def wrapper(*args):
        if all(isinstance(x,(int,float)) for x in args):
            return func(*args)
        else:
            raise ValueError('No todos los argumentos son números')
    return wrapper

@validate_numbers
@log_call
def multiply(*args):
    result = args[0] * args[1]
    return f'Resultado: {result}'


try:
    result = multiply(2,5)
except ValueError as ex:
    print(ex)

