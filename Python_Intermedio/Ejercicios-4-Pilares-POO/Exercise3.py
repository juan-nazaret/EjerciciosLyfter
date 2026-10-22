from abc import ABC, abstractmethod

class SamsungDevice(ABC):
    def __init__(self,rom, ram, samsung_account):
        self.rom = rom
        self.ram = ram
        self.samsung_account = samsung_account

    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass

class Tablet(ABC):
    def __init__(self, s_pen):
        self.s_pen = s_pen

    
class samsung_tab_s10(SamsungDevice, Tablet):
    def __init__(self, rom, ram, samsung_account,s_pen):
        SamsungDevice.__init__(self,rom, ram, samsung_account) 
        Tablet.__init__(self,s_pen)

    def turn_on(self):
        return 'encendido'
            

    def turn_off(self):
        return 'apagado'


tablet1 = samsung_tab_s10(5,5,546216,'yes')
print(f'rom: {tablet1.rom}, ram:{tablet1.ram}, samsung account: {tablet1.samsung_account}, tiene s-pen: {tablet1.s_pen} ')