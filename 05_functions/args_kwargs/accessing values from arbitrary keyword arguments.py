def my_function(**myvar):
    print("Type: ", type(myvar) )
    print("Name: ", myvar['name'])
    print("Age: ", myvar['age'])
    print("All details: ", myvar)

my_function(name='Kit', age=20)