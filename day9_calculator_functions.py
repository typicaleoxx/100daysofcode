#calculator
#requirements
#ask user for two numbers
#ask operation
#print result
#at last ask if user wants to run the calculator again

def main():
    num1=int(input("Enter one number: "))
    num2=int(input("Enter second number: "))
    oper=input("What operation you want to perform")
    print(f"{num1} {oper} {num2}= {calculation(num1,num2,oper)}")
    ask()
    
def calculation(a,b,c):
    if c=="+":
        d=a+b
    elif c=="*":
        d=a*b
    elif c=="-":
        d=a-b
    elif c=="/":
        d=a/b
    else:
        d="invalid input ! try again"
    return d

def ask():
    ask=input("do you want to run the calculator again(y/n)? ")
    if ask=="y":
        main()
    elif ask=="n":
        print("Okay. Have a great day!")
    else:
        print("Invalid input. Try again")
main()


    
    
    