from datetime import datetime
from functools import wraps
import math

def log_call(func):
    @wraps(func)
    def wrapper(*args):
        result = func(*args)
        print(f'func:{func.__name__} - args:{args} - {datetime.now()} - Resultado: {result}')
        return result
    return wrapper


def validate_numbers(func):
    @wraps(func)
    def wrapper(*args):
        if all(isinstance(x,(int,float)) and (type(x) is not bool) for x in args) :
            return func(*args)
        else:
            raise ValueError('No todos los argumentos son números')
    return wrapper

@validate_numbers
@log_call
def multiply(*args):
    result = math.prod(args)
    return result

def call_multiply(*args):
    try:
        result = multiply(*args)
        print(f"Resultado: {result}")
    except ValueError as ex:
        print(ex)

call_multiply(1,3)
call_multiply(True,2,5)
call_multiply('p',6)

