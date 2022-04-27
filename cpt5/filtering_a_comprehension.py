from math import sqrt

mx = 10

triples = [(a,b, sqrt(a**2 + b**2)) 
           for a in range(1, mx) 
           for b in range(a, mx)]

print(triples)

triples = list(
    filter(lambda triple: triple[2].is_integer(), triples)
)

print(triples)

# A Pythagorean triple is a triple (a, b, c) of integer numbers satisfying the equation a2 + b2 = c2.