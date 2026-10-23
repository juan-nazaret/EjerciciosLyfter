class Employee:
    def __init__(self, name,salary):
        self._name = name
        if salary < 0:
            raise ValueError('El salario no puede ser negativo\n')
        else: 
            self._salary = salary

    @property
    def my_name(self):
        return self._name

    @my_name.setter
    def my_name(self,name):
        self._name = name

    @my_name.deleter
    def my_name(self):
        del self._name

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self,salary):
        if salary > 0:
            self._salary = salary
        else: 
            raise ValueError('El salario no puede ser un número negativo\n')

    def promote(self, percentage):
        if percentage < 0 :
            raise ValueError('El aumento salarial no puede ser negativo\n')
        else:
            new_salary = self._salary * (percentage / 100)
            self._salary += new_salary
            print(f'El salario actualizado es: {self._salary}')

def salary_raise():
    while True:
        try:
            percentage = float(input(('Ingresa el porcentaje que se aumentara de salario: ')))
            print(f'Aumento de salario {percentage}%')
            return  percentage
        except ValueError as ex:
            print('Dato inválido, intenta de nuevo ')
            

try:
    employee = Employee('juan', 5000)
    print(f'nombre: {employee.my_name}, salario: {employee.salary}')
    percentage = salary_raise()
    employee.promote(percentage)
except ValueError as ex:
    print(ex)







