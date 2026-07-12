"""
You can change the value of a specific dictionary item by referring to its key.
"""

car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(car)

car["model"] = "Ranger"
print(car)


"""
You can also use the update() method
"""

car.update({"year": 2010})
print(car)
