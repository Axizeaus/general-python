def adder(*a):
    return sum(a)

s1 = sum(map(adder, range(100), range(1,101)))
s2 = sum(adder(*n) for n in zip(range(100), range(1,101)))
print(s1)
print(s2)

def moosh(*num):
    return str(num)

print(list(map(moosh, range(5), range(5,10))))
