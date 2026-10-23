# __str__() controls what is returned when an object is printed

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"His name is {self.name} and he is {self.age} years old!"

person1 = Person("Tobias", 34)
print(person1)