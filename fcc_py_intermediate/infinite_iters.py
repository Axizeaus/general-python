from itertools import count, cycle, repeat

for i in count(10):
    print(i)
    if i == 100:
        break
    
ls = [2,4,5] 
# for i in cycle(ls):
#     print(i)

for i in repeat(1, 10000):
    print(i)