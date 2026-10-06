"""
Ejercicio 1

"""

print(" ejercicio 1 *******************************")

Hotel_uno = {
    "name":"ula",
    "number_of_stars": 5,
    "rooms":[{"number" : 101, "floor" : 1, "price_per_night" : 1600 }, 
                    {"number" : 102, "floor": 1, "price_per_night": 1700},
                    {"number" : 103, "floor" : 1, "price_per_night" : 1800}],
}
print(Hotel_uno["rooms"])


"""
Ejercicio 2

"""
print("\n ejercicio 2 *******************************")

list_a = ["first_name", "last_name", "role"]
list_b = ["Alek", "Castillo", "Software Engineer"]
dicc_uno = {}


for i in range(len(list_a)):
    dicc_uno [list_a[i]] = list_b[i]

print(dicc_uno)


"""
Ejercicio 3

"""
print("\n ejercicio 3 *******************************")
list_of_keys = ["access_level", "age"]
employee = {"name": "John", "email": "john@ecorp.com", "access_level": 5, "age": 28}

for i in range(len(list_of_keys)):
    employee.pop(list_of_keys[i])

print(employee)
