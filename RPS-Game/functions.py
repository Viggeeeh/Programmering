from symbols import symbols
from colors import color
import random
import json
import os

# json_file = "stats.json", doesn't work, this is the solution
current_dir = os.path.dirname(os.path.abspath(__file__)) # Gets the path 
json_file = os.path.join(current_dir, "stats.json") # Combinds the file with the directory

score = {
    "wins": 0,
    "losses": 0,
    "ties": 0
}


def welcome():
    print(f"""
{color.YELLOW}__        __   _                           {color.RED} _         {color.BLUE} ____  ____  ____  {color.DEFAULT} 
{color.YELLOW}\ \      / /__| | ___ ___  _ __ ___   ___  {color.RED}| |_ ___   {color.BLUE}|  _ \|  _ \/ ___| {color.DEFAULT}
{color.YELLOW} \ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _ \ {color.RED}| __/ _ \  {color.BLUE}| |_) | |_) \___ \ {color.DEFAULT}
{color.YELLOW}  \ V  V /  __/ | (_| (_) | | | | | |  __/ {color.RED}| || (_) | {color.BLUE}|  _ <|  __/ ___) |{color.DEFAULT}
{color.YELLOW}   \_/\_/ \___|_|\___\___/|_| |_| |_|\___| {color.RED} \__\___/  {color.BLUE}|_| \_\_|   |____/ {color.DEFAULT}
""")


def load_stats():
    with open(json_file, "r") as file:
        global score
        score = json.load(file)


def AI():
    choice = random.randint(1, 3)
    if choice == 1:
        print(f"AI Chose ⬇️{color.LIGHT_GREEN + symbols.rock + color.DEFAULT}")
        result = "R"
    elif choice == 2:
        print(f"AI Chose ⬇️{color.LIGHT_GREEN + symbols.paper + color.DEFAULT}")
        result = "P"
    elif choice == 3:
        print(f"AI Chose ⬇️{color.LIGHT_GREEN + symbols.scissors + color.DEFAULT}")
        result = "S"

    return result


def round_end(condition):
    if condition == "win":
        score["wins"] += 1
        print(color.BOLD + color.GREEN + "\nYou Won!" + color.DEFAULT)
    elif condition == "loss":
        score["losses"] += 1
        print(color.BOLD + color.RED + "\nYou Lost..." + color.DEFAULT)
    else:
        score["ties"] += 1
        print(color.BOLD + color.DARK_GRAY + "\nIt's a tie!" + color.DEFAULT)


def win_conditions(player_choice, AI_choice):
    if player_choice == "Q":
        # Saves the stats
        with open(json_file, "w") as file:
            json.dump(score, file)
    elif player_choice == "U":
        # Resets the score
        score["wins"] = 0
        score["losses"] = 0
        score["ties"] = 0

    # Tie
    if player_choice == AI_choice:
        round_end("ties")
    # Rock beats Scissors
    elif player_choice == "R": 
        if AI_choice == "S":
            round_end("win")
        else: 
            round_end("loss")

            
    # Scissors beats Paper
    elif player_choice == "S":
        if AI_choice == "P":
            round_end("win")
        else:
            round_end("loss")
    # Paper beats Rock
    elif player_choice == "P":
        if AI_choice == "R":
            round_end("win")
        else:
            round_end("loss")