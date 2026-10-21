#EJERCICIO EXTRA 1

class Rectangle:
    def __init__(self,width, height):
        
        if width < 0  or height < 0:
            raise ValueError("No puede haber números negativos") 
        else:
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
        try:
            width = int(input('\nIngrese el ancho del rectángulo: '))
        except ValueError as ex:
            print('\n!numero invalido intenta de nuevo')
            continue
        try:
            height = int(input('Ingrese la altura del rectángulo: '))
        except ValueError as ex:
            print('\n!numero invalido intenta de nuevo')
            continue
        try:
            rectangle = Rectangle(width,height)
            return rectangle
        except ValueError as ex:
            print('\n!! No puede haber números negativos en los valores de la figura \n ')

rectangle = create_rectangle()
print(f'Area del rectángulo: {rectangle.get_area()}')
print(f'El perímetro del rectángulo es: {rectangle.get_perimeter()}')
