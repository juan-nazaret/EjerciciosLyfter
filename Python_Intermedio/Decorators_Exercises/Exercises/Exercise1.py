class Phone:
    def __init__(self,name,market_value,insurance):
        self.name = name
        self.market_value = market_value
        self.insurance = insurance

def insurance_only(func):
    def wrapper(phone, *args):
        print(f'name = {phone.name}, market value = {phone.market_value}, insurance= {phone.insurance} ')
        insurance = func(phone,*args)
        print(insurance)
        return func(phone,*args)
    return wrapper



@insurance_only
def apply_insurance(phone, amount):
    return f'The insurance will pay ${amount} for a {phone.name} '


phone = Phone('S26 ultra',500,True)
print(apply_insurance(phone,400))