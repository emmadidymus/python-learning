import math

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


            print("Result:", results(x, y, z))


        elif y in ["sqrt"]:
            while True:
                try:
                    a = float(input("Enter a number: "))
                    break
                except ValueError:
                    print("Please enter a valid number!")


            def sqrt(a):
                return math.sqrt(a)


            print("The square root is:", sqrt(a))
        else:
            print("Please enter a valid operator!")

        break

    repeat = input("Calculate again?(Yes/No): ")

    if repeat.lower() == "yes":
        continue
    else:
        break


