# using the + operator

list1 = [1, 2, 3]
list2 = [4, 5, 6]

list3 = list1 + list2
print(list3)

# using the append() method

for x in list2:
    list1.append(x)

print(list1)

# using the extend() method whose sole purpose is to add items of one list to another list
list1.extend(list2)
print(list1)