#print user data as much as user wants
user_data=input("Enter any data: ")
count=int(input("How many time do you want to print the data? "))

while True:
    print(user_data)
    count-=1
    if count==0:
        break