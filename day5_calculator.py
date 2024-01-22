
num1 = int(input('Enter a number : '))
num2 = int(input('Enter another number : '))
    
math_opt = input('Which arithematic operation do you want to perform [+,-,*,/] : ')

if math_opt == '+':
    result=num1+num2
    print(f"{num1} + {num2}= {result}")
elif math_opt == '-':
    result=num1-num2
    print(f"{num1} - {num2}= {result}")
elif math_opt == '*':
    result=num1*num2
    print(f"{num1} * {num2}= {result}")
elif math_opt == '/':
    result=num1/num2
    print(f"{num1} / {num2}= {result}")
else:
    print('Invalid operator!')

    

  


# Variable naming laws
# Define a meaningful name for a variable according to the data it will store

# Identifiers cases
# Pascal case
# Camel case
# Snake case

my_variable1 = None