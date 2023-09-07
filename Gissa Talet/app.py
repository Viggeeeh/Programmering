# Gissa Talet
# Coded and Designed Viggo Öfors
# Sources: Johan Wrangö with the colors.
# Version 1.0.1

import os
import random
from colors import bcolors
os.system('cls')

def check_number(guess, dice):
    if guess < dice:
        return print(bcolors.RED + "Higher Number! You have", (7 - tries), "tries left")
    elif guess > dice:
        return print(bcolors.RED + "Lower Number! You have", (7 - tries), "tries left")
    elif guess == dice:
        global win # Makes a global variable
        win = True
        return print(bcolors.GREEN + "That's the right Number! It took you", tries, "tries!")  

# Variables
win = False
cheat = False
avalible_tries = 7
tries = 1
dice = random.randint(1, 100)  
game = True 


print(bcolors.YELLOW + """Welcome to Guess The Number!
Developed by the one and only: Viggo Öfors
      
In this game you'll have to guess a number
between 1 and 100 And you only have 7 tries.
      
Note that if you type a negative or a number 
that is over 100, you will lose a try.

/q or /quit to force quit 
      
and /cheat for cheats :)
      
Good luck!\n""")

# Game loop
while game:
    if cheat:
        print(bcolors.GREEN, dice, bcolors.RED + "is the number")
    
    while True:
        try:
            guess = input(bcolors.DEFAULT + "\nGuess a number: " + bcolors.CYAN).lower()

            if guess == "/cheat":
                print(bcolors.PURPLE + "Cheat Activated!")
                cheat = True
                print(bcolors.GREEN, dice, bcolors.RED + "is the number") # + doesnt work infront of dice.

            elif guess == "/quit" or guess == "/q":
                print(bcolors.RED + "You Just ended the game!")
                game = False
                break

            guess = int(guess)
            check_number(guess, dice) # Checks and returns if the guess is correct
            break
        except:
            print("It Needs to be a Number!")


    # Handles the rounds
    tries += 1
    avalible_tries -= 1

    if avalible_tries <= 0 or win:
        if not win:
            print(bcolors.BLUE + "You sadly lost...")

        # Check if the user want's to play again
        new_game = input(bcolors.BLUE + "Do you want to try again? (Y/N): ").upper()
        if new_game == "Y":
            dice = random.randint(1, 100)   # Rolls a new dice
            # Resets the stats
            avalible_tries = 7
            tries = 1
            win = False

            os.system('cls')
        else:
            game = False