def dating_age_limit(your_age):
    girls_age = your_age/2 + 7
    return girls_age


bharath_limit = dating_age_limit(27)
random_limit = dating_age_limit(47)

print("bharath dating age limit is",bharath_limit,"or older")
print("random person's dating age limit is",random_limit,"or older")