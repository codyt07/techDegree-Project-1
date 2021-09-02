"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces. 

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""

import random
games =[]

def start_game():
    """Psuedo-code Hints
    
    When the program starts, we want to:
    ------------------------------------
    1. Display an intro/welcome message to the player.
    2. Store a random number as the answer/solution.
    3. Continuously prompt the player for a guess.
      a. If the guess greater than the solution, display to the player "It's lower".
      b. If the guess is less than the solution, display to the player "It's higher".
    
    4. Once the guess is correct, stop looping, inform the user they "Got it"
         and show how many attempts it took them to get the correct number.
    5. Let the player know the game is ending, or something that indicates the game is over.
    
    ( You can add more features/enhancements if you'd like to. )
    """
    # write your code inside this function.
    
    print("Welcome to the random number guessing game!")
    player_name = input("What is your name? ")
    player_guess = input(f"Welcome {player_name}, Please guess a number between 1 - 10: ")
    print("-" * 12)
    while True:
        try:
            player_guess = int(player_guess)
            winning_check(player_guess, player_name)
            break
        except ValueError:
            print("You did not enter a number!")
            player_guess = input(f"Welcome {player_name}, Please guess a number between 1 - 10: ")
        print("-" * 12)
        print("-" * 12)
      
def winning_check(player_guess, player_name):
  Winning_number = random.randint(1,10)  
  attempts = 1
  while player_guess != Winning_number:
    attempts += 1
    if player_guess < Winning_number:
      print(f"This is attempt number: {attempts}!")
      print(f"You guessed: {player_guess}, It's higher!")
      player_guess = input("Guess a new number: ")
      print("-" * 12)
      print("-" * 12)
    elif player_guess > Winning_number:
      print(f"This is attempt number {attempts}!")
      print(f"You guessed: {player_guess}, It's lower!")  
      player_guess = input("Guess a new number: ")
      print("-" * 12)
      print("-" * 12)
    while True:
      try:
        player_guess = int(player_guess)
        break
      except ValueError:
        player_guess = input("You did not input a number, try again! ")
  else:
    print("Got it! You have won!")
    print(f"it took you {attempts} attempt(s)!") 
    redo = input(f"Do you want to play again {player_name}? Enter yes/no: ")
    while True:
        if redo.lower() == "yes":
            new_game(player_name, attempts)
            break
        elif redo.lower() == "no":
            print("Thank you for playing!")
            break
        else: 
            redo = input("You did not enter a valid entry! Try again: ")
            
             
def new_game(player_name, attempts):
    games.append(attempts)
    rounds = len(games)
    index = rounds - 1
    while True: 
        if rounds != 0:
            print(f"Round {rounds} Score was: ", games[index])
            rounds = rounds - 1
            index = index - 1 
        else:
            break
    player_guess = input(f"Welcome back {player_name}, Please guess a number between 1 - 10: ")
    print("-" * 12)
    while True:
      try:
        player_guess = int(player_guess)
        winning_check(player_guess, player_name)
        break
      except ValueError:
        print("You did not enter a number!")
        player_guess = input(f"Welcome {player_name}, Please guess a number between 1 - 10: ")
        print("-" * 12)
        print("-" * 12)
    
    
            
start_game() 