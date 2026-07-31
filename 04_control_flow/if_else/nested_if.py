username = "emmanuel"
password = "qwe221"
is_active = True

if username:
    if password:
        if is_active:
            print(f"Logged in successfully as {username}")
        else:
            print("Account is inactive")
    else:
        print("Password is required")
else:
    print("Username is required")