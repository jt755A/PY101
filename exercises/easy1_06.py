# Write a program that asks the user to enter an integer greater than 0,
# then asks whether the user wants to determine the sum or the product of
# all numbers between 1 and the entered integer, inclusive.

# inputs:
    # integer greater than 0
    # choose sum or product

# output: return and print product

# Edges: 
    # non-integer: error validate
    # less than zero: error validate

# START

# GET numberChoice
# GET operationChoice

# SET range 1:numberChoice as array

# SET currentValue as first item
# FOR item in range:
    # currentValue = currentValue |OperationChoice| item
# SET result = currentValue

# PRINT currentValue

def invalid_num(number):
    try:
        int(number)
    except ValueError:
        return True
    if int(number) < 1:
        return True
    return False

number_choice = input("Please enter an integer greater than 0: ")

while invalid_num(number_choice):
    number_choice = input("That's not a valid choice."
                          "Please enter an integer. ")
number_choice = int(number_choice)

op_choice = input('Enter "s" to compute the sum,' \
                  'or "p" to compute the product. ').casefold()
while op_choice not in ['s', 'p']:
    print("That's not a valid choice." \
          " Please enter 's' for sum, or 'p' for product.")
    op_choice = input().casefold()
    

if op_choice == 's':
    operation = 'sum'
elif op_choice == 'p':
    operation = 'product'

match op_choice:
    case 's':
        result = number_choice
        for item in range(1, number_choice):
            result += item
    case 'p':
        result = number_choice
        for item in range(1, number_choice):
            result *= item
        

print(f'The {operation} of the integers between 1 and {number_choice} is {result}.')
        