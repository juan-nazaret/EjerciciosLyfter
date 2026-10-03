"""
EJERCICIO 1

"""
print("EJERCICIOS EXTRAS DE EXCEPCIONES\n")
print("************** EJERCICIO 1 ****************")
def obtaining_name():
    flag = False
    while flag == False:
        name = input("Ingrese su nombre: ")
        try:
            if name.isdigit():
                raise ValueError("el nombre no puede ser un numero intente de nuevo ")
                next
            else: 
                flag = True
        except ValueError as ex:
            print("error",ex)
            exit
    return name


def obtaining_age():
    flag = False
    while flag == False:
        age = ""
        try:
            age = int(input("Ingrese su edad: "))
            flag = True
        except ValueError as ex:
            print("numero no válido intente de nuevo")
            exit
    return age        


print(f"Hola {obtaining_name()} su edad es {obtaining_age()} ")

"""
EJERCICIO 2 

"""
print("\n************** EJERCICIO 2 ****************")
def convert_to_int(strings_list):
    for i in range(len(strings_list)):
        try:
            aux = int(strings_list[i])
            print(f"'{strings_list[i]}' convertido a: {aux}"  )
        except ValueError as ex:
            print(f"No se pudo convertir el elemento: '{strings_list[i]}' ")


def filling_list():
    flag = True
    my_list = []
    while flag == True:
        aux = str(input("Ingrese el nuevo elemento de la lista: "))
        my_list.append(aux)
        user_answer = ""
        while user_answer not in ["si","no"]:
            user_answer = input("Te gustaría ingresar otro elemento a la lista? si/no: ").lower()
            if user_answer not in ["si", "no"]:
                print("Opción inválida, intente de nuevo (si/no)")
            if user_answer == "no":
                flag = False
    return my_list


strings_list = filling_list()
print(f"\nla lista es: {strings_list}\nResultado: ")
convert_to_int(strings_list)

"""
EJERCICIO 3

"""
print("\n************** EJERCICIO 3 ****************")
def sum_values(values_list):
    total = 0
    for i in range(len(values_list)):
        try:
            aux = float(values_list[i])
            total += aux
            print(f"{aux} sumado correctamente")
        except ValueError as ex:
            print(f"Elemento inválido: {values_list[i]}")
    return float(total)


third_list = filling_list()
print(f"\nLa lista: {third_list}" )
print(f"Total de la suma: {sum_values(third_list)}")