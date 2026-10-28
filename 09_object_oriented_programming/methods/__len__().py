"""
The __len__() magic method controls what the built-in len() function returns for your objects
"""

class Company:
    def __init__(self, employees):
        self.employees = employees

    def __len__(self):
        return len(self.employees)

c1 = Company(["Tobias", "Kelly", "Lou"])
print(len(c1))