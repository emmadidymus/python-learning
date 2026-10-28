"""
the __contains__() method controls what the in operator checks for your operators.
"""

class Company:
    def __init__(self, employees):
        self.employees = employees

    def __contains__(self, name):
        return name in self.employees

e1 = Company(["Tobias", "Jeremy", "Des"])
print("Tobias" in e1)