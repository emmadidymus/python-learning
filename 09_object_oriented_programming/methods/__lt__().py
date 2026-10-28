"""
the __lt__() method controls what the less than operator (<) does for your objects
"""

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __lt__(self, other):
        return self.age < other.age

p1 = Person("Paul", 23)
p2 = Person("Gilly", 45)

print(p1>p2)


"""
Python also uses __lt__() to sort objects using functions like sorted()
"""

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __lt__(self, other):
        return self.age < other.age

    def __repr__(self):
        return f"Person(Name={self.name}, Age = {self.age})"

p1 = Person("Paul", 23)
p2 = Person("Gilly", 45)
p3 = Person("Julian", 32)
p4 = Person("Gotham", 23)
p5 = Person("Nairobi", 34)

x = sorted([p1, p2, p3, p4, p5])
print(x)
print([(person.name, person.age) for person in x])
