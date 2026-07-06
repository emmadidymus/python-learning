# using a for loop

thistuple = ("apple", "banana", "cherry")
for i in thistuple:
    print(i)

# loop through index numbers

for i in range(len(thistuple)):
    print(thistuple[i])

# using the while loop

i = 0
while i < len(thistuple):
    print(thistuple[i])
    i += 1