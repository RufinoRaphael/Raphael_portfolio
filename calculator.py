def add(x,y):
    return x + y

def subtract(x,y):
    return x - y

def multiply(x,y):
    return x * y

def divide(x,y):
    return x / y


print("Enter 'a' for addition")
print("Enter 's' for subtraction")
print("Enter 'm' for multiplication")
print("Enter 'd' for dividion")




while True:
    choice = input('Enter choice: (a, s, m, d): ')
    if choice.lower() in ('a', 'add','addition','s','subtract','subtraction', 'm','multiply','multiplication', 'd', 'divide', 'division'):
        num1 = float(input('Enter first number: '))
        num2 = float(input('Enter second number: '))
    
        if choice.lower() in ('a', 'add','addition'):
            print('Result: {} + {} = '.format(num1,num2),add(num1,num2))
            
        elif choice.lower() in ('s','subtract','subtraction'):
            print('Result: {} - {} = '.format(num1,num2),subtract(num1,num2))
    
        elif choice.lower() in ('m','multiply','multiplication'):
            print('Result: {} * {} = '.format(num1,num2),multiply(num1,num2))
    
        elif choice.lower() in ('d', 'divide', 'division'):
            print('Result: {} / {} = '.format(num1,num2),divide(num1,num2))
    
    else:
        print('Please input a correct choice')


    next_calculation = input("Want to do another calculation? (yes/no): ")
    if next_calculation.lower() in ['no', 'n', 'nope']:
        break
