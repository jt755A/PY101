import pdb
# function

# input: positive(?) integer
# output: returns input * 2, unless input is double-number
    # double number is even-LENGTH number where 1st half is identical to
    # right half. e.g. 103103

# given integer argument
    # convert arg to string
    # determine if num is double number
        # if length even AND start:mid-point = mid-point:end
            # return num
    # else, num * 2

# START

# given integer argument [we are excluding empty strings]

# SET num to integer of argument
# IF num has even length AND first half == second half (slice start to midpoint, midpoint + 1 - end)
    # RETURN num
# ELSE
    # RETURN num * 2

def twice(num):
    num_string = str(num)
    midpoint = len(num_string) // 2
    
    # if len(num_string) % 2 != 0:
    #     return num * 2
    
    # elif num_string[:midpoint] != num_string[midpoint:]:
    #     return num * 2

    if (
        (len(num_string) % 2 == 0) and
        (num_string[:midpoint] == num_string[midpoint:])
        ):
            return num
    
    return num * 2  
    # return num

# my solution works but is too complicated.
# functions should only do one thing: i.e. I should make a separate
# is_double_number func

# if that helper function returns a boolean, the main function can just
# use an if function that does/doesn't execute accordingly.


# LS solution

def is_double_number(number):
    string_number = str(number)
    center = len(string_number) // 2
    left_number = string_number[:center]
    right_number = string_number[center:]

    return left_number == right_number

def twice(number):
    if is_double_number(number):
        return number
    else:
        return number * 2

print(twice(37) == 74)                  # True
print(twice(44) == 44)                  # True
print(twice(334433) == 668866)          # True
print(twice(444) == 888)                # True
print(twice(107) == 214)                # True
print(twice(103103) == 103103)          # True
print(twice(3333) == 3333)              # True
print(twice(7676) == 7676)              # True
