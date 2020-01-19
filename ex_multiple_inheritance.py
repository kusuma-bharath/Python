class Mario:
    def move(self):
        print("Mario moves !")

class Shroom:
    def shroom(self):
        print("Mario Shrooms !")

class SuperMario(Mario,Shroom):
    pass

ob = SuperMario()

ob.move()
ob.shroom()
