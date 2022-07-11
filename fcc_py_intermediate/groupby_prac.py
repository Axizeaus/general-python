from itertools import groupby

def smaller_than_3(x):
    return x < 3

ls = [1,2,3,4]
group_obj = groupby(ls, key=smaller_than_3)

for k, v in group_obj:
    print(k, list(v)) 
    
group_obj2 = groupby(ls, key=lambda x : x < 2)

for k,v in group_obj2:
    print(k, list(v))