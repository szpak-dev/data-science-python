import pprint

alphabet = tuple('abcdefghijklmnopqrstuvwxyz')
dictionary = {}

for i, letter in enumerate(alphabet):
    dictionary[letter] = [letter] * i


pprint.pprint(dictionary)

# One-liner variant
# dictionary = {letter: [letter] * i for i, letter in enumerate(alphabet)}
# print(dictionary)
