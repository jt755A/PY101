# function

# input: 1 arg: positive integer
# output: returns STRING of alternating 1's and 0's. Starting on 1.
    # length of string matches integer

# given an integer
    # start with empty string
    # set an iterator.
    # iterator up to arg
    # if iterator is odd, reassign concatenate a string '1'
    # if iterator is even, reassign concatenate a string '0'

# START

# Given an integer argument

# SET iterator = 1
# SET result = ''
# FOR iterator in RANGE(0 - argument)
    # IF iterator is even
        # result = result + '1'
    # ELSE
        # result = result + '0'
# RETURN result


def stringy(size):
    result = ''
    for idx in range(size):
        if idx % 2 == 0:
            result += '1'
        else:
            result += '0'
    
    return result

# EDIT (neater using helper function + ternary expression)
# note that digit is used, because result += is used in each case. makes logic
# a little clearer

def string(size):
    result = ""
    for idx in range(size):
        digit = '1' if idx % 2 == 0 else '1'
        result += digit
    
    return result


print(repr(stringy(1)))
print(repr(stringy(2)))

print(repr(stringy(6)))
print(repr(stringy(9)))
print(repr(stringy(4)))
print(repr(stringy(7)))


print(stringy(6) == "101010")           # True
print(stringy(9) == "101010101")        # True
print(stringy(4) == "1010")             # True
print(stringy(7) == "1010101")          # True