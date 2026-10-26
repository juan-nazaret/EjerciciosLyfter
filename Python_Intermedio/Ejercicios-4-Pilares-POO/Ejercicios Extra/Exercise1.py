class Employee:
    def __init__(self, name,salary):
        self._name = name
        self.salary = salary

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,name):
        self._name = name

    @name.deleter
    def name(self):
        del self._name

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self,salary):
        if salary >= 0:
            self._salary = salary
        else: 
            raise ValueError('El salario no puede ser un número negativo\n')

    def promote(self, percentage):
        if percentage < 0 :
            raise ValueError('El aumento salarial no puede ser negativo\n')
        else:
            new_salary = self._salary * (1 + percentage)
            self.salary = new_salary
            return self.salary

def salary_raise():
    while True:
        try:
            percentage = float(input(('Ingresa el porcentaje que se aumentara de salario en decimales (si es 10% ingresa .1): ')))
            print(f'Aumento de salario {percentage}%')
            return  percentage
        except ValueError as ex:
            print('Dato inválido, intenta de nuevo ')
            

try:
    employee = Employee('juan', 1000)
    print(f'nombre: {employee.name}, salario: {employee.salary}')
    percentage = salary_raise()
    employee.promote(percentage)
    print(f'El salario actualizado es: {employee.salary}')
except ValueError as ex:
    print(ex)







