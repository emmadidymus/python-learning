print("===========")
print("Journal CLI")
print("===========")

def add_entry():
    title = input("What is the title of your entry?: ")
    entry = input("What is the entry?: ")

    with open("journal.txt", "a") as f:
        f.write(title + "\n")
        f.write(entry + "\n")


add_entry()

def view_entries():
    try:
        with open("journal.txt") as f:
            print(f.read())
    except FileNotFoundError:
        print("There are no entries yet!")

view_entries()