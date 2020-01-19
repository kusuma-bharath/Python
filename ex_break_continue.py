magicnumber = 28

# this is a single line comment

'''
this is for multi line comments
'''

for x in range(101):
    if x == magicnumber:
        print(x, " is the magic number!!")
        break
    else:
        print(x)

# to check divisibility by 4
for y in range(magicnumber + 1):
    if (y % 4 == 0):
        print(y, " is divisible by 4")
    else:
        print(y, " is not divisible by 4")
