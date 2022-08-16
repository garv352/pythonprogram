num1 = int(input('Enter the First number'))
num2 = int(input('Enter the second number'))
operation = input('Please choose an option to perform +,-,*,/')


def add(num1,num2):
    return num1 + num2

def sub(num1,num2):
    return num1 - num2

def multiply(num1,num2):
    return num1 * num2

def divide(num1,num2):
    return num1 / num2

def remainder(num1,num2):
    return num1 % num2



if operation == '+' :
    print('The addition for', num1, 'and', num2 , 'is', add(num1,num2))

elif operation == '-':
    if num1 == num2 :
        print(' The Subtraction for', num1, 'and', num2 , 'is', sub(num1,num2), 'and Entered numbers are same')
    elif sub(num1 , num2) < 0 :
        print ('The Subtraction for', num1, 'and', num2 , 'is', sub(num1,num2), 'and the solution is Negative')
    else:
        print('The Subtraction for', num1, 'and', num2 , 'is', sub(num1,num2))
    
    
    
elif operation == '*':
    print('The Multiplication for', num1 ,'and', num2 , 'is', multiply(num1,num2))
    
elif operation == '/':
    print('The Division for', num1 ,'and', num2 , 'is', round(divide(num1,num2),2), 'and remainder is', remainder(num1,num2) )
else:
    print("Can't be printed")
