stocks = {
    'APPLE': 345,
    'GOOGLE': 145,
    'INTEL': 245,
    'VISA': 445,
    'ADOBE': 645
}

print(min(stocks))

print(min(zip(stocks.values(), stocks.keys())))
