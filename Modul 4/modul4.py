import os
import random
os.system('cls')

# Uppgift 1
lenght = float(input("Vad är din längd i meter? "))
if lenght < 1.40:
    print("Du får inte åka allt på Gröna Lund! ")
else:
    print("Du får åka allt på Gröna Lund! ")

# Uppgift 2
name = input("What is your name? ")
age = input("What is your age? ")

while True: 
    try:
        if int(age):
            print("Välkommen", name, "Din ålder är", age)
            break
    except:
        age = input("What is your age? It needs to be a number. ")


# Uppgift 3
weight = input("Vad väger du? (i KG): ")
height = input("Hur lång är du? (i Meter): ")
try:
    if float(weight) and float(height):
        print("Ditt program funkar.")
except:
    print("Error!")

bmi = float(weight) / float(height) ** 2
print(bmi)

if (bmi <= 18.4):
    print("bmi = ", bmi, "du är underviktig.")
elif (bmi > 18.4 and bmi < 25):
    print("bmi = ", bmi, "du är normalviktig.")
elif (bmi >= 25 and bmi < 40):
    print("bmi = ", bmi, "du är överviktig.")
else: 
    print("bmi = ", bmi, "du är väldigt överviktig.")


# Uppgift 4
radius = float(input("Enter the radius: "))
circumference = radius * radius * 3.14
print(circumference)


# Uppgift 5
calculation_method = input("What calculation method would you like to use? \"+ - * /\" ")
number_1 = float(input("Enter a number: "))
number_2 = float(input("Enter another number: "))
if calculation_method == "+":
    print(number_1 + number_2)
elif calculation_method == "-":
    print(number_1 - number_2)
elif calculation_method == "/":
    print(number_1 / number_2)
elif calculation_method == "*":
    print(number_1 * number_2)

    
# Uppgift 6
print(random.randint(1, 6))

# Uppgift 7
throw_times = int(input("How many times would you like the dice to roll? "))
for i in range(throw_times):
    print(random.randint(1, 6))