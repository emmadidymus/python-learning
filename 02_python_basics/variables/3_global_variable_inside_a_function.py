"""
The global keyword can be used to create a global variable inside a function.
"""

def my_function():
    global x
    x = "fantastic"

my_function()
print("Python is " + x)