
import heapq

grades = [20,40,21,120,89,71,65]

print("Largest Elements:",heapq.nlargest(3,grades))

print("Smallest Elements:",heapq.nsmallest(3,grades))

stocks = [
    {'t': 'APPLE', 'p': 25},
    {'t': 'BALL', 'p': 12},
    {'t': 'CAT', 'p': 34},
    {'t': 'DOG', 'p': 7},
    {'t': 'EAGLE', 'p': 6}

]

print("Largest values:",heapq.nlargest(3,stocks, key = lambda stocks : stocks['p']))

print("Smallest values:",heapq.nsmallest(2, stocks,key = lambda stocks : stocks['p']))