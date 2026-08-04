"""
You can combine regular arguments, arbitrary arguments, and arbitrary keyword arguments in the following order:

    1. regular argument
    2. arbitrary argument
    3. arbitrary keyword argument

"""

def my_function(title, *args, **kwargs):
    print("Title: ", title)
    print("Args: ", args)
    print("Kwargs: ", kwargs)

my_function("User Info", "Emily", "Jones", age = "50", city = "San Francisco")