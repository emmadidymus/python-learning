fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    if fruit == "banana":
        break
    print(fruit)


for fruit in fruits:
    print(fruit)
    if fruit == "banana":
        break

for fruit in fruits:
    if fruit == "banana":
        continue
    print(fruit)


