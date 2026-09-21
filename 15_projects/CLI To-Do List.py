tasks = []

while True:
    print("==============")
    print("TO-DO LIST")
    print("==============")


    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")


    try:
        choice = int(input("Choose the number of the task you want to do: "))
    except ValueError:
        print("Please enter a number from 1 to 4")
        continue

    if choice == 1:
        enter_task = input("Enter Task: ")
        tasks.append(enter_task)

    elif choice == 2:
        if not tasks:
            print("No tasks yet")
            
        for task in tasks:
            print(task)


    elif choice == 3:
        try:
            remove_task = input("What task should be removed?: ")
            tasks.remove(remove_task)
            print("Task removed!")
        except ValueError:
            print("Task not found!")

    elif choice == 4:
        break

    else:
        print("Please choose a number from 1 to 4")
