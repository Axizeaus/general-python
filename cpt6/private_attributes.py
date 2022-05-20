class A:
    def __init__(self, factor) -> None:
        self.__factor = factor
        
    def op1(self):
        print('op1 : ', self.__factor)
        
class B(A):
    def op2(self, factor):
        self.__factor = factor
        print('op2 : ', self.__factor)
        
obj = B(100)
obj.op1()
obj.op2(20)
obj.op1()

# name mangling
print(obj.__dict__.keys())