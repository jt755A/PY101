# function input: 2 argument.
    # List: 2 or more elements
    # dict: 2 keys

# output: returns an f- string

# joins all elements of list in arg1
# accesses values of 2 keys in dict

# def greetings(name_lst, title_occup_dct):
#     name = ' '.join(name_lst)
#     title = tuple(title_occup_dct.values())
#     return f'''Hello, {name}! Nice to have a {title[0]} {title[1]} around.'''

def greetings(name, status):
    return (f"Hello, {' '.join(name)}! Nice to have a {status['title']} "
            f"{status['occupation']} around.")


greeting = greetings(
    ["John", "Q", "Doe"],
    {"title": "Master", "occupation": "Plumber"},
)







print(greeting)
# Hello, John Q Doe! Nice to have a Master Plumber around.