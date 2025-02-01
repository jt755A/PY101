# A

def mess_with_vars(one, two, three):
    one = two
    two = three
    three = one

one = ["one"]
two = ["two"]
three = ["three"]

mess_with_vars(one, two, three)

print(f"one is: {one}") # ["two"]
print(f"two is: {two}") # ["three"]
print(f"three is: {three}") # ["two"]???

# EDIT WRONG: local variables, don't affect global ones with same name


# B

def mess_with_vars(one, two, three):
    one = ["two"]
    two = ["three"]
    three = ["one"]

# Local variables: don't affect global ones

one = ["one"]
two = ["two"]
three = ["three"]

mess_with_vars(one, two, three)

print(f"one is: {one}")
print(f"two is: {two}")
print(f"three is: {three}")

# C

def mess_with_vars(one, two, three):
    one[0] = "two"
    two[0] = "three"
    three[0] = "one"

one = ["one"]
two = ["two"]
three = ["three"]

mess_with_vars(one, two, three)

print(f"one is: {one}") # ["two"]
print(f"two is: {two}") # ["three"]
print(f"three is: {three}") # ["one"]

# passing reference into function, mutates object reference. Affects global
# variable.