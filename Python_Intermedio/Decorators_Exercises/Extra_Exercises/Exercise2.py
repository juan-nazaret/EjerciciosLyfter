user_logged_in = True


def requires_login(func):
    def wrapper():
        if user_logged_in == False:
            raise ValueError("Usuario no autenticado")
        return func()
    return wrapper


@requires_login
def view_profile():
    return "Mostrando perfil del usuario"

try:
    print(view_profile())
except ValueError as ex:
    print(ex)