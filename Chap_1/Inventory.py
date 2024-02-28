from Category import *
from Guitar import Guitar
class Inventory: 
    def __init__(self) -> None:
        self.guitars = []

    def addGuitar(self, serialNumber: str, price: float, builder: Builder, model: str, type: Type, 
                 backwood: Wood, topwood: Wood) : 
        guitar = Guitar(serialNumber,price, builder, model, type, backwood, topwood)
        self.guitars.append(guitar)

    def get_Guitar(self, name: str): 
        for i in self.guitars: 
            if name == i.get_Serial_Number() : return i 

        return None 
    
    def search(self, guitar: Guitar): 
        for i in self.guitars : 
            if guitar.get_Builder() != i.get_Builder() : continue
            t = guitar.get_Model().lower()
            t_2 = i.get_Model().lower()
            if t != t_2 : continue
            if guitar.get_back_wood() != i.get_back_wood() : continue 
            if guitar.get_price() != i.get_price() : continue
            if guitar.get_Serial_Number() != i.get_Serial_Number(): continue
            if guitar.get_type() != i.get_type(): continue
            if guitar.get_top_wood() != i.get_top_wood(): continue
            return True

        return False
    


