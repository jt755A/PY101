import json

with open('calculator_messages.json', 'r') as file:
    MESSAGES = json.load(file)

LANGUAGE = 'en'

# def prompt(message):
#     print(f"==> {message}")

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
    
# prompt('Welcome to Calculator!')

# prompt(MESSAGES[LANGUAGE]["welcome"])
prompt('welcome')


keep_going = True

while keep_going:

    # prompt("What's the first number?")
    # prompt(MESSAGES["first_num"])
    prompt('first_num')


    number1 = input()

    while invalid_number(number1):
        # prompt("Hmm... that doesn't look like a valid number.")
        # prompt(MESSAGES["invalid_num"])
        prompt("invalid_num")


        number1 = input()

    # prompt("What's the second number?")
    # prompt(MESSAGES["second_num"])
    prompt("second_num")

    number2 = input()

    while invalid_number(number2):
        # prompt("Hmm... that doesn't look like a valid number.")
        # prompt(MESSAGES["invalid_num"])
        prompt("invalid_num")


        number2 = input()
        

    # prompt("""What operation do you want to perform?
    # 1) Add 2) Subtract 3) Multiply 4) Divide""")
    # prompt(MESSAGES["operation"])
    prompt("operation")

    operation = input()

    while operation not in ["1", "2", "3", "4"]:
        # prompt('You must choose 1, 2, 3, or 4')
        # prompt(MESSAGES["invalid_operation"])
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

    # prompt(f'The result is: {output}')
    # prompt(MESSAGES["output"]); prompt(output)
    # prompt("result")

    # Using prompt() function would result in double-printing if
    # passed to print function
    print(f'==> {messages("result", LANGUAGE).format(output=output)}')


    # prompt(f"Do you want to perform another calculation?"
    # "\nEnter 'Yes or no'")
    # prompt(MESSAGES["another"])
    prompt("another_operation")

    answer = input().casefold()

    while answer.casefold() not in ['no'.casefold(), 'Yes'.casefold()]:
        # prompt('You must choose Yes or no.')
        # prompt(MESSAGES["invalid_op"])
        prompt("invalid_op")


        answer = input().casefold()
    
    if answer == 'Yes'.casefold():
        continue
    if answer == 'No'.casefold():
        # prompt('End of calculation!')
        # prompt(MESSAGES["end"])
        prompt("end")

        break



# Ask the user for the first number.
# Ask the user for the second number.
# Ask the user for an operation to perform.
# Perform the operation on the two numbers.
# Print the result to the terminal.