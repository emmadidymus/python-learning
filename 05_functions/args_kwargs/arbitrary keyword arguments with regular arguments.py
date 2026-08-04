def my_function(username, **details):
    print("username: ", username)
    print("additional details: ")
    for key, value in details.items():
        print("" , key + ": " + value )

my_function("emmadidymus", name= "emmanuel", age = "50", gender= "male", hobby= "business")