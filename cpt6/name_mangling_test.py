class A:
    def __init__(self, sommet) -> None:
        self.sommet = sommet
        
    def oper1(self):
        print('operation 1 :', self.sommet)
        
class B(A):
    def oper2(self, sommet):
        self.sommet = sommet
        print('operation 2:', self.sommet)
        
obj = B(200)
obj.oper1()
obj.oper2(12)
obj.oper1()

print(obj.__dict__.keys())