# Mortage Calculator

def prompt(message):
    print(f'--> {message}')

def invalid_number(number_str):  # checks non-numeric + negative values
    try:
        float(number_str)
    except ValueError:
        return True
    if float(number_str) < 0:
        return True

    return False

def invalid_length(number_str):  # checks non-numeric, 0, and negative values
    try:
        float(number_str)
    except ValueError:
        return True
    if float(number_str) <= 0:
        return True

    return False

while True:

    prompt("Welcome to the Mortgage/Loan Calculator!\n")

    prompt("What is the loan amount? ($)")

    # removing dollar sign, spaces, and commas from input, if any
    loan_amount = input().strip('$').replace(' ', '').replace(',', '')

    while invalid_number(loan_amount):
        prompt("That looks like an invalid number. Enter a positive number!")
        loan_amount = input().strip('$').replace(' ', '').replace(',', '')

    loan_amount = float(loan_amount)

    prompt("What is the Annual interest rate? (Please enter the %)")
    apr = input()

    while invalid_number(apr.strip('%')):
        prompt("That looks like an invalid number. Enter a positive number!")
        apr = input()

    apr = apr.strip('%') # removing % symbol
    apr = float(apr) / 100 # final figure
    monthly_interest_rate = apr / 12

    prompt("Is the loan duration specified in:\n1) Years 2) Months?")
    time_unit = input()

    while time_unit not in ['1', '2']:
        prompt("You must choose '1' (years) or '2' (months)")
        time_unit = input()

    match time_unit:
        case '1':
            unit = 'years'
        case '2':
            unit = 'months'

    prompt(f"How many {unit}?")
    loan_length = input()

    while invalid_length(loan_length):
        prompt("That looks like an invalid number. Enter a positive number!")
        loan_length = input()

    match time_unit:
        case '1':
            loan_months = float(loan_length) * 12
        case '2':
            loan_months = float(loan_length)

    if apr == 0:
        monthly_payment = loan_amount / loan_months
    else:
        monthly_payment = (loan_amount * (monthly_interest_rate
                            / (1 - (1 + monthly_interest_rate)
                               ** (-loan_months)))
                            )
    rounded_payment = round(monthly_payment, 2)

    prompt(f'Your monthly payment is ${rounded_payment}')

    prompt("Would you like to make another calculation?")
    another_answer = input().casefold()

    while True:
        if another_answer.startswith('y') or another_answer.startswith('n'):
            break

        prompt('Please enter "y" or "n"')
        another_answer = input().casefold()

    if another_answer[0] == 'n':
        prompt("Thank you for using the Mortgage/Loan calculator!")
        break
