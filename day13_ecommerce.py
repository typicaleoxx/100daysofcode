#e-commerce system
#requirements
#first, ask if login or register
#if register, ask username and password and ask user type buyer or seller
#if login then check if user exists, also check user type
#if buyer-give choices to view product, view bills, purchase products
#if seller-give choices to add product, view their products, bills, delete products,  
import json
def main():
    user=input("Do you want to login or register(l/r)")
    if user=="l" or user=="r":
            if user=="l":
                login()
            else:
                register()
    
def register():
    username=input("Please enter your username: ")
    password=input("Please enter your password: ")
    user_type=input("Are you a buyer or a seller(buyer/seller)").lower().strip()
    try:
        if user_type=="buyer" or user_type=="seller":
            user_data={"username":username, "password":password, "user_type":user_type}
            file=open("user_data.json","a")
            try:
                json.dump(user_data,file)
                print("Registration successfull")
                file.close()
                ask=input("Do you want to login(y/n)").lower().strip()
                if ask=="y":
                    login()
                else:
                    print(f"Alright {username}, have a great day.")
            except:
                print("Registration error")
    except:
        print("Make a valid choice")
        
def login():
    username=input("Please enter your username: ")
    password=input("Please enter your password: ")
    file=open("user_data.json","r")
    for data in file:
        user_data=json.loads(data)
        if user_data.get("username")==username and user_data.get("password")==password:
            print("Login Successful !")
            if user_data["user_type"]=="buyer":
                buyer_menu()
            elif user_data["user_type"]=="seller":
                seller_menu()
            break
        else:
            print("Invalid username or password. ")
def seller_menu():
    try:
        print("Seller Menu")
        print("1. Add products")
        print("2. View your products")
        print("3. View your product bills")
        print("4. Delete products")
        user_choice=input("Enter your choice (1/2/3)")
        if user_choice in [1,2,3,4]:
            if user_choice==1:
                add_products()
            elif user_choice==2:
                view_your_products()
            elif user_choice==3:
                product_bills()
        else: 
            print("Invalid choice")
    except:
        print("An error occured. ")


def add_products():
    pass

def view_your_products():
    pass

def purchase_products():
    pass

def product_bills():
    pass

def buyer_menu():
    try:
        print("Buyer Menu: ")
        print("1. View all products")
        print("2. View your bills ")
        print("3. Purchase products ")
        user_choice=input("Enter your choice (1/2/3)")
        if user_choice in [1,2,3]:
            if user_choice==1:
                view_all_products()
            elif user_choice==2:
                view_user_bill()
            else:
                purchase_products()
        else: 
            print("Invalid choice.")
    except:
        print("Error occured")
def view_all_products():
    pass
def view_user_bill():
    pass

main()
            