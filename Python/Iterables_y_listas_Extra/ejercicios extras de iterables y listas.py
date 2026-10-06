


"""
EJERCICIOS EXTRAS DE ITERABLES Y LISTAS

Ejercicio 1

"""

my_list = []
number = 0
control = "YES"
counter = 0 
while control == "YES":
    number =  int(input("ingresa el numero: "))
    my_list.append(number)
    control = input("would you like to add another number to the list?")
print(f"la lista es: " + str(my_list) + "\n ")    

target_number = int(input("what number would you like to search in the list?"))
for i in range(len(my_list)):
    if my_list[i] == target_number:
        counter += 1
if counter == 0:
    print(f"el numero {number} no esta en la lista")
else: 
    print(f"el numero {number} aparece {counter} veces en la lista")

"""
Ejercicio 2

"""


second_list = [9,1,9,-6,5,2,5,5,5,63,21,0,5,8,-7,4,5,1,6,-3,5,56,4,4,65,45,45]
flag = True
for i in range(len(second_list)):
    if second_list[i] <= 0:
        flag = False
        
if flag == False:
    print("hay al menos un cero o un numero negativo en la lista")
else:
    print("todos los numeros son positivos")

    

"""
Ejercicio 3

"""

third_list = [9,8,7,5,6,2,3,5,4,1,8,7,5,9,6,5,7,4,5,6,3,2,5,0,8,5,5,89]
smallest_number = third_list[0]
for i in range(1, len(third_list) ):
    if third_list[i]< smallest_number:
        smallest_number = third_list[i]

print(f"El numero mas pequeño de la lista es {smallest_number}")

"""
Ejercicio 4

"""

forth_list = []
answer = "YES"
average = 0

#LLENAR LA LISTA
while answer == "YES":
    number = int(input("ingrese el numero: "))
    forth_list.append(number)
    answer = input("quieres agregar otro numero a la lista?  ")

print(f"la lista es {forth_list}")

#CALCULAR PROMEDIO
for i in range(len(forth_list)):
    average = average + forth_list[i]

average = average / len(forth_list)
print(f"el promedio es: {average}")

#LLENAR NUEVA LISTA
forth_list_B = []
for i in range(len(forth_list)):
    if forth_list[i] > average:
        forth_list_B.append(forth_list[i])
print(f"la lista de calificaciones mayores que el promedio es: {forth_list_B}")


"""
Ejercicio 5

"""

fifth_list = []
counter = 0
fifth_list_B = []
while counter < 5 :
    word = input("ingrese la palabra: ")
    fifth_list.append(word)
    counter += 1
#REVISAR QUE PALABRAS TIENEN MAS DE 4 LETRAS
for i in range(len(fifth_list)):
    if len(fifth_list[i]) > 4:
        fifth_list_B.append(fifth_list[i])

print(fifth_list_B)