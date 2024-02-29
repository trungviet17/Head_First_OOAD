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
        

    def add(self, serialNumber: str, price: float, guitarspec: GuitarSpec) : 
        self.inv.addGuitar(serialNumber, price, guitarspec)



if __name__ == "__main__" :
    gui = GuitarSpec(Builder.ANY, 't', Type.ACOUSTIC, Wood.ADIRONDACK, Wood.COCOBOLO, 13)
    test = FindGuitarTester()

    test.add('1', 20.0, gui)
    test.find(gui)