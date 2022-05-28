class OddEven:
    def __init__(self, data) -> None:
        self._data = data
        self.indexes = (list(range(0, len(data), 2)) + list(range(1, len(data), 2)))
        # print(self.indexes)
    def __iter__(self):
        return self
    def __next__(self):
        if self.indexes:
            return self._data[self.indexes.pop(0)]
        raise StopIteration
    
odd_even = OddEven('ThIsIsCoOl')
print(''.join(c for c in odd_even))

odd_even_2 = OddEven('CiAo')
it = iter(odd_even_2)
print(next(it))
print(next(it))
print(it.__next__())
print(next(it))
print(next(it))