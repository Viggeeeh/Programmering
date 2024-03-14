import random
from colors import color

def word_selection():
    selected_word = random.randint(0, len(words))
    return words[selected_word-1]


def user_input():
    while True:
        user_input = input("Type a word (that is 5 letters): ") 
        if len(user_input) == 5:
            break
        else:
            print("It has to be 5 letters!")
    return user_input


def guess_handle(word, guess):
    output = f""
    if guess == word:
        print("You guessed the word right!")
    else:
        for guess_index in range(0, 5):
            for word_index in range(0, 5):
                if guess[guess_index] == word[word_index]:
                    output += guess[guess_index]
                else:
                    output += guess[guess_index]
        print(output)
                




words = ["apple", "table", "cloud", "grape", "beach"]

while True:
    round_word = word_selection()
    print(round_word)
    while True:
        user_guess = user_input()
        guess_handle(round_word, user_guess)
