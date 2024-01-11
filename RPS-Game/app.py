from symbols import symbols
from functions import functions
from msvcrt import getwch
import random
import os

os.system("cls")

available_keys = ["R", "P", "S"]
score = 0 

while True:
    while True:
        print("\nPress R, P or S ", end="")
        key_pressed = getwch()
        os.system("cls")

        AI_choice = functions.AI()

        if key_pressed.upper() in available_keys:
            if key_pressed.upper() == "R":
                print(f"\nYou Chose:{symbols.rock}")
                functions.win_conditions("R", AI_choice)

            elif key_pressed.upper() == "P":
                print(f"\nYou Chose:{symbols.paper}")
                functions.win_conditions("P", AI_choice)

            elif key_pressed.upper() == "S":
                print(f"\nYou Chose:{symbols.scissors}")
                functions.win_conditions("S", AI_choice)
            break
        else:
            print("It has to be either R, P or S!")