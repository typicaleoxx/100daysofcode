import json

def main():
    """
    Main function to initiate the e-commerce system.
    """
    print("Welcome to the E-Commerce System!")
    user_choice = input("Do you want to login or register (l/r): ").lower().strip()

    if user_choice == "l":
        login()
    elif user_choice == "r":
        register()
    else:
        print("Invalid choice. Exiting.")

def register():
    """
    Function to handle user registration.
    """
    username = input("Please enter your username: ")
    password = input("Please enter your password: ")
    user_type = input("Are you a buyer or a seller (buyer/seller): ").lower().strip()

    try:
        if user_type in ["buyer", "seller"]:
            user_data = {"username": username, "password": password, "user_type": user_type}
            with open("user_data.json", "a") as file:
                file.write("\n")
                json.dump(user_data, file)
                print("Registration successful.")
            ask = input("Do you want to login (y/n): ").lower().strip()
            if ask == "y":
                login()
            else:
                print(f"Thank you, {username}. Have a great day.")
        else:
            print("Invalid user type. Registration failed.")
    except Exception as e:
        print(f"Registration error: {e}")

def login():
    """
    Function to handle user login.
    """
    username = input("Please enter your username: ")
    password = input("Please enter your password: ")

    try:
        with open("user_data.json", "r") as file:
            login_successful = False

            for data in file:
                user_data = json.loads(data)
                if user_data.get("username") == username and user_data.get("password") == password:
                    login_successful = True
                    print("Login successful!")

                    if user_data["user_type"] == "buyer":
                        buyer_menu()
                    elif user_data["user_type"] == "seller":
                        seller_menu()

                    break

            if not login_successful:
                print("Invalid username or password.")
    except Exception as e:
        print(f"Login error: {e}")

def buyer_menu():
    """
    Buyer menu options.
    """
    try:
        print("Buyer Menu:")
        print("1. View all products")
        print("2. View your bills")
        print("3. Purchase products")
        user_choice = input("Enter your choice (1/2/3): ").strip()

        if user_choice.isdigit() and int(user_choice) in [1, 2, 3]:
            user_choice = int(user_choice)
            if user_choice == 1:
                view_all_products()
            elif user_choice == 2:
                view_user_bills()
            elif user_choice == 3:
                purchase_products()
        else:
            print("Invalid choice.")
    except Exception as e:
        print(f"Error in buyer menu: {e}")

def view_all_products():
    """
    Function to view all available products.
    """
    print("Viewing all products.")

def view_user_bills():
    """
    Function to view user bills.
    """
    print("Viewing user bills.")

def purchase_products():
    """
    Function to handle product purchase.
    """
    print("Purchasing products.")

def seller_menu():
    """
    Seller menu options.
    """
    try:
        print("Seller Menu:")
        print("1. Add product")
        print("2. View your products")
        print("3. View your product bills")
        print("4. Delete product")
        user_choice = input("Enter your choice (1/2/3/4): ").strip()

        if user_choice.isdigit() and int(user_choice) in [1, 2, 3, 4]:
            user_choice = int(user_choice)
            if user_choice == 1:
                add_product()
            elif user_choice == 2:
                view_seller_products()
            elif user_choice == 3:
                view_seller_bills()
            elif user_choice == 4:
                delete_product()
        else:
            print("Invalid choice.")
    except Exception as e:
        print(f"Error in seller menu: {e}")

def add_product():
    """
    Function to add a product.
    """
    print("Adding product.")

def view_seller_products():
    """
    Function to view seller products.
    """
    print("Viewing seller products.")

def view_seller_bills():
    """
    Function to view seller bills.
    """
    print("Viewing seller bills.")

def delete_product():
    """
    Function to delete a product.
    """
    print("Deleting product.")

if __name__ == "__main__":
    main()
