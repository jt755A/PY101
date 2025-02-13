# Function

# input: year (integer)
# output: century (a string with 'st', 'nd', etc)

# requirement: new century begins in year ending 01.
# separate variables for
    # century number
    # suffix string


# convert to string
# check if length string_number < 3
    # prepend zero in for loop
    # for number range('0' to length of string_number)
        # prepend '0'
    
# century
    # slice string from before/after last 2 digits
        # convert to integer
        # 'century' is left side
        # 'year' is right side
        # if year > 0
            # century = century + 1

# suffix
    # match last digit of century
    #   # case 1:
    #       # 'st'
    #   # case 2:
    #       # 'nd'
    #   # case 3:
    #       # 'rd'
    #   # case _:
    #       # 'th'    

# combine century + suffix


def leading_zeroes(year):
    string_year = str(year)
    
    if len(string_year) < 3:
        string_year = ('0' * (3 - len(string_year))) + string_year

    return string_year

def num_century(year):
    string_year = leading_zeroes(year)
    left_number = string_year[:-2]
    right_number = string_year[-2:]
    if int(right_number) == 0:
        century = int(left_number)
    else:
        century = int(left_number) + 1
    return century

def suffix(year):
    century = str(num_century(year))

    if len(century) == 1 or century[-2] != '1':

        match century[-1]:
                case '1':
                    return 'st'
                case '2':
                    return 'nd'
                case '3':
                    return 'rd'
                case _:
                    return 'th'
            
    return 'th'
    # for X10th, X11th ... X19th centuries

    
def century(year):
    result = f'{num_century(year)}{suffix(year)}'
    return result


# print(repr(century_string(2000)) )
# print(repr(century_string(2001)) )
# print(repr(century_string(1965)) )
# print(repr(century_string(256)) )
# print(repr(century_string(5)) )
# print(repr(century_string(10103)) )
# print(repr(century_string(1052)) )
# print(repr(century_string(1127)) )
# print(repr(century_string(11201)) )


# print(num_century(5))
# print(num_century(10))
# print(num_century(1100))
# print(num_century(11510))

print(century(2000) == "20th")          # True
print(century(2001) == "21st")          # True
print(century(1965) == "20th")          # True
print(century(256) == "3rd")            # True
print(century(5) == "1st")              # True
print(century(10103) == "102nd")        # True
print(century(1052) == "11th")          # True
print(century(1127) == "12th")          # True
print(century(11201) == "113th")        # True



