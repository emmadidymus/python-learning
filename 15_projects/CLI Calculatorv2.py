import math


def calculate(x, operator, z):
    try:
        if operator == '+':
            return x + z
        elif operator == '-':
            return x - z
        elif operator == '*':
            return x * z
        elif operator == '/':
            return x / z
        elif operator == '%':
            return x % z
        elif operator == '**':
            return x ** z
    except ZeroDivisionError:
        return "Error! Cannot divide by zero!"

while True:
    print("=================")
    print("CLI CALCULATOR")
    print("=================")

    while True:

        operator = input("Enter Operator(+, -, *, /, %, **,sqrt): ")

        if operator in ["+", "-", "*", "/", "%", "**"]:
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


            print("Result:", calculate(x, operator, z))
            break


        elif operator in ["sqrt"]:
            while True:
                try:
                    a = float(input("Enter a number: "))
                    print("The square root is:", math.sqrt(a))
                    break
                except ValueError:
                    print("Please enter a nonnegative number!")
            break

        else:
            print("Please enter a valid operator!")

    repeat = input("Calculate again? (Yes/No): ")

    if repeat.lower() == 'yes':
        continue
    else:
        break







