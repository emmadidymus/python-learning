"""
The global keyword can also be used to change the global variable inside the function.
"""

x = "fantastic"

def my_function():
    global x
    x = "awesome"

my_function()

print("Python is " + x)