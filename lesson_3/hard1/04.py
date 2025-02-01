# def is_dot_separated_ip_address(input_string):
#     dot_separated_words = input_string.split(".")
#     while len(dot_separated_words) > 0:
#         word = dot_separated_words.pop()
#         if not is_an_ip_number(word):
#             break

#     return True



def is_an_ip_number(str_input):
    try:
        int(str_input)
    except TypeError:
        return False
    
    if 0 <= int(str_input) <= 255:
        return True
    else:
        return False

def is_dot_separated_ip_address(input_string):
    dot_separated_words = input_string.split(".")
    if len(dot_separated_words) != 4:
        return False
    
    while len(dot_separated_words) > 0:
        word = dot_separated_words.pop()
        if not is_an_ip_number(word):
            return False

    return True

# print(is_an_ip_number(input('Enter a ip number: ')))

# print(is_dot_separated_ip_address("1.2.55.65"))
print(is_dot_separated_ip_address(input("Enter an ip address: ")))

# works