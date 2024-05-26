# Guess The Price
# Coded and Designed Viggo Öfors
# Sources: ChatGPT with the colors and some questions.
# Version 1.0.0

from msvcrt import getwch
from colors import dye
import time
import json
import os
os.system("cls")


# json_file = "questions.json", doesn't work, this is the solution
current_dir = os.path.dirname(os.path.abspath(__file__)) # Gets the path 
question_file = os.path.join(current_dir, "questions.json") # Combinds the file with the directory
highscore_file = os.path.join(current_dir, "highscore.json") # Combinds the file with the directory
questions = [] # loads when LOAD functions is called.
highscore = None
availible_keys = ["A", "B", "C", "D"]

score = 0 # counts your score this round for later applying to highscore
edit = False


# Welcome function
def welcome():
    print(f'Welcome to {dye.BLUE}Guess {dye.MAGENTA}the {dye.GREEN}Price!{dye.RESET}')
    print(f'\n{dye.RED}Highscore{dye.BLACK}:{dye.RESET} {highscore}') # Shows highscore
    print(f'''\n{dye.BLUE}(1){dye.RESET} Try ALL of the questions
{dye.MAGENTA}(2){dye.RESET} Edit them if you are not happy
{dye.GREEN}(3){dye.RESET} Submit your answers''')

    print(f'\nPress {dye.RED}ANY{dye.RESET} button to start', end="")
    if getwch():
        pass

# SAVE function
def save_files(files):
    with open(question_file, "w") as file:
        json.dump(files, file)
    
# LOAD function
def load_files():
    with open(question_file, "r") as file:
        global questions
        questions = json.load(file)

# RESET function
def reset_files():
    for i in range(0, len(questions)):
        questions[i]["user_answer"] = None
    global score
    score = 0

# HIGHSCORE function
def load_highscore():
    with open(highscore_file, "r") as file:
        global highscore
        highscore = json.load(file)

# Send new highscore to json
def send_highscore():
    global highscore
    global score
    if highscore < score:
        highscore = score
    with open(highscore_file, "w") as file:
        json.dump(highscore, file)
    

# POINT function
def total_points():
    for i in range(0, len(questions)):
        correct_answer = questions[i]["correct_answer_index"]
        user_answer = questions[i]["user_answer"]
        if correct_answer == user_answer:
            global score
            score += 1

def end_screen():
    # Changes the color depending on your score
    if score < (0.5 * len(questions)):
        score_color = dye.RED
    elif score >= (0.5 * len(questions)) and score < (0.8 * len(questions)):
        score_color = dye.YELLOW
    else: 
        score_color = dye.GREEN
        
    print(f'You scored {score_color}{score}{dye.RESET} out of {dye.GREEN}{len(questions)}{dye.RESET}')

# The function for edit mode
def edit_mode():
    print(f'{dye.RED}{questions[i]["question"]}{dye.RESET}')
    for k in range(0, len(questions[i]["answers"])):
        if k == questions[i]["user_answer"]:
            print(f'{dye.CYAN}{availible_keys[k].lower()}) {dye.BG_RED}{questions[i]["answers"][k]}{dye.RESET}') # all the answer choices
        else:
            print(f'{dye.CYAN}{availible_keys[k].lower()}){dye.RESET} {questions[i]["answers"][k]}') # all the answer choices



# Main Game

load_files()
load_highscore()
welcome()

while True:
    # Loops as long as there's questions
    for i in range(0, len(questions)):
        os.system("cls")
        if not edit:
            print(f'{dye.RED}{questions[i]["question"]}{dye.RESET}')
            for k in range(0, len(questions[i]["answers"])):
                print(f'{dye.CYAN}{availible_keys[k].lower()}){dye.RESET} {questions[i]["answers"][k]}') # all the answer choices
        elif edit:
            edit_mode()

        # Make sure the user press an availible button
        while True:
            key_pressed = getwch().upper()
            if key_pressed in availible_keys:
                questions[i]["user_answer"] = availible_keys.index(key_pressed) # Adds the answer to the json file
                break
            
    while True:
        os.system("cls")
        print(f'Are you happy with your answers? ({dye.GREEN}Y{dye.RESET}/{dye.RED}N{dye.RESET})', end=" ")
        key_pressed = getwch().upper()
        if key_pressed == "Y":
            os.system("cls")
            total_points()
            save_files(questions)
            send_highscore()

            end_screen()
            time.sleep(2)

            reset_files() 

            print(f'Do you want to play again? ({dye.GREEN}Y{dye.RESET}/{dye.RED}N{dye.RESET})', end=" ")
            key_pressed = getwch().upper()
            if key_pressed == "Y":
                break
            elif key_pressed == "N":
                quit()
        elif key_pressed == "N":
            edit = True
            break
