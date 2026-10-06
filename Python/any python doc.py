#Agregamos la nota de español
def add_spanish_note():
    while True:
        try:
            spanish_note = int(input('Ingrese la nota de español: '))
            if spanish_note >= 0 and spanish_note <= 100:
                return spanish_note
            else:
                print('La nota debe ser un número entero entre 0 y 100')
        except ValueError as ex:
            print('La nota debe ser un número entero entre 0 y 100')

add_spanish_note()