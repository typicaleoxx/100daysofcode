#login program
#make dictionary, of username and password
#ask user, if both matches then access granted else denied

while True: 
    user_name=input("Enter your username: ")
    password=input("Enter your password: ")
    data={"typicaleoxx":"tuesday", "codewclumsy":"january", "sneha":"lama"}
    if user_name in data:
        if data.get(user_name)==password:
            print("Access granted.")
            break
        else:
            print ("Access denied.")
            break
    else:
        print ("Invalid username.")
        again=input("Do you want to try again?(y/n)")
        if again=="y":
            continue
        elif again=="n":
            print("Okay. Have a great day")
            break
        else :
            print("Invalid choice.")
            break
            
        
    