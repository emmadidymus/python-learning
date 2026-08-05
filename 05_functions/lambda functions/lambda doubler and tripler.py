def my_function(n):
    return lambda a: a * n

my_doubler = my_function(2)
my_tripler = my_function(3)

print(my_doubler(11))
print(my_tripler(11))