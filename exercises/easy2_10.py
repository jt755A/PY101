# text, no function
# input: ask for user age; age they want to retire
# output: displays when user retires; how many years until then

# requirement: get current year
import datetime

year = datetime.date.today().year

age = int(input("What is your age? "))
retirement_age = int(input("At what age would you like to retire? "))

years_left = retirement_age - age

print(f"It's {year}. You will retire in {year + years_left}.")
print(f"You only have {years_left} years of work to go!")