my_family = {
    "child1" : {
        "name":"Ida",
        "age":28,
        "gender":"Female"
    },

    "child2" : {
        "name":"Emmanuel",
        "age":25,
        "gender":"Male"
    },

    "child3" : {
        "name":"Aidan",
        "age":16,
        "gender":"Male"
    }
}

#print(my_family)

#accessing items
print(my_family["child3"]["name"])

for key in my_family.keys():
    print(key)

for value in my_family.values():
    print(value)
for key, value in my_family.items():
    print(key, value)


# Looping through nested dictionaries.

for child, details in my_family.items():
    print(child)

    for key, value in details.items():
        print(f"{key}: {value}")