#EJERCICIO EXTRA 3

class Rectangle:
    def __init__(self,width, height):
        self.width = width
        self.height = height

    def get_area(self):
        area = self.width * self.height
        return area

    def get_perimeter(self):
        perimeter = (self.width * 2 ) + (self.height * 2)
        return perimeter


def create_rectangle():
    while True:
        width = int(input('Ingrese el ancho del rectángulo: '))
        height = int(input('Ingrese la altura del rectángulo: '))

        if width < 0 or height < 0:
            print('Los valores no pueden ser negativos, intente de nuevo ')
        else:
            rectangle = Rectangle(width, height)
            return rectangle

rectangle = create_rectangle()
print(f'Area del rectángulo: {rectangle.get_area()}')
print(f'El perímetro del rectángulo es: {rectangle.get_perimeter()}')