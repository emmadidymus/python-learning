
contacts = []

while True:
    print("============")
    print("CONTACT BOOK")
    print("============")

    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Remove Contact")
    print("5. Exit")

    choice = int(input("Choose the number of the task you want to perform: "))

    if choice == 1:
        name = input("Name?: ")
        phone_number = input("Phone number?: ")
        email = input("Email?: ")

        contact = {"Name":name, "Phone Number":phone_number, "Email":email}
        contacts.append(contact)
        print("Contact Added!")

    elif choice == 2:
        if not contacts:
            print("No contacts added yet!")
        else:
            for i in range(len(contacts)):
                print(i+1, contacts[i]["Name"], contacts[i]["Phone Number"], contacts[i]["Email"])

    elif choice  == 3:
        search = input("Enter a name to search: ")

        found = False

        for contact in contacts:
            if search.lower() in contact["Name"].lower():
                print(contact)
                found = True

        if not found:
            print("Contact not found!")

    elif choice == 4:
        if not contacts:
            print("No contacts to remove!")
        else:
            for i in range(len(contacts)):
                print(i+1, contacts[i]["Name"], contacts[i]["Phone Number"], contacts[i]["Email"])

            try:
                remove_contact = int(input("Enter the number of the contact you want to remove: "))
                contacts.pop(remove_contact - 1)
                print("Contact removed!")

            except ValueError:
                print("Please enter a valid number!")
            except IndexError:
                print("Please choose a valid contact number")

    elif choice == 5:
        print("Thank you for using Contact Book!")
        break











