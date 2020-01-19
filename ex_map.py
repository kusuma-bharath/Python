income = [10,20,45,89]

def double_income(dollars):
    return dollars*2

new_income = list(map(double_income,income))

print(new_income)