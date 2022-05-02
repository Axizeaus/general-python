def get_square_gen(n):
    for x in range(n):
        yield x ** 2
        
s = get_square_gen(3)
print(s.__next__())
print(next(s))
print(s.__next__())
# print(s.__next__())
print("=" * 10)
# trying out send

def counter(start=0):
    n = start
    while True:
        yield n 
        n += 1
c = counter()
print(next(c))
print(next(c))
print(next(c))
# while True:
#     num = next(c)
#     print(num)
#     if num == 1000:
#         break