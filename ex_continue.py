numberTaken=[2,7,10,20,22]

print("Here are the numbers available")

for n in range(24):
    if n in numberTaken:
        continue
    print(n)
