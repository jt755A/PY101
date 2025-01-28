str1 = "Come over here!"
str2 = "What's up, Doc?"
str3 = '!'


def ends_exclamation(text):
    # return True if text.endswith('!') else False
    # return True if text[-1] == '!' else False
    if text.endswith('!'):
        return True
    else:
        return False


print(ends_exclamation(str1))
print(ends_exclamation(str2))
print(ends_exclamation(str3))










# How can you determine whether a given string ends with an exclamation
# mark (!)? Write some code that prints True or False depending on whether
# the string ends with an exclamation mark.