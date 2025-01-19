def outer():
    outer_var = 'Hello'

    def inner():
        inner_var = 'World'
        print(outer_var, inner_var)

    inner()

outer()

# What will the following code print and why?

# It will print 'Hello World'.

# Line 10 calls outer(), this initializes outer_var to 'Hello' and defines inner.
# inner is called in line 8 which initializes inner_var to 'World'.
# inner has access to outer_var because it is a nested function within
# outer's function block. So line 6 is able to execute without an error.

# CORRECT