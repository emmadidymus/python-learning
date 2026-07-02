print(10 > 9) # evaluates to True
print(10 < 9) # evaluates to False
print(10 == 9) # evaluates to False

"""
When you run a condition in an if statement, python returns True or False.
"""

a = 200
b = 33

if a > b:
    print("a > b")
else:
    print("a < b")


"""
You can create a function that returns a boolean value, 
and execute code based on that boolean value returned by the function.
"""

def my_function():
    return True

print(my_function())

if my_function():
    print("YES!")
else:
    print("NO!")