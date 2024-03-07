'''
- Class tương tác với hardware của cửa
'''

class DogDoor: 
    def __init__(self) : 
        self.open = False 

    def open(self): 
        print("The dog door opens")
        self.open = True 
    
    def close(self): 
        print("The dog door closes")
        self.open = False 

    def isOpen(self): 
        return self.open