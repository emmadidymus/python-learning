"""
You can combine regular parameters with *args.
The regular parameters must come before *args.
"""

def my_function(greeting, *names):
    for name in names:
        print(greeting, name)

my_function("Hello", "Jon", "John", "Constantine", "Roger")