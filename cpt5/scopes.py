A = 100 # global name 
print(A)
ex1 = [A for A in range(5)]
print(A)

ex2 = list(A for A in range(5))
print(A)

ex3 = (A for A in range(5))
print(A)

ex4 = {A : 2 * A for A in range(5)}
print(A)

ex5 = {A for A in range(5)}
print(A)

s = 0
for A in range(5): s += A
print(A)

print(globals())
