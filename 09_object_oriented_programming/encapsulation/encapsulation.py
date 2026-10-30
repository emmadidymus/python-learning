class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age # Private property

    """
    Private properties cannot be accessed directly from outside the class.
    To do so we need to create a getter method in the class.
    """
    def get_age(self):
        return self.__age

    """
    To set a private property value, we need to use a setter method in the class.
    """

    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Age must be positive!")

p1 = Person("John", 34)
print(p1.name)
print(p1.get_age()) # Accessing the age from outside the class after setting up a getter method.

p1.set_age(6) # setting up the age as 26 after defining a setter method in the class
print(p1.get_age())




