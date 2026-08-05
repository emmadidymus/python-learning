"""
You can use multiple decorators on one function.

This is done by placing the decorator calls on top of each other.

Decorators are called in the reverse order, starting with the one closest to the function.

"""

def uppercase(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs).upper()
    return wrapper

def add_greeting(func):
    def wrapper(*args, **kwargs):
        return f"Hello {func()}. Have a great day!"
    return wrapper

@uppercase
@add_greeting
def say_hello():
    return "Linus"
print(say_hello())