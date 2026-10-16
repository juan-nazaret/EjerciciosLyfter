class Bus:
    max_passengers = 5
    passengers = []

    def add_passenger(self):
        if len(self.passengers) < self.max_passengers:
            person = register_passenger()
            self.passengers.append(person)
            print('pasajero agregado')
            print(f'nombre del pasajero: {person.name}')
            print(f'edad del pasajero: {person.age}')
        else: 
            print('\n**** El bus esta lleno, no se admiten más pasajeros ***')
            


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


def register_passenger():
        while True:
            name = input('Ingrese el nombre del pasajero: ')
            if any(char.isdigit() for char in name) == True:
                print('El nombre no puede contener números, intenta de nuevo\n')
            else: 
                break

        while True:
            try: 
                age = int(input('ingrese la edad del pasajero: '))
                if age >= 0 and age <= 100:
                    break
                else:
                    print('La edad solo puede sr un número entero entre 0 y 100')
            except ValueError as ex:
                print('La edad debe estar expresada en numero enteros, intenta de nuevo\n ')    

        person1 = Person(name,age)
        return person1



def menu():
    while True:
        print("MENU\n" \
        "1.- Subir pasajero\n" \
        "2.- Salir")

        user_selection1 = user_selection()
        if user_selection1 in [1,2]:
            match user_selection1:
                case 1:
                    bus1.add_passenger()
                case 2: 
                    print('*** FIN ***')
                    exit()
        else: 
            print('Opción invalida, intente de nuevo')
            

def user_selection():
    while True:
        user_selection = int(input('Ingrese su opción: '))
        if user_selection in [1,2]:
            return user_selection
        else:
            print('opción inválida, intente de nuevo')

bus1 = Bus()
menu()