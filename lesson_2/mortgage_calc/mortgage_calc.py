# Mortage Calculator
import os
import math

def prompt(message):
    print(f'--> {message}')


def invalid_loan(number_str):  # checks non-numeric, 0 and negative values
    try:
        float(number_str)
    except ValueError:
        return True
    if (float(number_str) <= 0
        or not math.isfinite(float(number_str))):

        return True

    return False


def invalid_rate(number_str):  # checks non-numeric + negative values
    try:
        float(number_str)
    except ValueError:
        return True
    if (float(number_str) < 0
        or not math.isfinite(float(number_str))):
        return True

    return False


def invalid_length(number_str):  # checks non-numeric, 0, and negative values
    try:
        int(number_str)
    except ValueError:
        return True
    if (float(number_str) <= 0
        or not math.isfinite(float(number_str))):
        return True

    return False


def get_loan_amount():
    prompt("What is the loan amount? ($)")

    # removing dollar sign, spaces, and commas from input, if any
    loan = input().strip('$').replace(' ', '').replace(',', '')

    while invalid_loan(loan):
        prompt("That looks like an invalid number. Enter a positive number!")
        loan = input().strip('$').replace(' ', '').replace(',', '')

    loan = float(loan)
    return loan


def get_monthly_interest_rate():
    prompt("What is the Annual interest rate? (Please enter the %)")
    apr = input()

    while invalid_rate(apr.strip('%')):
        prompt("That looks like an invalid number. Enter a positive number!")
        apr = input()

    apr = apr.strip('%') # removing % symbol
    apr = float(apr) / 100 # final figure
    rate_monthly = apr / 12
    return rate_monthly


def get_time_unit():
    prompt("Is the loan duration specified in:\n1) Years 2) Months?")
    time_unit = input()

    while time_unit not in ['1', '2']:
        prompt("You must choose '1' (years) or '2' (months)")
        time_unit = input()

    match time_unit:
        case '1':
            time_unit = 'years'
            return time_unit
        case '2':
            time_unit = 'months'
            return time_unit


def get_loan_duration(time_unit):
    prompt(f"How many {time_unit}?")
    loan_length = input()

    while invalid_length(loan_length):
        prompt("That looks like an invalid number. Enter a positive number!")
        loan_length = input()

    match time_unit:
        case 'years':
            month_no = float(loan_length) * 12
            return month_no
        case 'months':
            month_no = float(loan_length)
            return month_no


def calculate_monthly_pay(loan, rate, months):
    if rate == 0:
        monthly_pay = loan / months
    else:
        monthly_pay = (loan * (rate / (1 - (1 + rate) ** (-months))))
    return monthly_pay


def calculate_again():
    prompt("Would you like to make another calculation?")
    answer = input().casefold()

    while True:
        if answer in ['yes', 'no', 'y', 'n']:
            return answer

        prompt('Please enter "y" or "n"')
        answer = input().casefold()

def calculator():

    while True:

        os.system('clear')
        prompt("Welcome to the Mortgage/Loan Calculator!\n")

        loan_amount = get_loan_amount()
        monthly_interest_rate = get_monthly_interest_rate()
        unit = get_time_unit()
        loan_months = get_loan_duration(unit)

        monthly_payment = calculate_monthly_pay(loan_amount, monthly_interest_rate, loan_months)
        prompt(f'Your monthly payment is ${monthly_payment:.2f}')

        another_answer = calculate_again()

        if another_answer[0] == 'n':
            prompt("Thank you for using the Mortgage/Loan calculator!")
            break

calculator()
