#using for loop to iterate every single data in an iterable data
user=int(input("How many datas do you want to enter?: "))
user_info=[]
for user in range(user):
    user_data=input("Enter data: ")
    user_info.append(user_data)
print (user_info)
#loop