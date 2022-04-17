from collections import namedtuple
from collections import deque
from random import randint, random

Point = namedtuple('Point', 'x,y' )
pt = Point(1,-4)
print(pt)
print(pt.x)
print(pt.y)

d = deque()
d.append(1)
d.append(2)
d.appendleft(3)
print(d)
d.pop()
d.popleft()
print(d)
d.clear()
d.extend('12345')
d.extendleft('567')
print(d)
d.rotate(randint(0,10))
print(d)