"""
__repr__() magic method is used to control the representation of an object on the developer's side.
It facilitates debugging and inspection of the object.
"""

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}({self.age})"

    def __repr__(self):
        return f"Person(name = {self.name!r}, age = {self.age})"

p1 = Person("Tobias", 34)
print(p1)
print(repr(p1))