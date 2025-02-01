a = 42
b = 42
c = a

print(id(a) == id(b) == id(c))

# xyz       ==   xys  == id(new variable)
#   True              ==  ...
# False


# Wrong: it's True.
# Interning from -5 - 256
# Each variable points to same object in memory