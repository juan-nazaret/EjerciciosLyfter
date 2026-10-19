#EJERCICIO EXTRA 3

class Product:
    def __init__(self, name, price,stock):
        self.name = name
        self.price = price
        self.stock = stock


class Inventory:
    def __init__(self):
        self.products_list = []

    def add_a_product(self):
        product_name = input('ingrese el nombre del producto: ')
        product_price = int(input('agregue el precio del producto: '))
        stock = int(input('ingrese el número de piezas: '))
        self.products_list.append(Product(product_name, product_price,stock))

    def show_all_products(self):
        for number,product in enumerate(self.products_list,start=1):
            print(f'\n{number}.- nombre: {product.name}, precio: {product.price}, cantidad: {product.stock}')

    def calculate_inventory(self):
        total_value = 0
        for product in self.products_list:
            total_per_product = product.price * product.stock
            total_value += total_per_product
        return total_value



def create_inventory():
    inventory = Inventory()
    while True:
        inventory.add_a_product() 
        user_answer = input('Quiere agregar otro producto?: ').lower()
        if user_answer in ['si','no']:
            if user_answer == 'no':
                break
    print(f'El total de productos es: ',end="")
    inventory.show_all_products()
    print(f'total de valor del inventario: {inventory.calculate_inventory()}')


create_inventory()