# function
# input: a string
# outputs: penultimate word


# get a string
# split into words
# return 2nd to last word



def penultimate(string):
    while len(string.split()) == 1 or len(string) == 0:
        # for empty + one word strings
        string = input('Please enter a string with multiple words: ')
    return string.split()[-2]


print(penultimate(input('Enter a string: ')))

# print(penultimate('hello world of people'))

# # These examples should print True
# print(penultimate("last word") == "last")
# print(penultimate("Launch School is great!") == "is")