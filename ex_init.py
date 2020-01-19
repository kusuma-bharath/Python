class Enemy:

    def __init__(self,x):
        self.energy = x
        print("Initialized Enemy with",self.energy,"Energy")

    def checkEnergy(self):
        print("Energy is",self.energy)

jason = Enemy(5)
sarah = Enemy(18)

jason.checkEnergy()
sarah.checkEnergy()