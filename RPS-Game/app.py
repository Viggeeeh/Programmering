from symbols import symbols
from msvcrt import getwch
from colors import color
import functions
import os

os.system("cls")

available_keys = ["R", "P", "S", "Q", "U"]

# Load the stats     
functions.load_stats()

# Welcome message
functions.welcome()

while True:
    while True:
        print(f"Wins: {color.GREEN}{functions.score['wins']}{color.DEFAULT}, Losses: {color.RED}{functions.score['losses']}{color.DEFAULT}, ties: {color.DARK_GRAY}{functions.score['ties']}{color.DEFAULT}")
        print(f"\nPress {color.LIGHT_BLUE + color.BOLD}R{color.DEFAULT}, {color.LIGHT_BLUE + color.BOLD}P{color.DEFAULT}, {color.LIGHT_BLUE + color.BOLD}S{color.DEFAULT}, {color.YELLOW + color.BOLD}Q {color.BLACK + color.BOLD}({color.WHITE}to quit{color.BLACK + color.BOLD}){color.DEFAULT} or {color.YELLOW + color.BOLD}U {color.BLACK + color.BOLD}({color.WHITE}to reset score{color.BLACK + color.BOLD}){color.DEFAULT} ", end="")
        
        key_pressed = getwch()
        os.system("cls")

        if key_pressed.upper() in available_keys:
            if key_pressed.upper() == "U":
                functions.win_conditions("U", None)
                break

            elif key_pressed.upper() == "Q":
                functions.win_conditions("Q", None)
                quit()
            
            AI_choice = functions.AI() 
            
            if key_pressed.upper() == "R":
                print(f"\nYou Chose ⬇️{color.DARK_GRAY + symbols.rock + color.DEFAULT}")
                functions.win_conditions("R", AI_choice)

            elif key_pressed.upper() == "P":
                print(f"\nYou Chose ⬇️{color.WHITE + symbols.paper + color.DEFAULT}")
                functions.win_conditions("P", AI_choice)

            elif key_pressed.upper() == "S":
                print(f"\nYou Chose ⬇️{color.ORANGE + symbols.scissors + color.DEFAULT}")
                functions.win_conditions("S", AI_choice)
            break
        else:
            print("It has to be either R, P or S!")