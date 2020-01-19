class Parent:
    def last_name(self):
        print("Kusuma")

class Child(Parent):
    def first_name(self):
        print("Bharath")

#Overriding parent method
    def last_name(self):
        print("Boss")

ob = Child()

ob.first_name()
ob.last_name()