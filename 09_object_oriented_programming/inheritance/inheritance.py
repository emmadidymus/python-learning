"""
Creating a parent class
"""


class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def printname(self):
        print(self.firstname, self.lastname)


x = Person("John", "Doe")
x.printname()

"""
Creating the child class
"""

class Student(Person):
    def __init__(self, firstname, lastname, year): # Creating the child's class own __init__ function. This can override the parent class init function
        Person.__init__(self, firstname,lastname) # This keeps the parent class __init__ function that was previously overridden
        super().__init__(firstname, lastname) # You can also use the super method instead of the class name to inherit everything.
        self.year = year

    def welcome(self):
        print(f"Welcome {self.firstname} {self.lastname} to the class of {self.year}")

x = Student("Jane", "Doe", 2019)
x.welcome()

