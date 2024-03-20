"""
Программа калькулятор ...
"""

def input_operation():
    operations = {'+', '-', '*', '/'}
    while True:
        operation = input('Enter the operation: ')
        if operation not in operations:
            print('Go home yankee, eeeii')
            continue
        break
    return operation

def info():
    print('simple calculator')

def input_number(step):
    while True:
        number = input(f'Enter {step} number:')
        
        if not number.isdigit():
            print('It is not number, again')
            continue

        break    
    return number

def main():
    info()
    number_one = input_number('1st')
    number_two = input_number('2nd')    
    operation = input_operation()
    print (f'{number_one} {operation} {number_two} = результат')

if __name__ == '__main__':
    main()