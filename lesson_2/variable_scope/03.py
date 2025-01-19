num = 5

def my_func():
    global num
    num = 10

my_func()
print(num)

# What will the following code print and why?

# It will print 10.
# The global num statement in line 4 means that any reassignment in the
# function block will affect the variable in the global scope (i.e. it
# won't create an independent local variable named num).

# my_func is called, which reassigns num to 10. Line 8 prints this value.

# CORRECT