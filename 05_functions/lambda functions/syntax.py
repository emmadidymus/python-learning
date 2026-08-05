"""
A lambda function can take any number of arguments.
But, it can only have one expression.

"""

x = lambda a,b,c: a+b+c
print(x(4, 5,6))



y = lambda a, b: a * b
print(y(4, 5))