def func(a=list(), b=dict()):
    print(a)
    print(b)
    print('#' * 12)
    a.append(len(a))
    b[len(a)] = len(a)
func()
func(a=[1,2,3], b={'B':1})
func()

# memoization 

# A technique in which partial results are recorded (forming a memo) and then can be re-used later without having to recompute them.

# notice that after adding a random input in the second call, the third call retains the default, and somehow continue from where the first call left off.

# way around that
def func(a=None):
    if a == None:
        a = list()
        # now you get fresh new list or dict or whatever you want