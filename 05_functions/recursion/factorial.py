def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(int(input("Enter the number whose factorial you would like to calculate: "))))