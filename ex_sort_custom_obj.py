from operator import attrgetter

class User:
    def __init__(self,x,y):
        self.name=x
        self.user_id=y

    def __repr__(self):
        return self.name + " : " + str(self.user_id)


Users = [
    User("bharath",1),
User("kusuma",3),
User("apoorva",2),
User("pandu",4),
User("reena",6),
User("raveena",5)
]

for x in Users:
    print(x)

print("-----------------")


for x in sorted(Users,key=attrgetter('name')):
    print(x)

print("-----------------")

for x in sorted(Users,key=attrgetter('user_id')):
    print(x)

print("-----------------")
