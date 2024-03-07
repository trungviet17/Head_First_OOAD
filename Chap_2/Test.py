from DogDoor import DogDoor
from Remote import Remote


class DogDoorSimulator: 

    def __init__(self): 
        self.door = DogDoor()
        self.remote = Remote(self.door)

    def run(self): 
        print("Fido barks to go outside...")
        self.remote.pressButton()

        print("\n Fido has gone outside ")
        self.remote.pressButton()

        print("\n Fido's all done.....")
        self.remote.pressButton()

        print("\n Fido's back inside..")
        self.remote.pressButton()


if __name__ == '__main__': 
    
    test = DogDoorSimulator()

    test.run()