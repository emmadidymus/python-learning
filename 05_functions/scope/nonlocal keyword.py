"""
nonlocal keyword is used to work with variables inside nested functions.
the nonlocal keyword makes the variable belong to the outer function.

"""

def my_function1():
    x = "Jane"
    def my_function2():
        nonlocal x
        x = "Hello"
    my_function2()
    return x
print(my_function1())