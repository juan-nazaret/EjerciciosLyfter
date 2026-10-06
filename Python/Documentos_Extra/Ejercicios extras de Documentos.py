"""
EJERCICIO 1

"""
print("\n***********EJERCICIO 1*************")
def read_text(path):
    with open(path, 'r', encoding= 'utf-8') as file:
        lines = file.readlines()
    return lines


def create_new_list(path, text):
    with open(path, 'w', encoding= 'utf-8') as file:
        for number, line in enumerate(text, start = 1):
            file.write(f'{line.strip()} ')


def shows_new_doc(path):
    with open(path, 'r', encoding= 'utf-8') as file:
        hola_mundo_2 = file.read()
    return hola_mundo_2


create_new_list('hola mundo 2.txt', read_text('hola mundo.txt'))
print(shows_new_doc('hola mundo 2.txt'))

"""
EJERCICIO 2

"""
print("\n***********EJERCICIO 2*************")
def obtain_doc(path):
    counter = 0
    with open(path,'r', encoding='utf-8') as file:
        text =  file.readlines()
        for line in (text):
            word = line.split()
            counter = counter + len(word)
    return counter


print(f'Este archivo tiene {obtain_doc('random.txt')} palabras' )

"""
EJERCICIO 3

"""
print("\n***********EJERCICIO 3*************")
def obtaining_the_text(path):
    with open(path,'r', encoding='utf-8') as file:
        document = file.readlines()
        return document


def capitalize(text):
    with open('mayusculas.txt','w',encoding='utf-8') as file:
        for line in (text):
            file.write(line.upper())


def obtain_upper_cases(path):
    with open(path,'r', encoding='utf-8') as file:
        new_doc = file.read()
    return new_doc


text = obtaining_the_text('random.txt')
capitalize(text)
print(obtain_upper_cases('mayusculas.txt'))

"""
EJERCICIO 4

"""
print("\n***********EJERCICIO 4*************")
def obtain_user_text():
    flag = False
    while flag == False:
        user_text = input("Ingrese una linea de texto: ")
        if user_text == "":
            print("no ingresó una cadena de texto, por favor intente de nuevo: ")
        else: 
            flag = True    
            print(user_text)
            return user_text
    

def adding_line(path, text):
    with open(path,'a',encoding='utf-8') as file:
        file.write(f'\n {text}')    


def obtain_new_text(path):
    with open(path,'r',encoding='utf-8') as file:
        new_text = file.read()
        return new_text


adding_line('random.txt',obtain_user_text())    
print(obtain_new_text('random.txt'))