class Vehicle:
    def __init__(self, brand,year):
        self._brand = brand
        self._year = year


    @property
    def get_info(self):
        return f'Marca: {self._brand}. Año: {self._year}'

class Car(Vehicle):
    def __init__(self, brand, year, doors, motor):
        super().__init__(brand, year)
        self._doors = doors
        self._motor = motor

    @property
    def get_info(self):
        return (
            'auto --> '
            f'doors: {self._doors}, motor: {self._motor}'
            f'{super().get_info}'
            )
        

class Motorcycle(Vehicle):
    def __init__(self, brand, year, motor, occupants):
        super().__init__(brand, year)
        self._motor = motor
        self._occupants = occupants

    @property
    def get_info(self):
        return (
            'Motocicleta --> '
            f'motor: {self._motor}, occupants: {self._occupants}'
            f'{super().get_info}'
        )

car = Car('Mazda',2011,5,2.5)
print(car.get_info)

moto = Motorcycle('Vento', '2025',190,2)
print(moto.get_info)