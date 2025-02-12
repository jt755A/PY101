# input number

# output: negative if negative, negative if positive, 0 if 0

# def negative(num):
#     return num if num <= 0 else -(num)

# def negative(num):
#     if num <= 0:
#         return num
#     else:
#         return -num

# EDIT

def negative(num):
    return -abs(num)


print(negative(5) == -5)      # True
print(negative(-3) == -3)     # True
print(negative(0) == 0)       # True