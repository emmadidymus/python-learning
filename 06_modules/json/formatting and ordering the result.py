import json

x = {
    "name":"John",
    "age":24,
    "married":True,
    "divorced":False,
    "children":("Andrea", "Billy"),
    "pets":None,
    "cars":[
        {"model":"BMW 230", "mpg":27.5},
        {"model":"Ford Edge", "mpg":24.1}
    ]
}

print(json.dumps(x, indent=4, separators=(", ", "="), sort_keys=False))