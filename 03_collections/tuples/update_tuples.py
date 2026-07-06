"""
Tuples are immutable but there is a workaround for this problem.
Convert thr tuple into a list, update it and then convert it back to a tuple.
"""

x = ("apple", "banana", "cherry")
print(x)
y = list(x)
y[1] = "orange"
x = tuple(y)
print(y)

"""
To add an item to a tuple, you can either:
1. Convert it to a list, add the item, and then convert it back to a tuple.
"""

numbers = (1, 2, 3)
y = list(numbers)
y.append(4)
numbers = tuple(y)
print(numbers)

"""
2. Or add a tuple to a tuple
"""

num = (1, 2, 3)
y = (4, 5, 6)
num += y
print(num)

"""Tuples are immutable. 
So, removing items or deleting them uses the same workaround.
"""

a = (1, 2, 3)
print(a)
b = list(a)
print(b)
b.remove(1)
a = tuple(b)
print(a)

"""
You can use the del keyword to delete the tuple completely
"""
