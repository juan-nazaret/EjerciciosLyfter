class NonExistingOption(Exception):
    def __init__(self):
        super().__init__("La opción ingresada no existe dentro del menú \n")


def addition(number1, number2):
    result = 0 
    try:
        result = number1 + number2
    except  TypeError as ex:
        print("el caracter ingresado no es un numero")
        print(ex)
    return result 


def subtraction(number1, number2):
    result = 0 
    try:
        result = number1 - number2
    except TypeError as ex:
        print("el caracter ingresado no es un numero")
        print(ex)
    return result


def multiplication(number1, number2):
    result = 0
    try: 
        result = number1 * number2
    except TypeError as ex:
        print("el caracter ingresado no es un numero")
        print(ex)
    return result


def division(number1,number2):
    result = 0 
    try: 
        result = number1 / number2
    except TypeError as ex:
        print("el caracter ingresado no es un numero")
        print(ex)
    except ZeroDivisionError as ex:
        print("Estas intentando dividir entre cero")
        print(ex)
    return result


def menu():
    user_selection = 0
    while user_selection not in [1,2,3,4,5,6]:  
        try:
            user_selection = int(input("Elija una opción \n1. Suma"\
                                "\n2. Resta"\
                                "\n3. Multiplicación"
                                "\n4. Division"\
                                "\n5. Borrar resultado"\
                                "\n6. Salir\n Ingrese su elección: "))
        except ValueError as ex:
            print("El valor ingresado no es válido\n")
        try:
            if user_selection not in [1,2,3,4,5,6]:
                raise NonExistingOption
        except NonExistingOption as e:
            print(f"Hubo un error: {e}")        
    return user_selection


def make_another_calculation():
    user_answer = ""
    while user_answer not in ["si","no"]:
        try:
            user_answer = (input("Deseas hacer otra operación? ")).lower()
            print(user_answer)
            if user_answer == "si":
                user_selection = menu()
                return user_selection
            elif user_answer == "no":
                user_selection = 6
            elif user_answer.isalpha:
                print(f"intenta de nuevo {user_answer} no es una respuesta valida. Ingresa SI o NO")
        except TypeError as ex:
            print("La respuesta no es válida")
            print(ex)  
    return user_selection  


def obtaining_user_number():
    flag = False
    user_number = 0
    while flag == False: 
        try:
            user_number = int(input("ingrese un numero: "))
            flag = True
        except ValueError as ex:
            print(f"El caracter ingresado no es un número. Ingrese un número para continuar: ")
    return user_number


def main(user_selection, current_number):
    while user_selection != 6:
        match user_selection:
            case 1:
                user_number= obtaining_user_number()
                result = addition(current_number,user_number)
                print(f"El resultado de sumar {current_number} + {user_number} es {result}")
                current_number = result
                user_selection = make_another_calculation()
            case 2:
                user_number = obtaining_user_number()
                result = subtraction(current_number,user_number)
                print(f"El resultado de restar {user_number} a {current_number} es {result}")
                current_number = result
                user_selection =  make_another_calculation()
                print(user_selection)
            case 3:
                user_number = obtaining_user_number()
                result = multiplication(current_number,user_number)
                print(f"El resultado de multiplicar {current_number} por {user_number} es {result}")
                current_number = result
                user_selection =  make_another_calculation()
            case 4:
                user_number = obtaining_user_number()
                result = division(current_number,user_number)
                print(f"El resultado de dividir {current_number} entre {user_number} es {result} ")
                current_number = result
                user_selection =  make_another_calculation()
            case 5: 
                current_number = 0
                print(f"El numero actual es: {current_number}")
                user_selection = make_another_calculation()


current_number = 6
user_selection = menu()
main(user_selection, current_number)
print("\n*************ADIOS************")