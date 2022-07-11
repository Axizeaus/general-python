def print_squares(start, end):
    for n in range(start, end):
        yield n ** 2
        
print(list(print_squares(5, 10)))
for n in print_squares(2, 5):
    print(n)