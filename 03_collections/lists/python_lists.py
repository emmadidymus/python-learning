"""
python lists are ordered, mutable, and allow duplicates.
"""

# List items are indexed, so you can access them by referring to the index number.
this_list = ["apple", "banana", "cherry"]
print(this_list[2])

# range of indexes
thisList = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thisList[2:5])

# Check if item is in the list

if "apple" in thisList:
    print("apple is in the list")