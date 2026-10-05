print("===========")
print("Journal CLI")
print("===========")



title = input("What is the title of your entry?: ")
entry = input("What is the entry?: ")

with open("journal.txt", "a") as f:
    f.write(title + "\n")
    f.write(entry + "\n")

with open("journal.txt") as f:
    print(f.read())