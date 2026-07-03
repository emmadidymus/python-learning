# Using append to add list items

thisList = ["Apple", "Banana", "Cherry"]
thisList.append('orange')
print(thisList)

# to append items from another list use the extend() method
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

# the extend() method can be used to append any other collection 