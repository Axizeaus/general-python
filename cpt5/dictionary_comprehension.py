from string import ascii_lowercase
from pprint import pprint

print([i for i in enumerate(ascii_lowercase)])
letter_map = {c:k for k, c in enumerate(ascii_lowercase, 1)}
pprint(letter_map)

word = 'Hello' 
swaps = {c: c.swapcase() for c in word}
print(swaps)
print(word.swapcase())

positions = {c: k for k, c in enumerate(word)}
print(positions)