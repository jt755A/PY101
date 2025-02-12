# Write a function that takes one integer argument
# and returns True when the number's absolute value is odd, False otherwise.


# Given an integer argument
# Calculate absolute value of arg
# If odd: return True
# If not: return False

def is_odd(integer):
    if abs(integer) % 2 != 0:
        return True
    return False

print(is_odd(0))
print(is_odd(2))
print(is_odd(-2))
print(is_odd(-3))
print(is_odd(-5))
print(is_odd(5))



