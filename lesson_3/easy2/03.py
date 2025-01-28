start_rng = 10
end_rng = 100

num1 = 42
num2 = 100
num3 = 101

def in_incl_rng(num, start_rng, end_rng):
    if num in range(start_rng, end_rng + 1):
        return True
    else:
        return False
    
print(in_incl_rng(num1, start_rng, end_rng))
print(in_incl_rng(num2, start_rng, end_rng))
print(in_incl_rng(num3, start_rng, end_rng))

# Programmatically determine whether 42 lies between 10 and 100, inclusive.
# Do the same for the values 100 and 101.