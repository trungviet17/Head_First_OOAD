
class Guitar: 

    def __init__(self, serialNumber: str, price: float, builder: str, model: str, type: str, 
                 backwood: str, topwood: str) : 
        self.serialNumber = serialNumber
        self.price = price
        self.builder = builder
        self.model = model
        self.type = type
        self.backwood = backwood 
        self.topwood = topwood 

    def get_Serial_Number(self): return self.serialNumber
    def get_price(self): return self.price 
    def set_price(self, price: float): 
        self.price = price 

    def get_Builder(self): return self.builder 

    def get_Model(self): return self.model

    def get_type(self): return self.type 
    def get_back_wood(self): return self.backwood 
    def get_top_wood(self): return self.topwood


    def information (self) : 
        return {'Serial Number': self.get_Serial_Number(), 'Price': self.get_price(), 
                'Builder' : self.get_Builder(), 'Model' : self.get_Model(), 'Type' : self.get_type(),
                'Back Wood' : self.get_back_wood(), 'Top Wood'  : self.get_top_wood()}