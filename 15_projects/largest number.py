"""
this Python program loops through a list to find the largest number.
it first assumes that the first number is the largest.
it then compares it to other numbers.
if it finds a number larger than it, it instead remembers that number and drops the previous one.
"""

numbers = [12, 34, 54, 21, 65, 12, 67, 9]

largest = numbers[0]

for number in numbers:
    if number > largest:
        largest = number

print(f"The largest number is {largest}")

