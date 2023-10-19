# Uppgift 1 och 2 - Countdown Timer
"""
import os
import time

os.system("cls")

while True:
    try:
        counter = int(input("How long would you like the timer to be (in seconds)? "))
        break
    except:
        print("It has to be a number!")

while True:
    os.system("cls")
    print(counter)
    counter -= 1
    time.sleep(1)

    if counter < 0:
        print("Ding Ding Ding!")
        exit()
"""

# Uppgift 3
"""
from msvcrt import getwch
import os

os.system("cls")

while True:
    name = input("What is your name? ")
    age = input(f"Okey {name}, how old are you? ")
    print(f"Welcome {name}, my cat is also {age} years old!")

    print("Press q to quit ", end="")

    key_press = getwch()

    if key_press.lower() == "q":
        exit()
"""        

# Uppgift 4
"""
from colors import bcolors

print(bcolors.RED + "Red color")
print(bcolors.BLUE + "Blue color")
"""


# Uppgift 5 och 6 - Countdown timer updaterad.
from colors import bcolors
from msvcrt import getwch
import time
import os

print(f"{bcolors.RED}Press any button! ", end="")
key_down = getwch()
os.system("cls")

if key_down:
    time_input = int(input(f"{bcolors.GREEN}Time in seconds: {bcolors.RED}"))
    while True:
        os.system("cls")

        if time_input > 0:
            print(f"{bcolors.CYAN}{time_input}")
            time_input -= 1
            time.sleep(1)
        else:
            print(f"{bcolors.YELLOW + bcolors.UNDERLINE}Time has ended!{bcolors.DEFAULT}")
            exit()