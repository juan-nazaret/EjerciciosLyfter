#EJERCICIO EXTRA 2

class Animal():
    def __init__(self,name):
        self.name = name

    def speak(self):
        return 'Hace un sonido'
    
    
class Dog(Animal):

    def speak(self):
        return 'Guau'


class Cat(Animal):

    def speak(self):
        return 'Miau'


dog = Dog('mica')
print(dog.speak())

cat = Cat('mini')
print(cat.speak())

