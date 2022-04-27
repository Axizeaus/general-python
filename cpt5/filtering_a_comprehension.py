from math import sqrt

mx = 10

triples = [(a, b, sqrt(a**2 + b**2))
           for a in range(1, mx)
           for b in range(a, mx)]

print(triples)

print('=' * 10)

triples2 = filter(lambda triple: triple[2].is_integer(), triples)

print(triples2)
print('=' * 10)


triples3 = list(
    filter(lambda triple: triple[2].is_integer(), triples)
)

print(triples3)
print('=' * 10)


triples4 = list(
    map(lambda triple: triple[:2] + (int(triple[2]),), triples)
)

print(triples4)
print('=' * 10)


# A Pythagorean triple is a triple (a, b, c) of integer numbers satisfying the equation a2 + b2 = c2.
