class BankAccount:
    def __init__(self,balance):
        self.balance = balance

    def deposit_money(self,amount):
        self.balance += amount
        print(f'Transacción exitosa')
        print(f'\nSaldo actualizado: {self.balance}\n')
        
    def withdraw_money(self):
        pass

class SavingsAccount(BankAccount):
    def __init__(self,balance,min_balance):
        super().__init__(balance)
        self.min_balance = min_balance

    def withdraw_money(self,amount):
            if (self.balance - amount) < self.min_balance:
                raise ValueError ('los fondos no son suficientes\n')
            else:
                self.balance -= amount
                print(f'Transacción exitosa')
                print(f'\nSaldo actualizado: {self.balance}\n')


def main_menu():
    list_of_accounts = []
    while True:
        print('*** Menu ***\n'\
        '1.- Crear una cuenta\n'\
        '2.- Ya tengo una cuenta\n'\
        '3.- Salir')

        user_answer = answer_from_user()
        match user_answer:
            #It creates a new SavingsAccount object and saves it into a list of instances of that class
            case 1:
                min_balance = define_min_balance()
                savings_account = SavingsAccount(0,min_balance)
                list_of_accounts.append(savings_account)
                print('*** Cuenta creada! ***')
                show_accounts_list(list_of_accounts)
            case 2:
                show_accounts_list(list_of_accounts)
                account_selection = choose_account(list_of_accounts)
                account_object = list_of_accounts[account_selection]
                account_menu(account_object)
            case 3:
                print('\nSESSION FINALIZADA')
                exit()


def answer_from_user():
    while True:
        try:
            user_answer = int(input('Elija una opción: '))
            if user_answer not in [1,2,3]:
                print('\nla opción no es válida, intente de nuevo\n') 
            else: 
                return user_answer
        except ValueError as ex:
            print('\nopción inválida, intente de nuevo\n')

def define_min_balance():
    while True:
        try:
            min_balance = float(input('Cual será el balance mínimo?: '))
            return min_balance
        except ValueError as ex:
            print('El balance mínimo debe ser un número, intenta de nuevo')

def account_menu(account_object):
    while True:
        print('*** Account Menu ***\n' \
            '1.- Depositar\n'\
            '2.- Retirar\n'\
            '3.- Volver al menu principal ')
        user_selection = answer_from_user()
        match user_selection:
            case 1:
                print('opción 1 depositar\n--------------------\n')
                amount = validate_int('depositar')
                account_object.deposit_money(amount)
            case 2:
                print('opción 2 retirar\n--------------------\n')
                amount = validate_int('retirar')
                try:
                    account_object.withdraw_money(amount)
                except ValueError as ex:
                    print(ex)
            case 3:
                print('opción 3 regresar al menú principal\n')
                return


    
#shows the accounts list and choose an account to work with
def show_accounts_list(list_of_accounts):
    if len(list_of_accounts) == 0:
        return False
    else:
        print(f'**** Lista de cuentas ***\n')
        for number,account in enumerate(list_of_accounts,start=1):
            print(f'{number}.- balance mínimo: {account.min_balance}')


def choose_account(list_of_accounts):
    while True:
        print(f'len {len(list_of_accounts)}')
        try:
            account_selection = int(input('\nIngrese el número de cuenta con el que desea trabajar: '))
            if account_selection > len(list_of_accounts) or account_selection < 1:
                print('\nOpción inválida, intente de nuevo')
                continue
            else:
                return account_selection - 1 
        except ValueError as ex:
            print('\nLa opción ingresada no es válida, intente de nuevo')


def validate_int(message):
    while True:
        try:
            float_number =  float(input(f'Ingresa la cantidad a {message}: $'))
            if float_number < 0:
                print('La cantidad debe ser un número positivo')
                continue
            else:
                return float_number
        except ValueError as ex:
            print('Debes ingresar un número, intenta de nuevo')

main_menu()