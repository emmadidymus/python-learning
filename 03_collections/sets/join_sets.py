"""
join() and update() methods join all items from both sets

The intersection() method keeps only duplicates

The difference() method keeps items from the first set that are not in the other set.

The symmetric_difference() method keeps items from both sets except duplicates

"""

# union(): returns a new set

Set1 = {1, 2, 3, 4, 5, 6, 7, 8, 9}
Set2 = {"a", "b", "c"}
Set3 = Set1 | Set2
print(Set3)

# joining multiple sets

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}
set5 = set1 | set2 | set3 | set4
print(set5)

# joining a set and a tuple
# you can always join a set with other iterables

x = {11, 22, 33, 44, 55}
y = ('aa', 'bb', 'cc', 'dd')
z = x.union(y)
print(z)

# update() inserts all items from one set into another. It does not create a new set

a = {'aaa', 'bbb', 'ccc', 'ddd'}
b = {'eee', 'fff', 'ggg', 'hhh'}
a.update(b)
print(a)

# both union and update will exclude any duplicate items

# intersection() keeps only the duplicates
fruits = {"apple", "banana", "cherry"}
companies = {"google", "microsoft", "apple"}
intersection = fruits & companies
print(intersection)

"""
the intersection_update() method will return only the duplicates
but it will modify an already existing set instead of creating a new one
"""

fruits.intersection_update(companies)
print(fruits)

# difference()

diff = fruits.difference(companies)
print(diff)

"""
difference2 = fruits - companies
print(difference2)
"""


"""
The difference_update() method will keep the items from the first set that are not in the other set, 
but it will change the original set instead of returning a new set.

fruits.difference_update(companies)
print(fruits)
"""

# symmetric_difference keeps items that are not duplicates. You can use the ^ operator.

cars1 = {"Volvo", "Peugeot", "Mercedes"}
cars2 = {"BMW", "Volvo", "Mercedes"}
cars3 = cars1.symmetric_difference(cars2)
print(cars3)


"""
The symmetric_difference_update() method will also keep all but the duplicates, 
but it will change the original set instead of returning a new set.
"""
cars1.symmetric_difference_update(cars2)
print(cars1)

