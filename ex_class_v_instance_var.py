class Girl:
    Gender = 'female'
    def __init__(self,name):
        self.name = name
        print("Craeted object with name: " + name)

r = Girl("Appu")
s = Girl("Reena")
print(r.Gender)
print(s.Gender)

print(r.name)
print(s.name)