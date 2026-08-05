"""
Sometimes the decorator function has no control over the arguments passed from decorated function,
to solve this problem, add (*args, **kwargs) to the wrapper function,
this way the wrapper function can accept any number, and any type of arguments,
and pass them to the decorated function

"""

def uppercase(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs).upper()
    return wrapper

@uppercase
def say_hello(name):
    return f"Hello {name}"

print(say_hello("Sally"))