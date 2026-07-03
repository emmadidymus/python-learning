# using the remove() method

thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)

# remove the specified index using pop()

thislist.pop(1)
print(thislist)

# remove the specified index using the del keyword
thisList = ["apple", "banana", "cherry"]
del thisList[0]
print(thisList)

# the del keyword can also be used to delete the entire list
del thisList
#print(thisList)

# the clear() method empties the list.
thislist.clear()
print(thislist)