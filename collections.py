from collections import Counter

a = 'aaaaaabbbbbbbbcc'
my_counter = Counter(a)
print(my_counter)
print(my_counter.items())
print(my_counter.elements())
print(my_counter.most_common())


for i in my_counter.elements():
    print(i)

x = 'bbbaaa'
test = Counter(x)
print(test.most_common(1))
