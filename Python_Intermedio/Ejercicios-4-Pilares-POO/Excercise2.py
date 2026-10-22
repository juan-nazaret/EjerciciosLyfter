from abc import ABC, abstractmethod

class   Shape(ABC):

    @abstractmethod
    def calculate_perimeter(self):
        pass


    @abstractmethod
    def calculate_area(self):
        pass

class Circle(Shape):
    pi = 3.1416
    def __init__(self,radius):
        self.radius = radius

    def calculate_area(self):
        area = self.pi * (self.radius* self.radius)
        print(f'\narea del circulo: {area}')

    def calculate_perimeter(self):
        perimeter = (self.radius *2) * self.pi
        print(f'perímetro del circulo: {perimeter}')

class Square(Shape):
    def __init__(self, side):
        self.side= side

    def calculate_area(self):
        area = self.side * self.side
        print(f'\nel area del cuadrado es: {area}')

    def calculate_perimeter(self):
        Perimeter = (self.side * 4 ) 
        print(f'el perímetro del cuadrado es {Perimeter}')


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        area = self.width * self.height
        print(f'\nel área del rectángulo es {area}')

    def calculate_perimeter(self):
        perimeter = (self.width * 2) + (self.height * 2)
        print(f'el perímetro del rectángulo es {perimeter}')

circle =  Circle(3)
circle.calculate_area()
circle.calculate_perimeter()


rectangle = Rectangle(5,9)
rectangle.calculate_area()
rectangle.calculate_perimeter()


square = Square(7.9)
square.calculate_area()
square.calculate_perimeter()