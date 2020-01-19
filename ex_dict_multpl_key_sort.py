from operator import itemgetter

users = [
    {'fname':'A', 'lname':'L'},
{'fname':'C', 'lname':'R'},
{'fname':'E', 'lname':'P'},
{'fname':'E', 'lname':'L'},
{'fname':'D', 'lname':'Q'},
{'fname':'B', 'lname':'N'},
{'fname':'B', 'lname':'O'},
{'fname':'B', 'lname':'M'},
]

for x in sorted(users,key=itemgetter('fname')):
    print(x)

######### Better way like Database is ################

print("--------------------------")

for x in sorted(users, key=itemgetter('fname','lname')):
    print(x)
