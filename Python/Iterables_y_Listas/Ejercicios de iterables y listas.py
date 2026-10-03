""" 
Primer ejercicio

"""
print("***** primer ejercicio ***** \n")
first_list = ['Hay', 'en', 'que', 'iteracion', 'indices', 'muy']
second_list = ['casos', 'los', 'la', 'por', 'es', 'util']

for index in range(0,len(first_list)):
    print(first_list[index])
    print(second_list[index])

"""
Segundo ejercicio

"""
print("\n ***** segundo ejercicio ***** \n")
my_string = 'Pizza con Piña'

for i in range(len(my_string) -1, -1, -1):
    print(my_string[i])

"""
Tercer ejercicio

"""
print("\n ***** tercer ejercicio ***** \n")
my_list = [4,3,6,1,0,5,0,5,9,8,6,7]
aux = my_list[-1]
my_list.insert(-1,my_list[0] )
my_list.pop(-1)
my_list.insert(0,aux)
my_list.pop(1)
print(my_list)



"""
Cuarto ejercicio

"""
print("\n ***** cuarto ejercicio ***** \n")


my_numbers_list= [1,2,3,4,5,6,7,8,9]

i = 0

while i < len(my_numbers_list):

    if my_numbers_list[i] % 2 != 0:
        my_numbers_list.pop(i)
    else:
        i += 1    

print(my_numbers_list)

"""
Quinto ejercicio

"""
print("\n ***** quinto ejercicio ***** \n")

my_other_list = []
higher_number = 0 
for i in range(10):

    number = int(input("ingresa el numero "))
    my_other_list.append(number)

for i in range(len(my_other_list)):
    if my_other_list[i] == 0:
        higher_number = my_other_list
    elif my_other_list[i] > higher_number:
        higher_number = my_other_list[i]    

print(my_other_list)
print(f"el numero mas grande es: {higher_number}" )
