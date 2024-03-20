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
    return float(number)

def main():
    info()
    number_one = input_number('1st')
    number_two = input_number('2nd')    
    operation = input_operation()
    result = solve(number_one, number_two, operation)
    print_solve(number_one, number_two, operation, result)

def print_solve(number_one, number_two, operation, result):
    print (f'{number_one} {operation} {number_two} = {result}')


def solve(number_one, number_two, operation):
    result = None
    if operation == '+':
        result = number_one + number_two
    elif operation == '-':
        result = number_one - number_two
    elif operation == '*':
        result = number_one * number_two
    else:
        result = number_one / number_two
    return result

if __name__ == '__main__':
    main()


