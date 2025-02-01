print(0.3 + 0.6)
# prints 0.9
print(0.3 + 0.6 == 0.9)
# Throws TypeError?: 0.3 + False. False not float type.
# Incorrect: arithmetic operations have higher precedence than
# comparisons/identity tests

# prints True


# Both wrong: floating point computation is imprecise.

# import math. Use math.isclose()