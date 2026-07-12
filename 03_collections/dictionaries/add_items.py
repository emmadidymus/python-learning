"""
You can add items to dictionaries by using a new key and assigning a value to it
"""

car = {"brand": "Ford",
       "year": 2010
       }
print(car)

car["model"] = "Mustang"
print(car)

"""
You can also use the update() keyword
"""

car.update({"color": "pearl"})
print(car)