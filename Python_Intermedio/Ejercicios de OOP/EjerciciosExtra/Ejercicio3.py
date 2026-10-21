#EJERCICIO EXTRA 3

class Product:
    def __init__(self, name, price,stock):
        self.name = name
        self.price = price
        self.stock = stock


class Inventory:
    def __init__(self):
        self.products_list = []

    def add_a_product(self,product):
        self.products_list.append(product)
        print('Producto agregado con éxito!*\n')

    def show_all_products(self):
        for number,product in enumerate(self.products_list,start=1):
            print(f'\n{number}.- nombre: {product.name}, precio: ${product.price}, cantidad: {product.stock}')

    def calculate_inventory(self):
        total_value = 0
        for product in self.products_list:
            total_per_product = product.price * product.stock
            total_value += total_per_product
        return total_value



def create_inventory():
    inventory = Inventory()
    while   True:
        product_name = input('\ningrese el nombre del producto: ')
        if product_name == "":
            print('el nombre no puede estar vacío, intenta de nuevo\n')
            continue
        product_price = verify_int('precio')
        stock = verify_int('stock')
        product_object = Product(product_name,product_price,stock)
        inventory.add_a_product(product_object)
        user_answer = user_answer1()
        if user_answer == False:
            print('El total de productos es: ')
            inventory.show_all_products()
            print(f'\ntotal de valor del inventario: ${inventory.calculate_inventory()}')
            exit()


def user_answer1():
    while True:
        user_answer = input('Quiere agregar otro producto? (si/no): ').lower()
        if user_answer in ['si','no']:
            if user_answer == 'no':
                return False
            else: 
                return True
        else:
            print('opción inválida, intenta de nuevo\n') 
            


def verify_int(message):
    while True:
        try:
            number_int = int(input(f'agregue el {message} del producto: '))
            if number_int < 0:
                print('El precio no puede ser negativo ***')
                continue
            else:
                return number_int
        except ValueError as ex:
            print('\ndato invalido, intenta de nuevo')


create_inventory()