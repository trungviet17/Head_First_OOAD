
from Category import Builder, Type, Wood


class Guitar: 

    def __init__(self, serialNumber: str, price: float, builder: Builder, model: str, type: Type, 
                 backwood: Wood, topwood: Wood) : 
        self.serialNumber = serialNumber
        self.price = price
        self.guitarspec = GuitarSpec(builer= builder, model= model, type= type, backwood= backwood, topwood= topwood)

    def get_Serial_Number(self): return self.serialNumber
    def get_price(self): return self.price 
    def set_price(self, price: float): 
        self.price = price 

    
    def information (self) : 
        spec = self.guitarspec.get_Spec()
        spec['Serial Number'] = self.get_Serial_Number()
        spec['Price'] = self.get_price()
        return spec

    def get_Spec(self): 
        return self.guitarspec
'''

'''
class GuitarSpec: 
    def __init__(self, builer: Builder, model: str, type: Type,
                 backwood: Wood, topwood: Wood):

        self._builder = builer
        self._model = model
        self._type = type
        self._backwood = backwood
        self._topwood = topwood

    def get_Builder(self): return self._builder

    def get_Model(self): return self._model

    def get_Type(self): return self._type 

    def get_BackWood(self): return self._backwood

    def get_TopWood(self): return self._topwood 
    
    def get_Spec(self): 
        return {'Builder' : self.get_Builder(), 'Model' : self.get_Model(), 'Type' : self.get_Type(),
                'Back Wood' : self.get_BackWood(), 'Top Wood'  : self.get_TopWood()}