from collections import deque

deq = deque()
deq.append(1234)
deq.appendleft('678')
print(deq)
print(deq.pop())
print(deq.popleft())
deq.clear()
print(deq)

for i in range(5):
    deq.append(i)
    for i in range(5,10):
        deq.appendleft(i)
    print(deq)
    
deq.popleft()
print(deq)
deq.clear()

for i in range(5):
    if i % 2 == 0: 
        deq.appendleft(i)
    else: 
        deq.append(i)
    print(deq)
    
deq.extend([1,2,3])
print(deq)
deq.extendleft([1,2,3])
print(deq)

# rotate -> takes the specified number of indexes from the right and append that to the left
deq.rotate(2)
print(deq)

deq.rotate(-2)
print(deq)