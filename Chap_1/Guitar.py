
from Category import Builder, Type, Wood

class GuitarSpec: 
    def __init__(self, builer: Builder, model: str, type: Type,
                 backwood: Wood, topwood: Wood, numString: int):

        self._builder = builer
        self._model = model
        self._type = type
        self._backwood = backwood
        self._topwood = topwood
        self._numString = numString

    def get_Builder(self): return self._builder

    def get_Model(self): return self._model

    def get_Type(self): return self._type 

    def get_BackWood(self): return self._backwood

    def get_TopWood(self): return self._topwood 
    
    def get_NumString(self) : return self._numString

    def get_Spec(self): 
        return {'Builder' : self.get_Builder(), 'Model' : self.get_Model(), 'Type' : self.get_Type(),
                'Back Wood' : self.get_BackWood(), 'Top Wood'  : self.get_TopWood(), 'NumString' : self.get_NumString()}
    
    def __eq__(self, __value: object) -> bool:
            if self.get_Builder() != __value.get_Builder() :return False
            
            m1 = self.get_Model().lower()
            m2 = __value.get_Model().lower()
            if m1 != m2 :return False
            if self.get_BackWood() != __value.get_BackWood() : return False
            
            
            if self.get_Type() != __value.get_Type():return False
            if self.get_TopWood() != __value.get_TopWood():return False
            if self.get_NumString() != __value.get_NumString() : return False

            return True

class Guitar: 

    def __init__(self, serialNumber: str, price: float, guitarspec: GuitarSpec) : 
        self.serialNumber = serialNumber
        self.price = price
        self.guitarspec = guitarspec

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

    