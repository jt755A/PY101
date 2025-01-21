"""
A rock, paper, scissors, lizard, spock game with best-of-five rounds.

The user plays against the computer (which makes a random choice).
The user is prompted to make a choice, and the result is displayed:
the result of each round, the running tally.
After a best of five rounds 'grand winner' is determined, the user is
asked if they would like to play another 5 rounds.
"""

import random

VALID_CHOICES = ['rock', 'paper', 'scissors', 'lizard', 'spock']
# This constant allows shortened input from user.
VALID_CHOICES_SHORTENED = [CHOICE[0] for CHOICE in VALID_CHOICES]
WINNING_COMBOS = {
    'rock': ['scissors', 'lizard'],
    'paper': ['rock', 'spock'],
    'scissors': ['paper', 'lizard'],
    'lizard': ['paper', 'spock'],
    'spock': ['rock', 'scissors'],
}

player_win_tally = 0
computer_win_tally = 0

def prompt(message):
    """Gives a visual clue of program output to user."""
    print(f"===> {message}")

def player_wins(player_choice, computer_choice):
    """Returns True if player wins, False otherwise"""
    return computer_choice in WINNING_COMBOS[player_choice]

def display_winner(player, computer):
    """Prints the result of a round to terminal, and increments win tally."""
    if player_wins(player, computer):
        prompt("You win!")
        global player_win_tally
        player_win_tally += 1

    elif player == computer:
        prompt("It's a tie!")

    else:
        prompt("Computer wins!")
        global computer_win_tally
        computer_win_tally += 1

keep_going = True

prompt("Welcome to the game! You will be playing against the computer in a"
" best-of-5-rounds match.\nPlease note you can enter just the first letter"
" of any valid choice.\n\nGood luck!\n\n")

while keep_going:

    # Resets tallies and round counter for each Best of Five loop
    player_win_tally = 0
    computer_win_tally = 0
    round_counter = 1

    # Best of Five loop
    while player_win_tally < 3 and computer_win_tally < 3:

        prompt(f'Round {round_counter}. Choose one: {", ".join(VALID_CHOICES)}')
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

        round_counter += 1

        if player_win_tally == 3:
            grand_winner = 'Player'
            prompt(f'The grand winner is {grand_winner}!')

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
        prompt("Thank you for playing the game. See you next time!")
        keep_going = False
