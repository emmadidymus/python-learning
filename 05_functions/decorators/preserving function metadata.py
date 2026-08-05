"""
Normally, a function's name can be returned with the __name__ attribute:
"""

def myfunc():
    return "Hello World"
print(myfunc.__name__)

"""
But, when a function is decorated, the metadata of the original function is lost.
"""

def changecase(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs).upper()
    return wrapper

@changecase
def say_hello():
    return "Hello World"
print(say_hello.__name__)


"""
To fix this, Python has a built-in function called functools.wraps 
that can be used to preserve the original function's name and docstring.

Import functools.wraps to preserve the original function name and docstring.

"""

import functools

def changecase1(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs).upper()
    return wrapper

@changecase1
def say_hello1():
    return "Hello World"
print(say_hello1.__name__)