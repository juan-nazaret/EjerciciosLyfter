from functools import wraps

user_logged_in = False


def requires_login(func):
    @wraps(func)
    def wrapper(*args):
        if not user_logged_in :
            raise PermissionError("Usuario no autenticado")
        return func()
    return wrapper


@requires_login
def view_profile():
    return "Mostrando perfil del usuario"

try:
    print(view_profile())
except PermissionError as ex:
    print(ex)