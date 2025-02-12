# inputs 2 args: string, positive num

# output: prints string x positive num times

# START

# idx = num
# WHILE idx > 0
    # PRINT num
    # idx = idx - 1

# END

# def repeat(text, times):
#     idx = times
#     while idx > 0:
#         print(text)
#         idx -= 1

def repeat(text, times):
    for _ in range(times):
        print(text)


repeat('Hello', 3)