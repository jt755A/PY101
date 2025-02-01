def foo(param="no"):
    return "yes"

def bar(param="no"):
    return (param == "no") and (foo() or "no")

bar(foo())

# returns False
# foo() returns "yes"

# bar("yes"):
# return (param == "no") and (foo() or "no"))
#            (False    ) and  ("yes" or "no")
#            False        and    True  (short circuits: yes is truthy)