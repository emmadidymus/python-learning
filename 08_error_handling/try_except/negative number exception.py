"""
The program below raises an error if the value of x is negative
"""

x = int(input("Please enter a number: "))

if x < 0:
    raise Exception ("Sorry, no numbers below zero!")
elif x % 2 == 0:
    print("You entered an even number")
else:
    print("You entered an odd number")