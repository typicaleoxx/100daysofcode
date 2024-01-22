#ask if user wants to login or register
#if register then
#take username and password from user
#then add data to a variable
#elif login ask for username and password then check whether its is in a variable
#if found, print login successful else invalid login
#whole program in loop
user_data = {} #global variable declare gareko
def main():
    user=input("Do you want to login or register(l/r)")
    if user=="l" or user=="r":
        if user=="l":
            login()
        elif user=="r":
            register()
    else:
        print("Please make a valid choice. ")
        main()

def login():
    try:
        username=input("Please enter your username: ")
        password=input("Please enter your password: ")
    except ValueError:
        print("Enter valid data.")
        login()
    if username in user_data:
        if user_data.get(username)==password:
            print("Login successful. ")
        else:
            print("Invalid password. Try again! ")
    else:
        print("Invalid username. Try again!")
    ask()
# var["username"]="password"
def register():
    try:
        username=input("Enter the username: ")
        password=input("Enter the password: ")
        user_data[username] = password
        if username in user_data:
            print("Registration Successful")
        else:
            print("Error Try again.")
    except:
        print("Invalid input. ")
    ask()
def ask():
    again=input("do you want to login or register again? (y/n)")
    if again=="y":
        main()
    else:
        print("Okay then, have a great day.")
main()