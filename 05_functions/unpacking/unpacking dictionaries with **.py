def my_function(fname, lname):
    print("Hello", fname, lname)

person = {"fname": "Emily", "lname": "Jones"}
my_function(**person)