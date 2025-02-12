# input: ask for name
# output:
    # if endswith !:
        # capitalize the name and return caps greeting
    # else print greeting name

name = input("What is your name? ")

if name.endswith('!'):
    print(f'HELLO {name.upper()} WHY ARE WE YELLING?')
else:
    print(f'Hello {name}.')