# input: string supplied to function
# output: sum of UTF-16 values of all characters

# get string from input to function
# set tally to 0
# iterate over each character in string
    # Get UTF-16 value of character
    # add to tally
# return result

def utf16_value(text):
    tally = 0
    for char in text:
        tally += ord(char)
    return tally

print(utf16_value('Four score') == 984)
print(utf16_value('Launch School') == 1251)
print(utf16_value('a') == 97)
print(utf16_value('') == 0)

OMEGA = "\u03A9"

print(utf16_value(OMEGA) == 937)
print(utf16_value(OMEGA + OMEGA + OMEGA) == 2811)