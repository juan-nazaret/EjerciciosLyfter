
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