"""
A variable declared outside a function is a global variable.
It can be used both outside and inside any function.
"""

x = "fantastic"

def my_function():
    print("Python is " + x)

my_function()

