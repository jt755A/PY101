# middle character

# input: non-empty string arg

# out: returns middle charcter
    # if odd: middle character
    # if even: middle two characters


# given a string argument
    # if length of string is odd:
        # set 'start index' = length // 2
    # if even:
        # set 'start index' = length // 2
        # slice 2 characters

# START

# given text string str

# if length string is odd:
    # SET start_index = length(string) // 2


def center_of(text):
    start_idx = len(text) // 2
    if len(text) == 1:
        return text[start_idx]
    elif len(text) % 2 != 0:
        return text[start_idx]
    else:
        return text[start_idx - 1:start_idx + 1]

# print(center_of('I Love Python!!!'))
# print(center_of('x'))
# print(center_of('hello'))


print(center_of('I Love Python!!!') == "Py")    # True
print(center_of('Launch School') == " ")        # True
print(center_of('Launchschool') == "hs")        # True
print(center_of('Launch') == "un")              # True
print(center_of('Launch School is #1') == "h")  # True
print(center_of('x') == "x")                    # True