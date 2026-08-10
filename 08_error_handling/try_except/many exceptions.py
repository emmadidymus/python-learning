"""
You can define as many exception blocks as you want
"""

try:
    print(x)
except NameError:
    print("Variable x is not defined!")
except:
    print("Something else went wrong!")