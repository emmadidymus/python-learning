"""
The __add__() magic method controls what happens when you use + operator on objects
"""

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __add__(self, other):
        return self.age + other.age


p1 = Person("Tobias", 23)
p2 = Person("Gad", 34)

print(p1 + p2)