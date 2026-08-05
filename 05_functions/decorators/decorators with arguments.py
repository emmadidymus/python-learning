def uppercase(n):
    def uppercase(func):
        def myinner():
            if n == 1:
                a = func().lower()
            else:
                a = func().upper()
            return a
        return myinner
    return uppercase

@uppercase(1)
def say_hello():
    return f"Hello Linus"
print(say_hello())

@uppercase(4)
def say_hello2():
    return f"Hello Linus"
print(say_hello2())