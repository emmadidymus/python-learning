"""
You can access items of a dictionary by referring to the key name, inside square brackets.
"""

car = {"brand":"Ford", "model":"Mustang", "year":1964}
print(car)
print(car["model"])

# You can also use the get() method

print(car.get("brand"))

# The keys() method will return a list of all the keys in a dictionary
print(car.keys())

"""
Adding a new item to the original dictionary will update the keys list
"""

car["color"] = "pearl"
print(car)
print(car.keys())

# The values method will return a list of all the values in a dictionary
print(car.values())


"""
The in keyword is used to check if a particular key is present in the dictionary.
"""

if "model" in car:
    print("Yes, 'model' is one of the keys in the dictionary.")