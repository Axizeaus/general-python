def deco(f):
    f.attr = 'decorated' 
    return f

@deco
def f() : pass 

print(f)
print(f.attr)

def deco1(f):
    print('deco1 called')
    return f
    
def deco2(f):
    print('deco2 called')
    return f
    
def deco3(f):
    print('deco3 called')
    return f

@deco1
@deco2
@deco3
def func(): print('function called')

func()

print('-' * 3)

def required_int(func):
    print('required int is called')
    def wrapper(args):
        print('wrapper is called')
        assert isinstance(args, int)
        return func(args)
    return wrapper

@required_int 
def p1(arg):
    print(arg)
    
@required_int
def p2(arg):
    print(arg)
    
p1(123)
p2(456.0)