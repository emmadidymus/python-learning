"""
You cannot normally access set items since sets are not indexed.
But you can use a for loop to loop through set items
"""

x = {"apple", "banana", "cherry"}

for i in x:
    print(i)

# Or use the in and not in membership operators

print("apple" in x)

print("banana" not in x)

"""
Once a set is created, you cannot change its items.
But you can add new ones

"""
