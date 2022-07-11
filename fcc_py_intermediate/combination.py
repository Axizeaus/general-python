from itertools import combinations, combinations_with_replacement

ls = [1,2,3,4]
comb = combinations(ls, 2)

print(list(comb))

comb_with_replacement = combinations_with_replacement(ls, 2)
print(list(comb_with_replacement))