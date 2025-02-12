# Square

import pdb

def multiply(num1, num2):
    return num1 * num2

# def square(num):
#     return multiply(num, num)



# print(square(5) == 25)
# print(square(-8) == 64)


# power to the n
# runs multiply(number, number) n-1 times
# use a counter and while loop

def power_to_n(number, n):
    counter = 1
    tally = 1
    
    while counter <= n:
        tally = multiply(number, tally)
        counter += 1

    return tally

print(power_to_n(3, 1))