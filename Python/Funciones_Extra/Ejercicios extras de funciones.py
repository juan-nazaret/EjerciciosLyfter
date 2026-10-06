"""
EJERCICIO 1

"""
def character_count(word, character):
    count = 0
    for i in range(len(word)):
        if word[i].lower() == character.lower():
            count += 1 
    print(f"EJERCICIO 1: Se han encontrado {count} veces el character ")


word = input("ingrese la palabra: ")
character =  input("ingrese el caracter que desea buscar: ")
character_count(word,character)

"""
EJERCICIO 2

"""
def filtering_words(words_list, number_of_characters):
    new_words_list = []
    for i in range(len(words_list)):
        if len(words_list[i]) > number_of_characters:
            new_words_list.append(words_list[i])
    print(f"EJERCICIO 2: {new_words_list}")


filtering_words(["avion","doscientos","cafe","comal"], 4)

"""
EJERCICIO 3

"""
def filtering_vowels(the_string):
    counter = 0
    for i in range(len(the_string)):
        if the_string[i].lower() in "aeiou":
            counter += 1
    print(f"EJERCICIO 3: {counter}")


filtering_vowels("holA mundo")