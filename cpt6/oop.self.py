from re import S


class Square(object):
    side = 8
    def area(self):
        return self.side ** 2
    
sq = Square()
print(sq.area())
print(Square.area(sq))
sq.side = 10
print(sq.area())

class TestingSelf(object):
    def say_hello(meh,name):
        print(meh.name, ', hello there')
        
ts = TestingSelf()
ts.name = 'JUUU'
ts.say_hello(ts.name)
