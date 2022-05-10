from curses.textpad import rectangle


class Rectangle(object):
    def __init__(self, side_a, side_b) -> None:
        self.side_a = side_a
        self.side_b = side_b
        
    def area(self):
        return self.side_a * self.side_b
    
r = Rectangle(2, 4)
print(r.side_a, r.side_b)
print(r.area())
r2 = Rectangle(10,5)
print(r2.side_a, r2.side_b)
print(r2.area())