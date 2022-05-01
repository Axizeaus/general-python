word = "Hello"
l1 = {c for c in word} 
l2 = set(c for c in word)
print(type(l1), type(l2))
print(l1, l2)
print(l1 == l2)