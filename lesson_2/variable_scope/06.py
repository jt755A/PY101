def my_func():
    x = 15

    def inner_func1():
        x = 25
        print("Inner 1:", x)

    def inner_func2():
        print("Inner 2:", x)

    inner_func1()
    inner_func2()

my_func()

# What will the following code print and why?

# It will print:
# "Inner 1: 25"
# "Inner 2: 15"

# inner_func1 creates a local variable x in line 5. Line 6 will access this
# value in its call to print.
# inner_func2 has no reassignment, so it will access the x variable
# defined in line 2 in the my_func block.

# CORRECT