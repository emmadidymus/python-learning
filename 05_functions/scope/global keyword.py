"""
If you want to create a global variable, but are stuck inside the local scope,
you can use the global keyword.

"""

def my_function():
    global x
    x = 5
my_function()

print(x)

"""
Also use the global keyword if you want to make changes to the global variable inside a function.
"""

x = 300

def myfunc():
    global x
    x = 200
myfunc()

print(x)