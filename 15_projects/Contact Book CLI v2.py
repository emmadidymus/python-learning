contacts = []

def add_contact():
    name = input("Name?: ")
    phone_number = input("Phone number?: ")
    email = input("Email?: ")

    contact = {"Name": name, "Phone Number": phone_number, "Email": email}
    contacts.append(contact)
    print("Contact Added!")

def view_contacts():
    if not contacts:
        print("No contacts added yet!")
    else:
        for i in range(len(contacts)):
            print(i + 1, contacts[i]["Name"], contacts[i]["Phone Number"], contacts[i]["Email"])

def search_contact():
    search = input("Enter a name to search: ")

    found = False

    for contact in contacts:
        if search.lower() in contact["Name"].lower():
            print(contact["Name"], contact["Phone Number"], contact["Email"])
            found = True

    if not found:
        print("Contact not found!")

def remove_contact():
    if not contacts:
        print("No contacts to remove!")
    else:
        for i in range(len(contacts)):
            print(i + 1, contacts[i]["Name"], contacts[i]["Phone Number"], contacts[i]["Email"])

        try:
            contact_number= int(input("Enter the number of the contact you want to remove: "))
            contacts.pop(contact_number - 1)
            print("Contact removed!")

        except ValueError:
            print("Please enter a valid number!")
        except IndexError:
            print("Please choose a valid contact number")



while True:
    print("============")
    print("CONTACT BOOK")
    print("============")

    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Remove Contact")
    print("5. Exit")

    try:
        choice = int(input("Choose the number of the task you want to perform: "))
    except ValueError:
        print("Enter a valid choice number from 1 to 5")
        continue

    if choice == 1:
        add_contact()

    elif choice == 2:
        view_contacts()

    elif choice == 3:
        search_contact()

    elif choice == 4:
        remove_contact()

    elif choice == 5:
        print("Thank you for using Contact Book!")
        break

    else:
        print("Choose a number from 1 to 5")
