import pdb

# function

# input: positive integer, n, as argument
# output: prints a right angled triangle: each side has n *
    # hypotenuse goes from bottom left to top right

#   *
#  **
# ***

# first line: has n-1 spaces (' ') then *
# subsequent lines have n - (line#) spaces, then (line# x *)

# given n
    # SET line_no = 1
    # WHILE line_no <= n
        # SET spaces = (n - line_no) * ' '
        # PRINT (spaces) + (line_no * '*')
        # line_no = line_no + 1

def triangle(n):
    line_no = 1
    while line_no <= n:
        spaces = (n - line_no) * ' '
        print(spaces + (line_no * '*'))
        line_no += 1

# triangle(3)
triangle(3)

