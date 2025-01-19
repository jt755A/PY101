def my_func():
    num = 10

my_func()
print(num)

# What will the following code do?

# This will throw a NameError: num is only accessible within the my_func
# function block. It is not available to the global block.
# The call to print in line 5 will cause an error to be thrown.

# CORRECT