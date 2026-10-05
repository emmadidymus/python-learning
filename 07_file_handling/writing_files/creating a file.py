#with open("demofile.txt", "x") as f:
    #f.write("Hello there!")

with open("demofile.txt", "a") as f:
    f.write("First Entry\n")



with open("demofile.txt", "a") as f:
    f.write("Second Entry\n")


with open("demofile.txt") as f:
    print(f.read())
