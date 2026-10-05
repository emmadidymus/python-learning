

def add_entry():
    title = input("What is the title of your entry?: ")
    entry = input("What is the entry?: ")

    with open("journal.txt", "a") as f:
        f.write(title + "\n")
        f.write(entry + "\n")



def view_entries():
    try:
        with open("journal.txt") as f:
            print(f.read())
    except FileNotFoundError:
        print("There are no entries yet!")


def search_entries():
    search = input("What word or phrase do you want to search for?: ")
    found = False
    try:
        with open("journal.txt") as f:
            for line in f:
                if search.lower() in line.lower():
                    print(line)
                    found = True
            if not found:
                print("No matching entries found!")
    except FileNotFoundError:
        print("There are no entries yet!")




while True:

    print("===========")
    print("Journal CLI")
    print("===========")

    print("1. Add Entry")
    print("2. View Entries")
    print("3. Search Entries")
    print("4. Delete all Entries")
    print("5. Exit")

    try:
        choice = int(input("Select the number of the action you want to perform: "))
    except ValueError:
        print("Please enter a valid choice (numbers 1 to 5)")
        continue

    if choice == 1:
        add_entry()
    elif choice == 2:
        view_entries()
    elif choice == 3:
        search_entries()
    elif choice == 5:
        print("Goodbye and thank you for using journal CLI")
        break
    else:
        print("Please select from choices 1 to 5")