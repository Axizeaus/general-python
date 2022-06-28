class Person:
    def __init__(self, age) -> None:
        self.age = age


class PersonWithAccessors:
    def __init__(self, age) -> None:
        self._age = age

    def get_age(self): return self._age

    def set_age(self, age):
        if 18 <= age <= 100:
            self._age = age
        else:
            raise ValueError('Age must be within 18 and 100')


class PersonPythonic:
    def __init__(self, age) -> None:
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        if 18 <= age <= 100:
            self._age = age
        else:
            raise ValueError('Age must be within 18 and 100')


p1 = Person(36)
p2 = PersonWithAccessors(26)
p3 = PersonPythonic(36)

print(p1.age)
print(p2._age)
print(p3.age)

p1.age = 101
p2.age = 101
p3.age = 101

print(p1.age)
print(p2._age)
print(p3.age)
