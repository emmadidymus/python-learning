import random

x = random.randint(1,100)

while True:
    try:
        y = int(input("A random number has been generated. Try and guess it: "))
        break
    except ValueError:
        print("Please enter a valid integer!")

while True:
    if y < x:
        print("Too low!")
        while True:
            try:
                y = int(input("Guess again: "))
                break
            except ValueError:
                print("Please enter a valid integer!")


    elif y > x:
        print("Too high!")
        while True:
            try:
                y = int(input("Guess again: "))
                break
            except ValueError:
                print("Please enter a valid integer!")

    elif y == x:
        print(f"Congratulations! You guessed it right attempts")
        break


