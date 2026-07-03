# To change the value of a specific item, refer to the index number.

thisList = ["apple", "banana", "cherry"]
thisList[0] = "blackcurrant"
print(thisList)

#To change a range of item values
this_list = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
this_list[2:4] = ["blackcurrant", "watermelon"]
print(this_list)

# Inserting items using the insert() method.
thisList.insert(3, "pear")
print(thisList)