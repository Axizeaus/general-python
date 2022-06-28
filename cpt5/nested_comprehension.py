items = 'ABCD' 
pairs = list()
for a in range(len(items)):
    for b in range(a, len(items)):
        pairs.append((items[a], items[b]))
        
print(pairs)

pairs2 = [(items[a], items[b]) for a in range(len(items)) for b in range(a, len(items))]
print(pairs2)