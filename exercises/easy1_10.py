# inputs integer greater than 1

# output: returns sum of multiples of 3 and 5

# set result to []
# iterate over list in range from 1 TO chosen number
    # add to array if mult of 3 or 5
# sum the array

def multisum(chosen_num):
    rng = range(1, chosen_num + 1)
    result = []
    
    [result.append(num) for num in rng
    if num % 3 == 0 or num % 5 == 0]
    return sum(result)

# def multisum(chosen_num):
#     rng = range(1, chosen_num + 1)
#     mult = (3, 5)
#     result = []
#     [result.append(num) for num in rng
#     if any(num % mult == 0)]
#     return sum(result)

# how to iterate through tuple?

print(multisum(3))
print(multisum(8))
print(multisum(10))
print(multisum(1000))








# y = (3, 5)
# any