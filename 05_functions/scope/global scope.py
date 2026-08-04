"""
A variable created outside a function is of a global scope.
It can be used by anyone

"""
x = 5

def my_function():
    print(x)

my_function()

print(x)