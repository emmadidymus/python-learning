# without list comprehension

list = ["apple", "banana", "cherry", "blackcurrant", "pomegranate", "orange", "tangerine"]
newlist = []

for x in list:
    if "a" in x:
        newlist.append(x)

print(newlist)

# with list comprehension

newlist = [x for x in list if "a" in x]
print(newlist)