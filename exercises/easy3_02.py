# function

# input: string argument

# output: string: all CONSECUTIVE characters, replaced with 1 

# iterate and reassignment

# assign first letter to new string
# if next character of arg = last character of new
    # skip
# else:
    # new string + character

# given text string
    #  

# FOR character in arg in range (length of string)
    # IF character = last character of result
        # pass
    # else
        # result = result + character

    # RETURN result

def crunch(text):
    if len(text) == 0:
        return ''
    else:
        result = text[0]
        for _ in range(len(text)):
            if text[_] == result[-1]:
                continue
            else:
                result = result + text[_]
        
        return result

print(crunch('ddaaiillyy ddoouubbllee'))

# These examples should all print True
print(crunch('ddaaiillyy ddoouubbllee') == 'daily double')
print(crunch('4444abcabccba') == '4abcabcba')
print(crunch('ggggggggggggggg') == 'g')
print(crunch('abc') == 'abc')
print(crunch('a') == 'a')
print(crunch('') == '')