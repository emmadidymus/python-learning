day = 6

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Invalid input")



day = 5
month = 4
match day:
    case 1 | 2 | 3 | 4 | 5 if month == 4:
        print("Today is a weekday in April")
    case 6 | 7 if month == 4:
        print("I love April weekends!")
    case _:
        print("Invalid input")