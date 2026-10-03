"""
Ejercicio 1

"""

def prints_something():
    print("something")


def prints_something_and_something_else():
    print("Ejercicio 1 : this prints ")
    prints_something()


prints_something_and_something_else()


"""
Ejercicio 2

"""
#variable global
x = 96



def second_function():
    global x
    x = 3

"""
def first_function():
    y = 57


def second_function():
    x = 56

        
print(y)
print(x)

"""
second_function()
print(f"\nEjercicio 2 : {x}")


"""
Ejercicio 3

"""

def list_sum(numbers_list):
    suma = 0
    for i in range(len(numbers_list)):
        
        suma = suma + numbers_list[i]
    return suma


numbers_list =[4, 6, 2, 29] 
print(f"\nEjercicio 3 : {list_sum(numbers_list)}")



"""
Ejercicio 4: 

"""

def string_backwards(my_string):
    my_word_list = []
    for i in range(len(my_string) -1, -1, -1):
        my_word_list.append(my_string[i])
    word = "".join(my_word_list)
    print(f"\nEJERCICIO 4: {word}")

my_string = "Hola mundo"
string_backwards(my_string)


"""
Ejercicio 5: 

"""


my_word = "Hola mundo yo soy Juan Nazaret 223Oo"
def upper_lower_cases(my_word):

    capital_letters = 0
    lower_letters = 0

    for i in range(len(my_word)):
        if my_word[i].isalpha():   
            if my_word[i].isupper():
                capital_letters = capital_letters + 1 
            elif my_word[i].islower():
                lower_letters = lower_letters + 1
    print(f"\nEJERCICIO 5 : There are {capital_letters} upper cases and {lower_letters} lower cases" )


upper_lower_cases(my_word)

"""
Ejercicio 6: 

"""

def creating_words_list(word):
    new_word = ""
    words_list = []
    for i in range(len(word)):
        if word[i] != "-":
            new_word = new_word + word[i]
            if i == len(word) -1:
                words_list.append(new_word)
        elif word[i] == "-" :
                words_list.append(new_word)
                new_word = ""
    ordered_words = "-".join(sorted(words_list))
    print(f"\nEJERCICIO 6: {ordered_words}")


creating_words_list("hola-cachorro-perro-rico-hello-yo-mas-dos")

"""
Ejercicio 7: 

"""

def is_it_prime_number(numbers_list):
    prime_list = []
    prime = True
    for i in range(len(numbers_list)):
        prime = True
        number = numbers_list[i]
        if number < 2 :
            prime = False
        for n in range(2,number):
            if number % n == 0:
                prime = False
                
        if prime == True:
            prime_list.append(number)
    print(f"\nEJERCICIO 7: {prime_list}")


is_it_prime_number([5,9,3,6,7,8,4,2,5,69,58,47,52,41,63,55,88])