y = True

while y == True:
    x = input("Enter a number: ")

    try:
        x = float(x)
        y = False
    except:
        print("Wrong input! Please enter a number!")

print("Thank You!")