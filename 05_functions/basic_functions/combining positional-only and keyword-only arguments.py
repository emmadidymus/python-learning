# the parameters before / are positional and the parameters after * are keyword

def my_function(a, b, / , *, c, d):
    return a + b + c + d

print(my_function(3, 5, c = 5, d = 3))