class User:
    def __init__(self,name):
        self.name = name


def name_twice(func):
    def wrapper(user):
        func(user)
        func(user)
    return wrapper

@name_twice
def show_name(user):
    print(f'Hola, {user.name}')

user = User('juan')
show_name(user)