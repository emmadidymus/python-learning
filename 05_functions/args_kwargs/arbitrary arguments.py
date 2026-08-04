"""
If you do not know how many arguments will be passed to your function, add a * before the parameter name.
This way a function will receive a tuple of arguments, and will access the items accordingly.
"""

def my_function(*names):
    print(f"The youngest kid is {names[2]}")

my_function("Emily", "Ken", "Jon", "Dave", "Moses")