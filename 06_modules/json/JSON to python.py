import json

x = '{"name":"Jon", "age":23, "country":"SA"}'

y = json.loads(x)

print(y)