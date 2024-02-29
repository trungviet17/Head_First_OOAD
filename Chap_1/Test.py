from Inventory import Inventory
from Guitar import Guitar, GuitarSpec
from Category import *

class FindGuitarTester : 
    def __init__(self) :
        self.inv = Inventory()
        


    def find(self, guitaspec: GuitarSpec): 
        result = self.inv.search(guitaspec)
        
        if len(result) == 0 : return "Not found"
        else : 
            for i in result : 
                print(i.information())
        

    def add(self, serialNumber: str, price: float, builder: Builder, model: str, type: Type, 
                 backwood: Wood, topwood: Wood) : 
        self.inv.addGuitar(serialNumber, price, builder, model, type, 
                 backwood, topwood)



if __name__ == "__main__" :
    gui = GuitarSpec(Builder.ANY, 't', Type.ACOUSTIC, Wood.ADIRONDACK, Wood.COCOBOLO)
    test = FindGuitarTester()

    test.add('1', 20.0, Builder.ANY, 't', Type.ACOUSTIC, Wood.ADIRONDACK, Wood.COCOBOLO)
    test.find(gui)