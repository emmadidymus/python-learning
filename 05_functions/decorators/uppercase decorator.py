"""
define the decorator first
then apply it above the function with @decorator_name
"""

def changecase(func):
    def myinner():
        return func().upper()
    return myinner

@changecase
def greeting():
    return "Hello, Sally!"

print(greeting())