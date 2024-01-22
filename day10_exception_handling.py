#calculator
#requirements
#ask user for two numbers
#ask operation
#print result
#at last ask if user wants to run the calculator again

def main():
    while True:
        try:
            num1=int(input("Enter first number: "))
            num2=int(input("Enter second number: "))
            break
        except ValueError:
            main()
    oper=input("What operation do you want to perform(+,-,/,*)")
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
        if ask=="n" or ask=="y":
            if ask=="y":
                main()
            else:
                print("Okay, have a great day.")
        else:
            print("Invalid input.")
            ask()
main()


    
    
    
    