# Ask the user for the first number.
# Ask the user for the second number.
# Ask the user for an operation to perform.
# Perform the operation on the two numbers.
# Print the result to the terminal.

print('Welcome to Calculator!')

print("What's the first number?")
number1 = int(input())

print("What's the second number?")
number2 = int(input())

print('What operation do you want to perform?'
'\n1) Add 2) Subtract 3) Multiply 4) Divide')
operation = input()

if operation == '1':   # '1' represents addition
    result = number1 + number2
elif operation == '2': # '2' represents subtraction
    result = number1 - number2
elif operation == '3': # '3' represents multiplication
    result = number1 * number2
elif operation == '4': # '4' represents division
    result = number1 / number2
else:
    print('Incorrect operation selected!')

print(f'The result is: {result}')