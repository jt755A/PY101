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


prompt("What is the loan amount? ($)")
loan_amount = input().strip('$').replace(' ', '') # removing dollar sign and spaces from input
if ',' in loan_amount:           # removing commas, if any
    loan_amount = loan_amount.replace(',', "")

while invalid_number(loan_amount):
    prompt("That looks like an invalid number")
    loan_amount = input().strip('$').replace(' ', '').replace(',', '')


prompt("What is the Annual interest rate? (Please enter the %)")
apr = input()

while invalid_number(apr.strip('%')):
    prompt("That looks like an invalid number")
    apr = input()

apr = apr.strip('%') # removing % symbol
apr = float(apr) / 100 # final figure

monthly_interest_rate = apr / 12

prompt("What is the loan duration? (In years or months)")
loan_length = input()

while invalid_number(loan_length):
    prompt("That looks like an invalid number")
    loan_length = input()

prompt("Is the loan duration in:\n1) Years 2) Months?")
time_unit = input()

while time_unit not in ['1', '2']:
    prompt("You must choose 1 or 2")
    time_unit = input()


# if time_unit == '1':
#     loan_months = float(loan_length) * 12

# elif time_unit == '2':
#     loan_months = float(loan_length)

match time_unit:
    case '1':
        loan_months = float(loan_length) * 12
    case '2':
        loan_months = float(loan_length)



if apr == 0:
    monthly_payment = float(loan_amount) / loan_months
else:
    monthly_payment = (
        float(loan_amount)
                       * (monthly_interest_rate
                          / (1 - (1 + monthly_interest_rate) ** (-loan_months))
                          )
                          )
rounded_payment = round(monthly_payment, 2)

prompt(f'Your monthly payment is ${rounded_payment}')
