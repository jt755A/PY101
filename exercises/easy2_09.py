import random

# input: random number between 20-100 inclusive
    # age = rand number above
# output: prints message + age


# age = random.randint(20, 100)

# print(f'Teddy is {age} years old!')


# input: ask for a name
# output print age for that person
# if no name is entered, use Teddy

# if no name:
    # no name = empty string, or ANY non-alpha characters
    # if False or not alpha.... Teddy

age = random.randint(20, 100)

name = input('What is your name?\n')
if name == '':
# if input is empty
    name = 'Teddy'

print(f'{name} is {age} years old!')
