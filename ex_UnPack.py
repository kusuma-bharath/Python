def healthcalculator(age, apples_ate, cigs_smoke):
    answer = (100 - age) + (apples_ate * 3.5) - (cigs_smoke * 2)
    print(answer)


bharath_data = [27, 2, 0]

healthcalculator(bharath_data[0], bharath_data[1], bharath_data[2])

# This is called unpacking the arguments
healthcalculator(*bharath_data)
