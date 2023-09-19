# Sträng med 20-50 ord
# räknar antal ord 
# och lägger ihop längden och skriver ut medellängd på orden
import os
os.system("cls")


word_list = "Ett Två Tre Johan Nisse " # Must have a blankspace after the last word.
word = ""
words = []
word_length = 0

for i in range(len(word_list)):
    if word_list[i] == " ":
        words += [word]
        word_list.replace(word, " ")
        word = ""
    else: 
        word += word_list[i]

total_words = len(words)

for i in range(total_words):
    word_length += len(words[i])

print(word_length / total_words)