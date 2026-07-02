"""
If you create a variable with the same name inside a function,
this variable will be local, and can only be used inside that function.
The global variable with the same will remain as it was, global and with its original value.
"""

x = "fantastic"

def my_function():
    x = "awesome"
    print("Python is " + x)

my_function()

print("Python is " + x)