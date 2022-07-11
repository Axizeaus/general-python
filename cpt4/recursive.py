# N!

# 5! = 1*2*3*4*5 = (1*2*3*4) * 5 = 4! * 5

def fac(n):
    if n in (0,1):
        return 1
    return fac(n - 1) * n

print(fac(5))

from math import factorial

print(factorial(5))