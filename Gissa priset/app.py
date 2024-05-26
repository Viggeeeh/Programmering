from msvcrt import getwch
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

counter = 0 # counts your score this round for later applying to highscore

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

# HIGHSCORE function
def load_highscore():
    with open(highscore_file, "r") as file:
        global highscore
        highscore = json.load(file)

# Send new highscore to json
def send_highscore():
    global highscore
    global counter
    if highscore < counter:
        highscore = counter
    with open(highscore_file, "w") as file:
        json.dump(highscore, file)
    

# POINT function
def total_points():
    for i in range(0, len(questions)):
        correct_answer = questions[i]["correct_answer_index"]
        user_answer = questions[i]["user_answer"]
        if correct_answer == user_answer:
            global counter
            counter += 1
    print(counter)


load_files()
load_highscore()

while True:
    for i in range(0, len(questions)):
        os.system("cls")
        print(highscore)
        print(questions[i]["question"])
        for k in range(0, len(questions[i]["answers"])):
            print(f"{availible_keys[k].lower()}) {questions[i]['answers'][k]}") # all the answer choices

        print("Choose an answer", end=" ")
        while True:
            key_pressed = getwch().upper()
            if key_pressed in availible_keys:
                questions[i]["user_answer"] = availible_keys.index(key_pressed)
                break
            
    while True:
        os.system("cls")
        print("Are you done? (Y/N)", end=" ")
        key_pressed = getwch().upper()
        if key_pressed == "Y":
            total_points()
            reset_files() 
            save_files(questions)
            send_highscore()
            quit() # END SCREEN HAS TO BE HERE
        elif key_pressed == "N":
            break
