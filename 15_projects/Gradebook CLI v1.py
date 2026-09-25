students = []



while True:
    print("==========")
    print("GRADE BOOK")
    print("==========")

    print("1. Add Students")
    print("2. View Students")
    print("3. Calculate Student Average")
    print("4. Show Class Average")
    print("5. Exit")

    try:
        choice = int(input("Choose from options 1 to 5: "))
    except ValueError:
        print("Please choose from options 1 to 5")
        continue

    if choice == 1:
        student_name = input("Name?: ")
        mark1 = int(input("Mark 1?: "))
        mark2 = int(input("Mark 2?: "))
        mark3 = int(input("Mark 3?: "))

        marks = [mark1, mark2, mark3]
        student = {"Name": student_name, "Marks": marks}
        students.append(student)

    elif choice == 2:
        if not students:
            print("There are no any student records yet!")
        else:
            for i in range(len(students)):
                print(i+1, students[i]["Name"], "Marks: ", students[i]["Marks"])

    elif choice == 3:
        if not students:
            print("There are no any student records yet!")
        else:
            for i in range(len(students)):
                print(i + 1, students[i]["Name"], "Marks: ", students[i]["Marks"])

            try:
                student_number = int(input("Choose the number of the student whose average you want to calculate: "))
                student = students[student_number-1]
            except ValueError:
                print("Please enter a valid number!")
                continue
            except IndexError:
                print("Please enter a valid student number!")
                continue

            student_average = sum(student["Marks"]) / len(student["Marks"])

            print(f"{student['Name']}'s average is {student_average:.2f}")

    elif choice == 4:
        if not students:
            print("There are no student records yet!")
        else:
            total_marks = 0
            number_of_marks = 0
            for student in students:
                for mark in student["Marks"]:
                    total_marks += mark
                    number_of_marks += 1
            class_average = total_marks / number_of_marks
            print(f"The class average is {class_average:.2f}")

    elif choice == 5:
        print("Thank you for using Gradebook!")
        break

    else:
        continue












