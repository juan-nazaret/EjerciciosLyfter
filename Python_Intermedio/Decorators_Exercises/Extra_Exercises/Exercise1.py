class User:
    def __init__(self,name):
        self.name = name


def name_twice(func):
    def wrapper(user):
        return f"{func(user)}\n{func(user)}"
    return wrapper

@name_twice
def show_name(user):
    return f'Hola, {user.name}'

user = User('juan')
print(show_name(user))
