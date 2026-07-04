# using the sort() method to sort the list alphanumerically, ascending by default

fruits = ["apple", "banana", "cherry", "mango", "pomegranate", "tangerine", "orange", "kiwi"]
fruits.sort()
print(fruits)

# sort descending
fruits.sort(reverse=True)
print(fruits)

# customize sort function

def my_function(n):
    return  abs(n-50)

numbers = [30, 50, 23, 65, 110]
numbers.sort(key=my_function)
print(numbers)

"""
sort() is case sensitive by default. This results in it sorting upper case before lower case.
If you want it to be case insensitive, use str.lower() as a key function.
"""
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key=str.lower)
print(thislist)

# You can use the reverse() method to reverse the order of  a list.
thislist.reverse()
print(thislist)
