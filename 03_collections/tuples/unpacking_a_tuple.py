"""
When crating a tuple we normally assign values to it,
this is called packing a tuple.
"""

fruits = ("apple", "banana", "cherry")

""" 
But in python, we are allowed to extract the variable back into variables.
This is called unpacking a tuple.
"""

green, yellow, red = fruits
print(green, yellow, red)

"""
The number of variables must match the numbers of values.
Otherwise, you must use an asterisk * to collect the remaining values into a list
"""
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green, yellow, red)
