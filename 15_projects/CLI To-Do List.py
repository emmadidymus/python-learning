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
        print("Task added!")

    elif choice == 2:
        if not tasks:
            print("No tasks yet")

        for i in range(len(tasks)):
            print(i+1, tasks[i])


    elif choice == 3:
        try:
            remove_task = int(input("What task number should be removed?: "))
            tasks.pop(remove_task-1)
            print("Task removed!")
        except ValueError:
            print("Please enter a valid number!")
        except IndexError:
            print("Please enter a valid task number ")

    elif choice == 4:
        break

    else:
        print("Please choose a number from 1 to 4")
