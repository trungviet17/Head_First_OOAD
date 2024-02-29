from Category import *
from typing import List
from Guitar import Guitar, GuitarSpec
class Inventory: 
    def __init__(self) -> None:
        self.guitars = []

    def addGuitar(self, serialNumber: str, price: float, guitarspec: GuitarSpec) : 
        guitar = Guitar(serialNumber,price, guitarspec)
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
            
            if guitarspec.__eq__(ispec):  res.append(i)

        return res
    


