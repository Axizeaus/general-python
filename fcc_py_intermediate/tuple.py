import sys

from timeit import timeit

li = [i for i in range(10)]
tup = tuple(li)
print(tup)
li = list(tup)
i1, *i2, i3 = tup
print(i1)
print(i2)
print(i3)

print(sys.getsizeof(tup), 'bytes')
print(sys.getsizeof(li), 'bytes')

# using tuple is more efficient than using list (memory wise)

print(timeit(stmt='[1, 2, 3, 4, 5, 6, 7, 8]', number=100000))
print(timeit(stmt='(1, 2, 3, 4, 5, 6, 7, 8)', number=100000))
