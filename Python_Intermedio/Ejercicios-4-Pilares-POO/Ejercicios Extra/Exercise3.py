class Vehicle:
    def __init__(self, brand,year):
        self._brand = brand
        self._year = year


    
    def get_info(self):
        return f'Marca: {self._brand}. Año: {self._year}'

class Car(Vehicle):
    def __init__(self, brand, year, doors):
        super().__init__(brand, year)
        self._doors = doors

    def get_info(self):
        return (
            'auto --> '
            f'doors: {self._doors}'
            f'{super().get_info()}'
            )
        

class Motorcycle(Vehicle):
    def __init__(self, brand, year,type):
        super().__init__(brand, year)
        self._type = type

    def get_info(self):
        return (
            'Motocicleta --> '
            f'tipo: {self._type}'
            f'{super().get_info()}'
        )

car = Car('Mazda',2011,5)
print(car.get_info())

moto = Motorcycle('Vento', 2025,'Deportiva')
print(moto.get_info())