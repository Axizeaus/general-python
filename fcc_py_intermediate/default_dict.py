from collections import defaultdict

dd = defaultdict(int)
dd['a'] = 1
dd['b'] = 2
print(dd['c'])
print(dd)

d = dict()
d['a'] = 10
d['b'] = 20
print(d)
try:
    print(d['c'])
except KeyError:
    print('There is key error')
finally:
    print('as expected')
