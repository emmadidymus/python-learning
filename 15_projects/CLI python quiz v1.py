questions = [
    {"question" : "which keyword is used to define a function in python?",
     "options" : ["A.function", "B. def", "C. func", "D. define"],
     "answer" : "B"},

    {"question": "Which of the following creates a Python list?",
     "options": ["A. ('apple', 'banana')", "B. {'apple', 'banana'}", "C. ['apple', 'banana']", "D. <'apple', 'banana'>"],
     "answer": "C"},

    {"question": "Which data structure stores information as key-value pairs?",
     "options": ["A. List", "B. Tuple", "C. Set", "D. Dictionary"],
     "answer": "D"},

    {"question": "Which loop is commonly used when you want to iterate through every item in a list?",
     "options": ["A. if", "B. for", "C. try", "D. def"],
     "answer": "B"},

    {"question": "Which block is used to handle an exception in Python?",
     "options": ["A. catch", "B. error", "C. except", "D. handle"],
     "answer": "C"}

]
score = 0

for question in questions:
    print(question["question"])

    for option in question["options"]:
        print(option)

    while True:
        answer = input("Enter you answer: ").upper()

        if answer in ['A', 'B', 'C', 'D']:
            break
        else:
            print("Please enter A, B, C, or D")

    if answer == question["answer"]:
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")

print(f"You scored {score} out of {len(questions)}")

percentage_score = (score / len(questions)) * 100

print(f"Your percentage score is {percentage_score} percent")
