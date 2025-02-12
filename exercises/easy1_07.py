# Write a function that takes two strings as arguments, determines the length
# of the two strings, and then returns the result of concatenating the
# shorter string, the longer string, and the shorter string once again.
# You may assume that the strings are of different lengths.

# inputs: 2 arguments to function

# output: RETURN concatentation of short, long, short
# requirements: any string, incl empty ('')

# empty array
# 

# determine length of string1
# determine length of string2

# if len(str1) shorter than len(str2):
    # array + str1
# else:
    # array str2 

# make ordered array of strings by length, ascending

# concat array[0][1][0]




def short_long_short(str1, str2):
    if len(str1) < len(str2):
        return str1 + str2 + str1
    elif len(str1) > len(str2):
        return str2 + str1 + str1
    
print(short_long_short('abc', 'defgh'))
print(short_long_short('abcde', 'fgh'))
print(short_long_short('', 'xyz'))