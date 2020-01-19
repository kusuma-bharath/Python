from collections import Counter

text = 'Hi, this is a sample text. It has lot of words repeating. hopefully some words will be repeated. It implements word counter also. words are so important in this. 4 4 4 4 4 . 5 5 5'

words = text.split()

print(words)

counter = Counter(words)

top_three = counter.most_common(4)

print(top_three)