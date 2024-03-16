
"""
- Remote control to operate the dog door
"""
import time 

from DogDoor import DogDoor

class Remote: 
    def __init__(self, door: DogDoor): 
        self._door = door

    def pressButton(self): 
        print("Pressing the remote control button.....")
        if self._door.isOpen(): 
            self._door.close()
        else : 
            self._door.open()

        

        