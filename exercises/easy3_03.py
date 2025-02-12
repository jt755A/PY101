# function
# input: text string
# outputs text in box
    # 1st line: + --- +
    # 2nd line: space
    # 3rd line: text
    # a space on either side of text ' '
    # penultimate: space
    # final: same as 1st


# get length of text

# concatenate '+' then '-' lenth number of times

# def print_in_box(text):
#     def line():
#         return len(text)
    
#     print('+' + ('-' * (line() + 2)) + '+')
#     print('|' + (' ' * (line() + 2)) + '|')
#     print('| ' + text + ' |')
#     print('|' + (' ' * (line() + 2)) + '|')
#     print('+' + ('-' * (line() + 2)) + '+')

def print_in_box(message):
    horizontal_line = f'+-{"-" * len(message)}-+'
    empty_line = f'| {' ' * len(message)} |'

    print(horizontal_line)
    print(empty_line)
    print(f'| {message} |')
    print(empty_line)
    print(horizontal_line)


print_in_box('hello')
        
