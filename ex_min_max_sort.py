stock = {
    'b': 10,
    'a': 44,
    'c': 34,
    'd': 56,
    'e': 65
}

print(min(zip(stock.values(), stock.keys())))

print(max(zip(stock.values(), stock.keys())))

print(sorted(zip(stock.values(), stock.keys())))
