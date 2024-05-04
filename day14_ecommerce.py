# Requirements
# Ask the user if he/she wants to login or register
# Register - Ask username, password, usertype (Buyer/Seller) and store it in a file
# Login - Ask username and password , if the username and password exists on userdata file then print login successfull. Check the usertype.
# If the user is buyer , give him choices : View all products, View his/her bills, Purchase products. If the user is seller : Add products, View his/her products, View his/her products bills

# User data = {"username":"ram","password":"ram123","usertype":"buyer"}

# {'username':'password','usertype':'buyer'}

import json

def register():
    user_name = input("Enter your username: ")
    user_password = input("Create a password: ")
    user_type = input("Are you a buyer or seller? ").lower()

    user_data = {"user_name": user_name, "user_password": user_password, "user_type" :user_type }
    json_user_data = json.dumps(user_data)

    f = open("userdata.txt","a")
    f.write(json_user_data + "-")
    f.close()
    user_log = input("Do you want to login? [y/n]").lower()
    if user_log == "y":
        login()
    else:
        print("thankyou for the registration!!")

def login():
    user_name = input("Enter your username: ")
    user_password = input("Enter your password: ")
    
    f = open("userdata.txt","r")
    json_user_datas = f.read()
    f.close()
    list_user_data = json_user_datas.split("-")
    user_login = False
    for i in list_user_data:
        if i!= '':
            dict_data = json.loads(i)
            if (user_name == dict_data.get("user_name")) and user_password == dict_data.get("user_password"):
                user_login = True
                type = dict_data.get("user_type") 
                break

    if user_login == True:
        print("Login Successful!!")
        if type == "buyer":
            print(f"Hi {dict_data.get('user_name')}! Welcome to your buyer account.")
            print("What would you like to do? ")
            user_operation = input("[view products/ purchase/ view bills] :").lower() 
            if user_operation == "view product" or user_operation == "view products":
                view_all_products()   
            elif user_operation == "view bill" or user_operation == "view bills":
                view_bills()
            elif user_operation == "purchase":
                purchase()
            else:
                print("Invalid selection!!!")
        else:
            print(f"Hi {dict_data.get('user_name')}! Welcome to your seller account.")
            print("What would you like to do? ")
            user_operation = input("[add product/ view bills] :").lower() 
            if user_operation == "add product" or user_operation == "add products":
                add_product()
            elif user_operation == "view bill" or user_operation == "view bills":
                view_bills()
            else:
                print("Invalid selection!!!")
        
    else:
        print("Invalid Credentials!!")                              

def view_bills():
    pass

def purchase():
    purchase_product_name = input('Which product do you want to buy? ')
    purhcase_quantity = int(input('How much quantity? '))

    f = open('productdata.txt','r')

    product_json_data = f.read()

    f.close()

    list_product_data = product_json_data.split('-')

    for i in list_product_data:
        if i != '':
            dict_data = json.loads(i)
            if purchase_product_name == dict_data['product_name']:
                price = int(dict_data['product_price'])

    print('Purchase completed!')

    print(f'Your total is {purhcase_quantity * price}')



def view_all_products():
    f = open('productdata.txt','r')

    product_json_data = f.read()

    f.close()

    list_product_data = product_json_data.split('-')

    for i in list_product_data:
        print(i)

    purchase()

def view_products():
    pass

def add_product():
    product_name = input('Enter product name : ')
    product_description = input('Enter product description : ')
    product_price = input('Enter product price : ')

    product_dict_data = {'product_name':product_name,'product_desc':product_description,'product_price':product_price}
    product_json_data = json.dumps(product_dict_data)
    f = open('productdata.txt','a')

    f.write(product_json_data + '-')

    f.close()


user_input = input("Do you want to login or register? ").lower()

if user_input == "register":
    register()

if user_input == "login":
    login()
