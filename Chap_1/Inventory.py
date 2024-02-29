from Category import *
from typing import List
from Guitar import Guitar, GuitarSpec
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
    
    def search(self, guitarspec: GuitarSpec) -> List[Guitar]:  
        res = []
        for i in self.guitars : 
            # Ignore price and serial number because it's unique
            ispec = i.get_Spec()
            if guitarspec.get_Builder() != ispec.get_Builder() : continue
            

            m1 = guitarspec.get_Model().lower()
            m2 = ispec.get_Model().lower()
            if m1 != m2 : continue
            if guitarspec.get_BackWood() != ispec.get_BackWood() : continue 
            
            
            if guitarspec.get_Type() != ispec.get_Type(): continue
            if guitarspec.get_TopWood() != ispec.get_TopWood(): continue
            res.append(i)

        return res
    


