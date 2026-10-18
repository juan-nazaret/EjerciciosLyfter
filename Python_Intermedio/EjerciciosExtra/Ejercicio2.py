class Animal():
    def __init__(self,name):
        self.name = name

    def speak(self):
        return 'hace un sonido'
    
    
class Dog(Animal):

    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        return 'guau'


class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        return 'miau'


dog = Dog('mica')
print(dog.speak())

cat = Cat('mini')
print(cat.speak())