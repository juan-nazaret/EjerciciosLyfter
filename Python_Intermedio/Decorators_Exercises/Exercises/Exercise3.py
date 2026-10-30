from datetime import date


class User:
    def __init__(self, date_of_birth):
        self.date_of_birth = date_of_birth

    @property
    def age(self):
        today = date.today()
        years = today.year - self.date_of_birth.year

        if (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day):
            years -= 1

        return years

def adult_only(func):
    def wrapper(user):
        if not user.age >= 18:
            raise ValueError('El usuario no es mayor de edad')
        func(user)
    return wrapper

@adult_only
def access(user):
    print(f'Granted access your age is {user.age}, enjoy')


user = User(date(1993,8,29))
try:
    access(user)
except ValueError as ex:
    print(ex)