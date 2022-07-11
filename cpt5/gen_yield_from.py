def print_squares(start, end):
    yield from (n ** 2 for n in range( start, end ))
for n in print_squares(2, 5):
    print(n)
    
def sommet(n):
    yield from (i for i in n.split())
    
print(list(sommet('this is getting ridiculous')))
print(list(sommet('and I like it, lmao')))