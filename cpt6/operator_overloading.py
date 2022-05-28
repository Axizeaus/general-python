class Weird:
    def __init__(self, s) -> None:
        self._s = s
        
    def __len__(self):
        return len(self._s)
    
    def __bool__(self):
        return '42' in self._s
    
weird = Weird("Hello I'm 42 years old")
print(len(weird))
print(bool(weird))
weird2 = Weird("This is neat, isn't it?")
print(len(weird2))
print(bool(weird2))
