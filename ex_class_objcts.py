class Enemy:
    life = 3
    def attach(self):
        self.life -=1
        print("Ouch!!")

    def checklife(self):
        if self.life <=0:
            print("Enemy dead")
        else:
            print(str(self.life)," life's left")


ob1 = Enemy()
ob2 = Enemy()

ob1.checklife()
ob1.attach()
ob1.attach()
ob1.checklife()

ob2.checklife()