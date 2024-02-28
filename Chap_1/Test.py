from Inventory import Inventory
from Guitar import Guitar 
from Category import *

class FindGuitarTester : 
    def __init__(self, guitar) :
        self.inv = Inventory()
        self.find_guitar = guitar


    def find(self): 
        result = self.inv.search(self.find_guitar)
        print(2)
        if result == False : return "Not found"
        else : 
            return self.find_guitar.information()
        

    def add(self, serialNumber: str, price: float, builder: Builder, model: str, type: Type, 
                 backwood: Wood, topwood: Wood) : 
        self.inv.addGuitar(serialNumber, price, builder, model, type, 
                 backwood, topwood)



if __name__ == "__main__" :
    gui = Guitar('1', 20.0, Builder.ANY, 't', Type.ACOUSTIC, Wood.ADIRONDACK, Wood.COCOBOLO)
    test = FindGuitarTester(gui)

    test.add('1', 20.0, Builder.ANY, 't', Type.ACOUSTIC, Wood.ADIRONDACK, Wood.COCOBOLO)
    print(test.find())