numbers = [1, 2, 3, 4, 5, 15, 16, 17, 95, 96, 99]

number1 = 8  # False (not in numbers)
number2 = 95 # True (in numbers)

def in_lst(number, lst):
    # if number in lst:
    #     return True
    # else:
    #     return False
    return True if number in lst else False

    
print(in_lst(number1, numbers))
print(in_lst(number2, numbers))

# Given a number and a list, determine whether the number is included
# in the list.