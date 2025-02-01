def factors(number):
    divisor = number
    result = []
    while divisor != 0:
        if number % divisor == 0:
            result.append(number // divisor)
        
        if divisor > 0:
                divisor -= 1
        elif divisor < 0:
                divisor += 1
    return result

# print(factors(21))
print(factors(-21))

# Fixing infinite loop when input is a negative number


# Bonus Q: What is the purpose of number % divisor == 0 in that code?

# This checks whether the number divides by divisor without a remainder:
# i.e. clean integer division.