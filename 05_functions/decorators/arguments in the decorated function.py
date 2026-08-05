"""
Functions that require arguments can also be decorated,
just make sure you pass the arguments to the wrapper function

"""

def uppercase(func):
    def wrapper(x,y):
        return func(x,y).upper()
    return wrapper

@uppercase
def greet(name,name1):
    return f"Hello {name} and {name1}. "

print(greet("Sally", "John"))