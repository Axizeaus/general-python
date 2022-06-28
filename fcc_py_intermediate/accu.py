from itertools import accumulate
import operator 

a = [1,2,3,4]
acu = accumulate(a, func=max)
print(a)
print(list(acu))