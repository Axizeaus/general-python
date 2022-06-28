from pprint import pprint
from itertools import product

a = [1,2]
b = [3]
pro = product(a,b, repeat=2)

pprint(list(pro))
print(list(pro)) # <- iter exhausted here
for i in pro:
    print(i)