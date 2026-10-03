"""
**********************************************
Ejercicios  extras de sintaxis Python
Ejercicio 1.1
**********************************************
"""


price = int(input("ingrese el precio del producto"))
if price < 100:
    final_price = price - (price * .02)
else:
    final_price = price - (price * .10)

print(f"el precio después del descuento es: {final_price}")


"""
************************************************
Ejercicio 1.2
************************************************
"""

time_in_seconds = int(input("Ingrese el tiempo en segundos: "))
if time_in_seconds > 600:
    print("Mayor")
elif time_in_seconds < 600:
    print("Faltan ", (600 - time_in_seconds), " segundos para llegar a 10 minutos")
else:
    print("Igual")

"""
************************************************
Ejercicio 1.3
************************************************
"""

number = int(input("Ingrese el numero"))
auxiliar = 1 
outcome = 0
counter = 1

while counter <= number:
    outcome = outcome + counter
    counter = counter + 1

print(f"la suma es: {outcome}")

"""
************************************************
Ejercicio 2
************************************************
"""

result = 0
my_list = []
flag = False
#llenado de la lista con los números
for i in range (3):
    my_list.append (int(input(f"ingrese el numero {i+1}: ")))

#validar si la suma de todos es 30 
if my_list[0] + my_list [1] + my_list[2] == 30 :
        print(f"Correcto,la suma de los numero es 30")
else:
#validar si unos de ellos es 30
    for i in range (3):
        if my_list[i] == 30:
            print(f"correcto, el numero en el lugar {i+1} es 30 ")
            break
        elif i == 2:
            print("incorrecto")

"""
************************************************
Ejercicio 3
************************************************
"""
temperature = float(input("ingrese la temperatura en grados Celsius"))
Fahrenheit = float((temperature * 1.8) + 32)
kelvin = float(temperature + 273.15)
print(f"""
 Fahrenheit: {Fahrenheit},
      kelvin: {kelvin},
""")


"""
************************************************
Ejercicio 4
************************************************
"""

number = int(input("ingrese un numero del 1 al 10: "))
for i in range (1,13):
    print(f"{number} x {i} = {number * i}")
      