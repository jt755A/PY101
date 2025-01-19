import random

VALID_CHOICES = ['rock', 'paper', 'scissors', 'lizard', 'spock']
# This constant allows shortened input from user.
VALID_CHOICES_SHORTENED = [CHOICE[0] for CHOICE in VALID_CHOICES]

player_win_tally = 0
computer_win_tally = 0
grand_winner = ''

def prompt(message):
    print(f"===> {message}")

def display_winner(player, computer):
    prompt(f"You chose {player}, computer chose {computer}")

    if ((player == "rock" and computer == "scissors") or
        (player == "rock" and computer == "lizard") or

        (player == "paper" and computer == "rock") or
        (player == "paper" and computer == "spock") or

        (player == "scissors" and computer == "paper") or
        (player == "scissors" and computer == "lizard") or

        (player == "lizard" and computer == "spock") or
        (player == "lizard" and computer == "paper") or

        (player == "spock" and computer == "scissors") or
        (player == "spock" and computer == "rock")):
        prompt("You win!")
        global player_win_tally
        player_win_tally += 1

    elif ((player == "rock" and computer == "paper") or
        (player == "rock" and computer == "spock") or

        (player == "paper" and computer == "scissors") or
        (player == "paper" and computer == "lizard") or

        (player == "scissors" and computer == "rock") or
        (player == "scissors" and computer == "spock") or

        (player == "lizard" and computer == "rock") or
        (player == "lizard" and computer == "scissors") or

        (player == "spock" and computer == "lizard") or
        (player == "spock" and computer == "paper")):
        prompt("Computer wins!")
        global computer_win_tally
        computer_win_tally += 1

    else:
        prompt("It's a tie!")

keep_going = True

while keep_going:

    # Best of Five loop
    while player_win_tally < 3 and computer_win_tally < 3:

        prompt(f'Choose one: {", ".join(VALID_CHOICES)}')
        choice = input()
    # added constant for 1st character
        while choice.casefold() not in VALID_CHOICES and\
        choice.casefold() not in VALID_CHOICES_SHORTENED:
            prompt("That's not a valid choice")
            choice = input()

        # If the player used shortened input:
        # this block reassigns choice to its
        # corresponding full-length string.
        if choice in VALID_CHOICES_SHORTENED:
            match choice:

            # add a new case condition for future additions to VALID_CHOICES,
            # where you have multiple words starting with the same letter.
                case 's':
                    prompt('Select 1) scissors 2) spock')
                    choice = input()
                    while choice not in ['1', '2']:
                        prompt('Please enter "1" for scissors, or "2" for spock')
                        choice = input()

                    match choice:
                        case '1':
                            choice = 'scissors'
                        case '2':
                            choice = 'spock'

                case _:
                    index = VALID_CHOICES_SHORTENED.index(choice)
                    choice = VALID_CHOICES[index]

        computer_choice = random.choice(VALID_CHOICES)

        display_winner(choice, computer_choice)

        prompt(f'The score is:\n===> Player: {player_win_tally}, Computer: {computer_win_tally},')

        if player_win_tally == 3:
            grand_winner = 'Player'

        if computer_win_tally == 3:
            grand_winner = 'Computer'

    prompt(f'The grand winner is {grand_winner}!')

    # Play another match of best-of-five
    prompt("Do you want to play again (y/n)?")
    answer = input().lower()

    # Error validation

    while not answer.startswith('n') and not answer.startswith('y') is True:
        prompt('Please enter "y" or "n".')
        answer = input().lower()

    if answer[0] == 'n':
        keep_going = False
