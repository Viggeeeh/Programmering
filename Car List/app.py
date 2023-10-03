import os
from colors import bcolors

os.system("cls")
car_list = []

def instructions():
    print(f"""{bcolors.DEFAULT}Welcome to {bcolors.BOLD + bcolors.CYAN}Favourite Cars List{bcolors.DEFAULT}
1) Type a new car and it will {bcolors.UNDERLINE + bcolors.GREEN}appear{bcolors.DEFAULT}
2) Enter the same car and it will {bcolors.UNDERLINE + bcolors.RED}disappear{bcolors.DEFAULT}
3) Write {bcolors.BOLD + bcolors.BLUE}edit {bcolors.DEFAULT}to edit a list item
4) Press {bcolors.BOLD + bcolors.PURPLE}enter{bcolors.DEFAULT} to {bcolors.UNDERLINE}exit{bcolors.DEFAULT} from the list\n""")
    

def check_inputs(name):
    if name == "":
        exit()

    if name == "edit":
        while True: # Makes sure we don't get a wrong input
            try:
                edit_car = int(input(f"{bcolors.DEFAULT}What item would you like to edit? "))
                new_car = input(f"What would you like to change {bcolors.BLUE + car_list[edit_car-1] + bcolors.DEFAULT} with? ")
                car_list[edit_car-1] = new_car
                break
            except:
                print("It has to be in the list!\n")
            
    elif name in car_list:
        car_list.pop(car_list.index(name)) 

    elif not name in car_list: 
        car_list.append(name)


while True:
    instructions()

    for i in car_list:
        print(f"{bcolors.DEFAULT} {car_list.index(i)+1}) {bcolors.BLUE + i}")

    car = input(f"{bcolors.DEFAULT}Enter a Car: {bcolors.BLUE}")

    check_inputs(car)
    os.system("cls")