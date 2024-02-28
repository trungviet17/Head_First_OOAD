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
        res = []
        for i in self.guitars : 
            # Ignore price and serial number because it's unique
            if guitar.get_Builder() != i.get_Builder() : continue
            

            m1 = guitar.model.lower()
            m2 = i.model.lower()
            if m1 != m2 : continue
            if guitar.get_back_wood() != i.get_back_wood() : continue 
            
            
            if guitar.get_type() != i.get_type(): continue
            if guitar.get_top_wood() != i.get_top_wood(): continue
            res.append(i)

        return res
    


