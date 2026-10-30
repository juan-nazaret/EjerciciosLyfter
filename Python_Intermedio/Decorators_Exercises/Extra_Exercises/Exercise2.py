user_logged_in = False


def requires_login(func):
    def wrapper():
        if user_logged_in == False:
            raise ValueError("Usuario no autenticado")
        func()
    return wrapper


@requires_login
def view_profile():
    print("Mostrando perfil del usuario")

try:
    view_profile()
except ValueError as ex:
    print(ex)