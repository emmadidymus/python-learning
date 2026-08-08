"""
You can convert a python object into JSON using the json.dumps() method
"""

import json

x = {
    "name":"Jon",
    "age":23,
    "country":"Norway"
}

y = json.dumps(x)

print(y)