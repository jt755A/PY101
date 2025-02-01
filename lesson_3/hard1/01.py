def first():
    return {
        'prop1': "hi there",
    }

def second():
    return
    {
        'prop1': "hi there",
    }

print(first())
print(second())

# Will the following functions return the same results?

# Yes: both functions return a value-equal dict to the prnit function.

# EDIT: NO.

# second has return on its own line. I.e. the dict below it will never be
# evaluated or returned