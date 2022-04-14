from pprint import pprint

li = list('012345')
print(li)

com_list = [int(i) for i in li]
print(com_list)

com_list.append([i for i in range(100)])
print(com_list)

crazy_list = [(i, j, k) for i in range(10) for j in range(10,20) for k in range(20,30)]
pprint(crazy_list)