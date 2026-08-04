def my_function(*numbers):
    total = 0
    for number in numbers:
        total += number
    print(total)

my_function(1, 2, 3)
my_function(89, 87, 34, 21)
