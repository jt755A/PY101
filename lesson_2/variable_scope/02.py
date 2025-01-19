num = 5

def my_func():
    num = 10

my_func()
print(num)

# What will the following code print and why?

# It will print 5.
# Line 7 can only access variables within its own scope: the global scope.
# num in line 1 is defined in the global scope and is accessible to print().

# myfunc() creates a local variable named num set to a value of 10. This is
# independent of num in line 1, and not accessible within the global scope.

# CORRECT