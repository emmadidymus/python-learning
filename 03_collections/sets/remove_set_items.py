"""
You can use the remove() or discard() methods to remove items.
"""

set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
set.remove(1)
print(set)

set.discard(3)
print(set)

"""
The clear() method empties the set and the del keyword deletes the set completely
"""
set.clear()
print(set)

#del set