# Using the add() method

fruits = {'apple', 'banana', 'orange'}
print(fruits)

fruits.add('cherry')
print(fruits)

# Using the update() method to add items from another set
set1 = {'apple', 'banana', 'cherry'}
set2 = {'orange', 'kiwi', 'peach'}
set1.update(set2)
print(set1)

# You can also use the update() method to add any iterable.
set = {1, 2, 3}
list = [4, 5, 6]
set.update(list)
print(set)