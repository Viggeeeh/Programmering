import os
import random
from colors import bcolors
os.system('cls')

# Todo List
# Commands: /quit, /cheat etc.
# Secret Numbers: If you guess the number, you'll get something.
# Print tries left.

def check_number(guess, dice):
    if guess < dice:
        return print(bcolors.RED + "Higher Number!")
    elif guess > dice:
        return print(bcolors.RED + "Lower Number!")
    elif guess == dice:
        global win # Makes a global variable
        win = True
        return print(bcolors.GREEN + "That's the right Number!")    

# Variables
win = False
avalible_tries = 7
dice = random.randint(1, 100)   


print("""Welcome to Guess The Number!
Developed by the one and only: Viggo Öfors
In this game you'll have to guess a number
between 1 and 100 And you only have 7 tries. 
Good luck!\n""")

# Game loop
while True:
    print(dice)
    while True:
        # Handles The Guess
        try:
            guess = int(input(bcolors.DEFAULT + "Guess a number: "))
            break
        except:
            print("It Needs to be a Number!")

    check_number(guess, dice) # Checks and returns if the guess is correct 

    # Handles the rounds
    avalible_tries -= 1

    if avalible_tries <= 0 or win:
        if not win:
            print(bcolors.BLUE + "You sadly lost...")

        # Check if the user want's to play again
        new_game = input(bcolors.BLUE + "Do you want to try again? (Y/N): ").upper()
        if new_game == "Y":
            dice = random.randint(1, 100)   
            avalible_tries = 7
            win = False
        else:
            break