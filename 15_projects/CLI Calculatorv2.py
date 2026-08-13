import math


def results(x, y, z):
    try:
        if y == '+':
            return x + z
        elif y == '-':
            return x - z
        elif y == '*':
            return x * z
        elif y == '/':
            return x / z
        elif y == '%':
            return x % z
        elif y == '**':
            return x ** z
    except ZeroDivisionError:
        return "Error! Cannot divide by zero!"

while True:
    print("=================")
    print("CLI CALCULATOR")
    print("=================")

    while True:

        y = input("Enter Operator(+, -, *, /, %, **,sqrt): ")

        if y in ["+", "-", "*", "/", "%", "**"]:
            while True:
                try:
                    x = float(input("Enter the first number: "))
                    break
                except ValueError:
                    print("Please enter a valid number!")

            while True:
                try:
                    z = float(input("Enter the second number: "))
                    break
                except ValueError:
                    print("Please enter a valid number!")


            print("Result:", results(x, y, z))
            break


        elif y in ["sqrt"]:
            while True:
                try:
                    a = float(input("Enter a number: "))
                    print("The square root is:", math.sqrt(a))
                    break
                except ValueError:
                    print("Please enter a nonnegative number!")


        else:
            print("Please enter a valid operator!")

    repeat = input("Calculate again? (Yes/No): ")

    if repeat.lower() == 'yes':
        continue
    else:
        break







