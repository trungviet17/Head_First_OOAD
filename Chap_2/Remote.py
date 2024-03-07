
"""
- Remote control to operate the dog door
"""

from DogDoor import DogDoor

class Remote: 
    def __init__(self, door: DogDoor): 
        self._door = door

    def pressButton(self): 
        print("Pressing the remote control button.....")
        if self._door.isOpen(): 
            self._door.open()
        else : 
            self._door.close()

        