"""
Calculator program for basic arithmetic operations

The user is prompted to enter 2 numbers, and then to specify an operation.
A result is printed, then the user is asked if they want to make another
operation.

The program currently has three language options: English, Portuguese,
and French. These can be selected by editing the LANGUAGE constant in line 16,
using ISO 639 language codes
"""
import json

with open('calculator_messages.json', 'r') as file:
    MESSAGES = json.load(file)

LANGUAGE = 'en'

def messages(message, lang):
    return MESSAGES[lang][message]

def prompt(key):
    message = messages(key, LANGUAGE)
    print(f'==> {message}')
    return message

def invalid_number(number_str):
    try:
        float(number_str)
    except ValueError:
        return True

    return False

prompt('welcome')


keep_going = True

while keep_going:

    prompt('first_num')

    number1 = input()

    while invalid_number(number1):
        prompt("invalid_num")
        number1 = input()

    prompt("second_num")

    number2 = input()

    while invalid_number(number2):
        prompt("invalid_num")
        number2 = input()

    prompt("operation")

    operation = input()

    while operation not in ["1", "2", "3", "4"]:
        prompt("invalid_operation")

        operation = input()

    match operation:
        case '1':
            output = float(number1) + float(number2)
        case '2':
            output = float(number1) - float(number2)
        case '3':
            output = float(number1) * float(number2)
        case '4':
            output = float(number1) / float(number2)

    print(f'==> {messages("result", LANGUAGE).format(output=output)}')

    prompt("another_operation")

    answer = input().casefold()

    while answer.casefold() not in ['no'.casefold(), 'Yes'.casefold()]:
        prompt("invalid_op")

        answer = input().casefold()

    if answer == 'Yes'.casefold():
        continue
    if answer == 'No'.casefold():
        prompt("end")

        break
