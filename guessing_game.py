import random

"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces.

NOTE: If you strongly prefer to work locally on your own computer, you can
totally do that by clicking:
File -> Download Workspace in the file menu after you fork the snapshot of this
workspace."""

"""Going for "Exceeds Expectations Grade only... Thank you in advance!
PEP 8 kind of verified"""

games = []


def start_game():
    """Psuedo-code Hints

    When the program starts, we want to:
    ------------------------------------
    1. Display an intro/welcome message to the player.
    2. Store a random number as the answer/solution.
    3. Continuously prompt the player for a guess.
      a. If the guess greater than the solution,
            display to the player "It's lower".
      b. If the guess is less than the solution,
            display to the player "It's higher".
    4. Once the guess is correct, stop looping, inform the user they "Got it"
         and show how many attempts it took them to get the correct number.
    5. Let the player know the game is ending, or something
        that indicates the game is over.

    ( You can add more features/enhancements if you'd like to. )
    """
    # write your code inside this function.
    Winning_number = random.randint(1, 10)
    print("Welcome to the random number guessing game!")
    player_name = input("What is your name? ")
    player_guess = input(f"Welcome {player_name}, Please guess a number between 1 - 10: ")
    space()
    attempts = 1
    best_score = 0
    player_check(player_guess, player_name, attempts, Winning_number)
    space()


def space():
    print("=" * 15)
    print("=" * 15)


def winning_check(player_guess, player_name, attempts, Winning_number):
    if player_guess != Winning_number:
        attempts += 1
    if player_guess < Winning_number:
        space()
        print(f"This is attempt number: {attempts}!")
        print(f"You guessed: {player_guess}, It's higher!")
        player_guess = input("Guess a new number: ")
        player_check(player_guess, player_name, attempts, Winning_number)
    elif player_guess > Winning_number:
        space()
        print(f"This is attempt number {attempts}!")
        print(f"You guessed: {player_guess}, It's lower!")
        player_guess = input("Guess a new number: ")
        player_check(player_guess, player_name, attempts, Winning_number)
    else:
        space()
        print("Got it! You have won!")
        print(f"it took you {attempts} attempt(s)!")
        redo = input(f"Do you want to play again {player_name}? Enter yes/no: ")
        space()
    while True:
        if redo.lower() == "yes":
            new_game(player_name, attempts)
            break
        elif redo.lower() == "no":
            print("Thank you for playing!")
            exit()
            
        else:
            redo = input("You did not enter a valid entry! Try again: ")


def player_check(player_guess, player_name, attempts, Winning_number):
    try:
        player_guess = int(player_guess)
        if player_guess < 1:
            player_guess = input("You entered a number lower than 1. Try again! ")
            player_check(player_guess, player_name, attempts, Winning_number)
        elif player_guess > 10:
            player_guess = input("You entered a number higher than 10. Try again! ")
            player_check(player_guess, player_name, attempts, Winning_number)
        else:
            winning_check(player_guess, player_name, attempts, Winning_number)
    except ValueError:
            player_guess = input("you did not enter a number! Try Again: ")
            player_check(player_guess, player_name, attempts, Winning_number)


def new_game(player_name, attempts):
    games.append(attempts)
    rounds = len(games)
    space()
    index = rounds - 1
    best_score = min(games)
    print(f"Your best score was: {best_score}")
    while True:
        if rounds != 0:
            print(f"Round {rounds} Score was:", games[index])
            rounds = rounds - 1
            index = index - 1
        else:
            break
    player_guess = input(f"Welcome back {player_name}, Please guess a number between 1 - 10: ")
    attempts = 1
    Winning_number = random.randint(1, 10)
    player_check(player_guess, player_name, attempts, Winning_number)
    print("-" * 12)


start_game()
