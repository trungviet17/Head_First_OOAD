from DogDoor import DogDoor
from Remote import Remote
import time

class DogDoorSimulator: 

    def __init__(self): 
        self.door = DogDoor()
        self.remote = Remote(self.door)

    def run(self): 
        print("Fido barks to go outside...")
        self.remote.pressButton()

        print("\n Fido has gone outside ")
    
        time.sleep(5)
        print("\n Close the door")
        print("\n ... Fido stuck outside")
        print("\n Gina grabs the remote control")
        self.remote.pressButton()


if __name__ == '__main__': 
    
    test = DogDoorSimulator()

    test.run()