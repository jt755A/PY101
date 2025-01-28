ages = {'Herman': 32, 'Lily': 30, 'Grandpa': 5843, 'Eddie': 10}
additional_ages = {'Marilyn': 22, 'Spot': 237}

# for key, value in additional_ages.items():
#     ages[key] = value

# ages.update(additional_ages)

ages |= additional_ages


print(ages)

# We have most of the Munster family in our ages dictionary:
# Add entries for Marilyn and Spot to the dictionary: