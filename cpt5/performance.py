from time import time

mx = 1000 * 4
t = time()
floop = list()
for a in range(1, mx):
    for b in range(a, mx):
        floop.append((a,b))
        
print('for loop :{:.4f} s'.format(time() - t))

d = time() 
ls_compr = [
    divmod(a, b) for a in range(1, mx) for b in range(a, mx)
]
print('list comprehension :{:.4f} s'.format(time() - d))

d = time()
gener = list(
    (a,b) for a in range(1, mx) for b in range(a, mx)
)

print('gen exp: :{:.4f} s'.format(time() - d))