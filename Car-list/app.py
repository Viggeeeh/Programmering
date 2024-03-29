# app.py: Skriv in dina favoritbilar i en lista

__author__  = "Viggo Öfors"
__version__ = "1.0.0"
__email__   = "viggo.ofors@elev.ga.ntig.se"


import os
from colors import bcolors
import json

os.system("cls")
car_list = []
file_name = "./Car-list/list.json"
file_exists = os.path.exists(file_name)


def instructions():
    print(f"""{bcolors.DEFAULT}Welcome to {bcolors.BOLD + bcolors.CYAN}Favourite Cars List{bcolors.DEFAULT}
1) Type a new car and it will {bcolors.UNDERLINE + bcolors.GREEN}appear{bcolors.DEFAULT}
2) Enter the same car and it will {bcolors.UNDERLINE + bcolors.RED}disappear{bcolors.DEFAULT}
3) Write {bcolors.BOLD + bcolors.BLUE}edit {bcolors.DEFAULT}to edit a list item
4) Press {bcolors.BOLD + bcolors.PURPLE}enter{bcolors.DEFAULT} to {bcolors.UNDERLINE}exit{bcolors.DEFAULT} from the list\n""")
    
def check_inputs(car_name):
    if car_name == "":
        # Adds to json
        if file_exists:
            os.remove(file_name)
        with open(file_name, "w") as file:
            json.dump(car_list, file)

        exit()


    if car_name.lower() == "edit" and len(car_list) > 0:
        while True: # Makes sure we don't get a wrong input
            try:
                print(f"{bcolors.DEFAULT}Press {bcolors.PURPLE}Enter {bcolors.DEFAULT}to exit Edit Mode")
                edit_car = input(f"{bcolors.DEFAULT}What item would you like to edit? (1 - {len(car_list)}): ")

                # Press enter to exit edit mode
                if edit_car == "":
                    break
                
                # Makes it to an integer
                edit_car = int(edit_car)

                new_car = input(f"What would you like to change {bcolors.BLUE + car_list[edit_car-1] + bcolors.DEFAULT} with? ")
                car_list[edit_car-1] = new_car
                break
            except:
                print("It has to be in the list!\n")
            
    elif car_name in car_list:
        car_list.pop(car_list.index(car_name)) 

    elif not car_name in car_list: 
        car_list.append(car_name)

# Adds the beforeused list
if file_exists:
    with open(file_name, "r") as file:
        car_list += json.load(file)
    

while True:
    instructions()
    print(car_list) # Debug test

    for i in car_list:
        print(f"{bcolors.DEFAULT} {car_list.index(i)+1}) {bcolors.BLUE + i}")

    car = input(f"{bcolors.DEFAULT}Enter a Car: {bcolors.BLUE}")

    check_inputs(car)
    os.system("cls")