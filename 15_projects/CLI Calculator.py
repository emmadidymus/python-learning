print("=================")
print("CLI CALCULATOR")
print("=================")


def result(x,y,z):
    try:
        if y == "+":
            return x + z

        elif y == "-":
            return x - z

        elif y == "*":
            return x * z

        elif y == "/":
            return x / z

        elif y == "%":
            return x % z

        elif y == "**":
            return x ** z
        return None
    except ZeroDivisionError:
        return "Error! Cannot divide by zero!"



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


y = input("Enter Operator(+, -, *, /, %, **): ")


print("Result: ", result(x,y,z))

