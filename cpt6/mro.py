from pprint import pprint


class A:
    label = 'a'
    
class B(A):
    label = 'b' 
    
class C(B):
    label = 'c'
    
class D(C,B):
    pass

d = D()
print(d.label)
pprint(d.__class__.mro())