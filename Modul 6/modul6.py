# Uppgift 1
def addition(num_1, num_2):
    return print(num_1 + num_2)

addition(5, 2)


# Uppgift 2
def name_printer(name):
    return print(name)

name = input("What is your name? ")
name_printer(name)


# Uppgift 3
for i in range(10):
    addition(i, 1)


# Uppgift 4
array = []

def add(word):
    array.append(word)

def delete(index):
    array.pop(index-1)

def change(index, word):
    array[index-1] = word

while True:
    while True:
        setting = input("add / delete / change: ")
        if setting == "add":
            word = input("Type something: ")
            add(word)
        elif setting == "delete":
            print(array)
            index = int(input("which word would you like to remove? (1 for the first word etc.): "))
            delete(index)
        elif setting == "change":
            print(array)
            index = int(input("which word would you like to change? (1 for the first word etc.): "))
            word = input(f"Type something to replace {array[index-1]} with: ")
            change(index, word)
        break
        

    for i in range(len(array)):
        print(array[i])

    break   # Behövs för att koden under ska funka.


# Uppgift 5
def calculate(operator, number_1, number_2):
    if operator == "+":
        print(number_1 + number_2)
    elif operator == "-":
        print(number_1 - number_2)
    elif operator == "*":
        print(number_1 * number_2)
    elif operator == "/" and number_1 != 0 and number_2 != 0:
        print(number_1 / number_2)
    elif number_1 == 0 or number_2 == 0:
        print("You can't devide by 0!")
    else:
        print("Error!")
    
operator = input("+ - / *: ")
number_1 = float(input("Enter a number: "))
number_2 = float(input("Enter another number: "))
calculate(operator, number_1, number_2)
