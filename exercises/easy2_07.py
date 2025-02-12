# Write xor function

# inputs: 2 arguments
# outputs: returns True, or False

# program: checks if argument is truthy

# step1: if conditional. Will execute if boolean evaluates as truthy
    # if arg1 is truth AND arg2 is falsy -
    # elif check if arg2 is truthy AND arg1 is falsy
    # else False

def xor(arg1, arg2):
    if arg1 and not arg2:
        return True
    elif arg2 and not arg1:
        return True
    else:
        return False
    

# neater solution

def xor(value1, value2):
    if (value1 and not value2) or (value2 and not value1):
        return True
    
    return False

# even neater

def xor(value1, value2):
    return bool((value1 and not value2) or (value2 and not value1))


print(xor(5, 0) == True)
print(xor(False, True) == True)
print(xor(1, 1) == False)
print(xor(True, True) == False)




# Does the xor function perform short-circuit evaluation of its operands?
# Why or why not? Does short-circuit evaluation in xor operations
# even make sense?

# Answer: no. The definition of an xor operation is that it evaluates
# both operands. It is not possible to short circuit, as it must evaluate
# the 2nd operand in every case.