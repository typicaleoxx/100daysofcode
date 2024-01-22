# login or register program using file handling
# Ask if user  wants to login or register
# Register - Ask username and password, and add the data to a file using file handling
# Login - Ask username an password, then 
# read data from the file where user data is being stored during register and 
# check whether the username and password provided exists or not. 
import json

def register():
    user_username = input('Enter your username : ')
    user_password = input('Enter your password : ')
    user_data = {user_username:user_password}
    json_user_data = json.dumps(user_data)

    f = open('userdata.txt','a')
    try:
        f.write(json_user_data + '-')
    except:
        print("Registration Error.")

    f.close()

def login():
    user_username = input('Enter your username : ')
    user_password = input('Enter your password : ')
    f = open('userdata.txt','r')
    json_user_datas = f.read()
    f.close()
    list_user_data = json_user_datas.split('-')
    
    for i in list_user_data:
        if i != '':
            dict_data = json.loads(i)
            if user_username in dict_data and user_password == dict_data.get(user_username):
                print('Login successfull!')
            else:
                print('Invalid credentials!')
def main():
    user_choice = input('Do you want to login or register? (l/r)').lower()

    if user_choice == 'l':
        login()
    elif user_choice == 'r':
        register()
main()
