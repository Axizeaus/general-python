even = set()
odd = set()
prime = {2,3,5,7}
for i in range(0,10,2):
    even.add(i)
    odd.add(i+1)

print(even)
print(odd)
print(prime)

print(even.union(odd))
print(odd.union(even))
print(even.intersection(odd))
print(even.intersection(prime))
print(even.difference(prime))
print(prime.difference(even))
print(even.symmetric_difference(odd))
print(even.symmetric_difference(prime))

setA = {1,2,3,4,5}
setB = {2,3,4}

if setB.issubset(setA):
    print('yes, set B is a subset of set A')
if setA.issuperset(setB):
    print('yes again')
    
    
if even.isdisjoint(odd):
    print('disjoint it is')
    
# frozen set is to set is tuple is to list.