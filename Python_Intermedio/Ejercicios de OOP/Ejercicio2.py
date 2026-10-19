class Bus:
    max_passengers = 5
    def __init__(self):
        self.passengers = []

    def add_passenger(self, person):
        if len(self.passengers) < self.max_passengers:
            self.passengers.append(person)
            print('pasajero agregado con éxito')
        else: 
            print('\n**** El bus esta lleno, no se admiten más pasajeros ***')
            
    def delete_passenger(self):
        name = input('Ingrese el nombre del pasajero a bajar: ')
        for index,passenger in enumerate(self.passengers):
            if passenger.name.lower() == name.lower():
                self.passengers.pop(index)
                print('pasajero eliminado con éxito')
                return
        print('\nel pasajero no existe\n')
            
    def print_passengers_list(self):
        if len(self.passengers) == 0:
            print(f'no hay pasajeros')
        else:
            print('\n*** LISTA DE PASAJEROS ***\n')
            for number, passenger in enumerate(self.passengers, start=1):
                print(f'{number}.- nombre:{passenger.name}, edad:{passenger.age}\n')

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
        print("MENU\n"\
        "1.- Subir pasajero\n" \
        "2.- bajar pasajero\n" \
        "3.- mostrar lista de pasajeros\n"
        "4.- Salir")

        user_selection1 = user_selection()
        match user_selection1:
            case 1:
                person = register_passenger()
                bus1.add_passenger(person)
            case 2:
                bus1.delete_passenger()
            case 3:
                bus1.print_passengers_list()
            case 4: 
                print('*** FIN ***')
                exit()

def user_selection():
    
    while True:
        try:
            user_selection = int(input('Ingrese su opción: '))
            if user_selection in [1,2,3,4]:
                return user_selection
            else:
                print('opción inválida, intente de nuevo')
        except ValueError as ex:
            print('opción inválida, intente de nuevo')

bus1 = Bus()
menu()