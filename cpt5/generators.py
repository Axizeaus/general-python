def get_squares(n):
    return [x ** 2 for x in range(n)]

print(get_squares(10))

def get_squares_gen(n):
    for x in range(n):
        yield x ** 2
        
print(list(get_squares_gen(10)))
print(get_squares_gen(10))

squares = get_squares_gen(4)
print(squares)
print(next(squares))
print(next(squares))
print(next(squares))
print(next(squares))
print(next(squares))
print(next(squares))
print(next(squares))
