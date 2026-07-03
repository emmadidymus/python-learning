num = 6

x = "Weekend" if num > 5 else "Workday"
print(x)

"""
The ternary operator is not an actual operator. It is a conditional statement 
or simply a shorthand if statement
"""

"""
The ternary operator can be used instead of elif in longer if statements
"""

num = 6

x = "Fri" if num == 5 else "Sat" if num == 6  else  "Sun" if num == 7 else "Workday"
print(x)