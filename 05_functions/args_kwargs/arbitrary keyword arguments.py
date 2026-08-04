"""
If you do not know how many keyword arguments will be passed into your function,
add two asterisks ** before your parameter name.
This way your function will receive a dictionary of arguments and can access them accordingly.
"""

def my_function(**kid):
    print(f"His last name is {kid['lname']}")

my_function(fname='Kit', lname='John')