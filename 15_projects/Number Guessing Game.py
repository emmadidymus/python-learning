import random


while True:
    x = random.randint(1, 50)

    while True:

        try:
            y = int(input("Guess the number: "))
        except ValueError:
            print("Please enter a valid Integer!")
            continue

        if y < x:
            print("Too low!")
        elif y > x:
            print("Too high!")
        else:
            print("Congratulations! You guessed the right number!")
            break

    repeat = input("Play again? (Yes/No): ")

    if repeat.lower() == 'yes':
        continue
    else:
        break
