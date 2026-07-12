car = {"brand": "Ford",
       "model": "Mustang",
       "year": 2010
       }

print(car)

"""
You can use pop() with a specified key name
"""
car.pop("model")
print(car)

"""
You can use popitem() that removes the last inserted item
"""
car.popitem()
print(car)

"""
You can also use the del keyword that removes the item with a specified key name
"""
del car["brand"]
print(car)


"""
The del keyword can also be used to delete the dictionary completely. eg. del car
"""

student = {
    "name": "George",
    "age": 20,
    "stream":"A"
}
#del student
print(student)


"""
The clear() method can be used to clear the dictionary
"""

student.clear()
print(student)

