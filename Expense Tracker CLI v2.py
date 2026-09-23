expenses = []


def add_expense():
    expense_description = input("What is the expense: ")
    try:
        expense_amount = int(input("Enter the expense amount: "))
    except ValueError:
        print("Please enter a valid amount!")
        return

    expense = {
        "description": expense_description,
        "amount": expense_amount
    }

    expenses.append(expense)
    print("Expense added!")


def view_expenses():
    if not expenses:
        print("No expenses added yet!")
    else:
        for expense in expenses:
            print(expense["description"], expense["amount"])


def calculate_total():
    total = 0
    for expense in expenses:
        total += expense["amount"]
    return total


def remove_expense():
    if not expenses:
        print("There are no expenses to remove!")
    else:
        for i in range(len(expenses)):
            print(i + 1, expenses[i]["description"], expenses[i]["amount"])
        try:
            expense_number = int(input("Choose the number of the expense you want to remove: "))
            expenses.pop(expense_number - 1)
            print("Expense removed!")
        except ValueError:
            print("Please enter a valid number!")
        except IndexError:
            print("Please enter a valid expense number!")


while True:
    print("===============")
    print("EXPENSE TRACKER")
    print("===============")

    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Calculate Total")
    print("4. Remove Expense")
    print("5. Exit")

    try:
        choice = int(input("Choose the number of task you want to perform: "))
    except ValueError:
        print("Please enter a number from 1 to 5")
        continue

    if choice == 1:
        add_expense()
    elif choice == 2:
        view_expenses()
    elif choice == 3:
        total = calculate_total()
        print(f"The total of your expenses is {total}")
    elif choice == 4:
        remove_expense()
    elif choice == 5:
        print("Thank you for using the expense tracker!")
        break
    else:
        print("Choose a number from 1 to 5")