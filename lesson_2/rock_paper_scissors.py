import random

VALID_CHOICES = ['rock', 'paper', 'scissors']

def prompt(message):
    print(f"===> {message}")

def display_winner(player, computer):
    prompt(f"You chose {player}, computer chose {computer}")

    if ((player == "rock" and computer == "scissors") or
        (player == "paper" and computer == "rock") or
        (player == "scissors" and computer == "paper")):
        # prompt("You win!")
        print("You win!")
        return "You win!"
    
    elif ((player == "rock" and computer == "paper") or
        (player == "paper" and computer == "scissors") or
        (player == "scissors" and computer == "rock")):
        # prompt("Computer wins!")
        print("Computer wins!")
        return "Computer wins!"

    else:
        # prompt("It's a tie!")
        print("It's a tie!")
        return "It's a tie!"

keep_going = True
# while True:
while keep_going:

    prompt(f'Choose one: {", ".join(VALID_CHOICES)}')
    choice = input()

    while choice.casefold() not in VALID_CHOICES:
        prompt("That's not a valid choice")
        choice = input()

    computer_choice = random.choice(VALID_CHOICES)

    display_winner(choice, computer_choice)
    
    # if display_winner == "Computer wins!":
    #     print("Computer wins!")
    # elif display_winner == "You win!":
    #     print("You win!")
    # elif display_winner == "It's a tie!":
    #     print("It's a tie!")

    # while True:
    #     prompt("Do you want to play again (y/n)?")
    #     answer = input().lower()

    #     if answer.startswith('n') or answer.startswith('y'):
    #         break
    #     else:
    #         prompt("That's not a valid choice")

    # if answer[0] == 'n':
    #     break
        
    prompt("Do you want to play again (y/n)?")
    answer = input().lower()

    # Condition will evaluate as True only when both operands do not start
    # with 'n' or 'y'

    while not answer.startswith('n') and not answer.startswith('y') == True:
        prompt('Please enter "y" or "n".')
        answer = input().lower()    
        
           
    if answer[0] == 'n':
        keep_going = False
    