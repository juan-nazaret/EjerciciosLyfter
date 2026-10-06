"""Ejercicio 1"""


number1 = 1
number2 = "54"

#result = number1 + number2
#esta linea de código genera un error TypeError unsupported operand types

print("hola mundo " + "soy Juan")
print("el arroz cuesta ", 54, "pesos")
print(1993, "es el año en que nací")

number_list = [1,5,2,6,9,4,1,5,8,745,4]
second_list = ["uno","dos","tres","cuatro", "cinco"]

print("los numero almacenados en la lista son", number_list)
print(f"""mostraremos dos listas:
      lista 1: {number_list},
      lista 2: {second_list}""")

first_number = 52
second_number = 89.56
print(f"resultado de sumar {first_number} mas {second_number} es: ", first_number + second_number)


flag = True
print(f"lo contrario de {flag} es {not flag}")

"""Ejercicio 2"""

first_name = input("ingrese su nombre")
last_name = input("ingrese su apellido")
age = int(input("Ingrese su edad"))

if age <3:
    print(f"{first_name} {last_name} es un bebé")
elif age > 3 and age < 12:
    print(f"{first_name} {last_name} es un niño")
elif age >= 12 and age < 18:
    print(f"{first_name} {last_name} es un adolescente" )
elif age >= 18 and age <= 35:
    print(F"{first_name} {last_name} es un adulto joven")
elif age > 35 and age < 60:
    print(f"{first_name} {last_name} es un adulto")
elif age >=60 :
    print(f"{first_name} {last_name} es un adulto mayor")
else:
    print("opción invalida")

"""
Ejercicio 3.- 
Cree un programa con un numero secreto del 1 al 10. 
El programa no debe cerrarse hasta que el usuario adivine el numero.
"""

import random
secret_number = random.randint(1,10)
flag = False

while flag == False:

    user_number = int(input("ingrese el numero: "))
    if secret_number != user_number:
        print("el numero esta equivocado, intenta de nuevo")
    else:
        print("felicidades, adivinaste el numero")
        flag = True    

"""#Ejercicio 4.- Cree un programa que le pida tres números al usuario y muestre el mayor."""

greater_number = None
for i in range (3):
    number_list[i] = int(input(f"ingrese el numero {i + 1 }:"))
    if i == 0:
        greater_number = number_list[i]
    else:
        if number_list[i] > greater_number:
            greater_number = number_list[i]
print(f"el numero mayor es {greater_number}") 


"""
************************************************************************************
Ejercicio 5.- Dada n cantidad de notas de un estudiante, calcular:
Cuantas notas tiene aprobadas (mayor a 70).
Cuantas notas tiene desaprobadas (menor a 70).
El promedio de todas.
El promedio de las aprobadas.
El promedio de las desaprobadas.
************************************************************************************
"""

notes_total_amount = int(input("ingrese el numero de notas: "))
approved_notes_amount = 0
failed_notes_amount = 0
approved_notes_average = 0
failed_notes_average = 0
grand_average = 0
 
counter = 0

while counter < notes_total_amount:
    current_note = int(input(f"ingrese la nota {counter + 1}"))
    if current_note >= 0 and current_note <= 100:
            
        if current_note > 70 :
            approved_notes_amount += 1
            approved_notes_average = approved_notes_average + current_note

        else:
            failed_notes_amount += 1
            failed_notes_average = failed_notes_average + current_note
        
        grand_average = grand_average + current_note
        counter += 1

    else:
        print("calificación invalida, intente de nuevo")

if failed_notes_amount == 0 or approved_notes_average == 0:
   print(f"El promedio de las notas reprobatorias es 0")
else:
    failed_notes_average = failed_notes_average / failed_notes_amount
    print(f"el promedio de notas reprobadas es: {failed_notes_average}")

if approved_notes_amount == 0 or approved_notes_average == 0:
    print("El promedio de las notas aprobatorias es 0") 
else:    
    approved_notes_average = approved_notes_average / approved_notes_amount
    print(f"El promedio de las notas aprobadas es: {approved_notes_average}" )
grand_average = grand_average / notes_total_amount

print(f"cantidad de notas aprobadas: {approved_notes_amount}")
print(f"cantidad de notas reprobadas: {failed_notes_amount}")
print(f"el promedio total es: {grand_average}")


