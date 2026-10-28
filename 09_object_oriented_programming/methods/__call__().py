"""
The __call__() magic method allows an object to be called like a function using the object() syntax
"""

class ClickCounter:
    def __init__(self):
        self.clicks = 0

    def __call__(self, *args, **kwargs):
        self.clicks += 1
        return self.clicks

click_counter = ClickCounter()

print(click_counter())
print(click_counter())
print(click_counter())
print(click_counter())

