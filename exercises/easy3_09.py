import pdb

# function

# input: a string (that contains alpha + non-alphabetic characters (incl whitespace)

# output: string with non-alpha characters replaced by space
    # no consecutive spaces
        # from non-alpha characters (including whitespace)


# given a string
    # intialize 'result' as  empty string
    # iterate over each character of arg
        # if character is alphabetic
            # result = result + character
        # else
            # if last character of result is space
                # continue
            # else
                # result = result + space
        # 

# START
# given a string 'text'

# SET result = empty string

# FOR character in text
    # IF character is alphabetic
        # result = result + character
    
    # IF last character of result = ' '
        # CONTINUE

    # SET result = result + ' '

# RETURN result

# END

# do for loop, skip until you reach an alpha character
    # insert space
    # insert alpha







# def clean_up(text):
#     result = ''
#     for idx in range(len(text)):
#         if not text[idx].isalpha():
#             # pdb.set_trace()
            
#             iterator = 1
            
#             while idx + iterator < len(text):
#                 if not text[idx + iterator].isalpha():
#                     iterator += 1

#                 result += ' '
#                 break
                
#         result += text[idx]        

#     return result

# def clean_up(text):
#     result = ''
#     for idx in range(len(text)):
#         if text[idx].isalpha():
#             result += text[idx]
        
#         else:
#             try:
#                 result[-1].isalpha()

#             except IndexError:
#                 # for idx == 0
#                 result += ' '
#                 continue

#             if result[-1] == ' ':
#                 continue

#             result += ' '

#     return result


def clean_up(text):
    result = ''
    for idx in range(len(text)):
        if text[idx].isalpha():
            result += text[idx]
        
        elif idx == 0 or result[-1] != ' ':
            result += ' '

    return result





print(clean_up("---what's my +*& line?"))

print(clean_up("---what's my +*& line?") == " what s my line ")
# True



# 2nd approach
# split string at non-alpha characters
# filter to only contain alpha strings
# join with space

# problem: if first/last character is non-alpha, there won't be a space?