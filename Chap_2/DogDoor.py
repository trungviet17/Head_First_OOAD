'''
- Class tương tác với hardware của cửa
'''

class DogDoor: 
    def __init__(self) : 
        self.state = False 

    def open(self): 
        print("The dog door opens")
        self.state = True 
    
    def close(self): 
        print("The dog door closes")
        self.state = False 

    def isOpen(self): 
        return self.state