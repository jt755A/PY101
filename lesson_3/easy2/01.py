numbers = [1, 2, 3, 4, 5]

rev1 = list(reversed(numbers))

print(rev1)
print(numbers)


rev2 = []
for number in numbers[::-1]:
    rev2.append(number)

print(rev2)
print(numbers)

# Write two distinct ways of reversing the list without mutating the
# original list.