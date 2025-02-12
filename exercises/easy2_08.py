# write function returns a list
# that contains every other element of a list that is passed in as argument.
# returned list contains 1st, 3rd, 5th etc elements of argument list.

# input: list
# requirement: only 1 argument

# output: returns a list

# given a list as argument

    # iterate over every element in list
        # initialize an empty 'result' list
        # set an iterator
        # for each iteration, check if iterator is odd number
            # if odd:
                # add element at iterator index to result list
            # otherwise, move on to next value
    # return result list


# START

# given a list called 'lst'

# SET result = []
# SET iterator = 1

# WHILE iterator <= length of lst
    # IF iterator == odd number
        # result = result + element at index[iterator]

    # iterator = iterator + 1

# return result

def oddities(lst):
    result = []
    idx = 1
    while idx <= len(lst):
        if idx % 2 != 0:
            result.append(lst[idx - 1])

        idx += 1

    return result

def evens(lst):
    result = []
    idx = 0
    while idx < len(lst):
        if idx % 2 != 0:
            result.append(lst[idx])
    return result


# print(oddities([2, 3, 4, 5, 6]))

import copy
import pdb

# INCORRECT
# def oddities(lst):
#     result = copy.deepcopy(lst)
#     for idx in range(1, len(lst) + 1):
#         if idx % 2 == 0:
#             result.pop(0)
#             pdb.set_trace()
#     return result

# print(oddities([2, 3, 4, 5, 6]))


# list slicing

# # input lst
# output: [::2]

def oddities2(lst):
    result = lst[::2]
    return result


        
# print(oddities([2, 3, 4, 5, 6]) == [2, 4, 6])  # True
# print(oddities([1, 2, 3, 4]) == [1, 3])        # True
# print(oddities(["abc", "def"]) == ['abc'])     # True
# print(oddities([123]) == [123])                # True
# print(oddities([]) == [])                      # True

print(oddities2([2, 3, 4, 5, 6]))

print(oddities2([2, 3, 4, 5, 6]) == [2, 4, 6])  # True
print(oddities2([1, 2, 3, 4]) == [1, 3])        # True
print(oddities2(["abc", "def"]) == ['abc'])     # True
print(oddities2([123]) == [123])                # True
print(oddities2([]) == [])                      # True


            