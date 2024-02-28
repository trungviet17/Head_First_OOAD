from Inventory import Inventory
from Guitar import Guitar 


class FindGuitarTester : 
    def __init__(self, guitar) :
        self.inv = Inventory()
        self.find_guitar = guitar


    def find(self): 
        result = self.inv.search(self.find_guitar)

        if result == None : return "Not found"
        else : 
            return result.information()
        

    def add(self, serialNumber: str, price: float, builder: str, model: str, type: str, 
                 backwood: str, topwood: str) : 
        self.inv.addGuitar(serialNumber, price, builder, model, type, 
                 backwood, topwood)


