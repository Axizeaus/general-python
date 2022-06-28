squares = list()
for n in range(10):
    squares.append( n ** 2 )

print(squares)

squares = list(map(lambda n: n**2, range(10)))
print(squares)

squares = [i ** 2 for i in range(10) ]
print(squares)

sq1 = list(
    map(lambda n : n ** 2, filter(lambda n: not n % 2, range(10)))
)

print(sq1)

sq2 = [ n ** 2 for n in range(10) if not n % 2]
print(sq2)