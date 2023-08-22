# Det här är min fina kommentar
"""Tjena
Johan
Hur är läget?"""

# Uppgift 2
print(5 + 2)
print(5 - 2)
print(5 * 2)
print(5 / 2)
print(5 // 2)
print(5 ** 2)
print(5 % 2)

# Uppgift 3
name = input("Vad är ditt namn? ")
age = int(input("Vad är din ålder? "))
print("Välkommen", name, "din ålder är", age)

# Uppgift 4
num_1 = float(input("Skriv ett nummer: "))
num_2 = float(input("Skriv ett till nummer: "))
sum = num_1 * num_2
print("Produkten utav", num_1, "och", num_2, "är", sum)

# Uppgift 5
weight = float(input("Vad väger du? (i KG): "))
height = float(input("Hur lång är du? (i Meter): "))
bmi = weight / height ** 2
print(bmi)

if (bmi <= 18.4):
    print("bmi = ", bmi, "du är underviktig.")
elif (bmi > 18.4 and bmi < 25):
    print("bmi = ", bmi, "du är normalviktig.")
elif (bmi >= 25 and bmi < 40):
    print("bmi = ", bmi, "du är överviktig.")
else: 
    print("bmi = ", bmi, "du är väldigt överviktig.")

# Uppgift 6
# (2023 - 2006) * 12 * 4
year_born = int(input("Viket år är du född? "))
age = 2023 - year_born
months_alive = age * 12
weeks_alive = months_alive * 4
print("Du har levt", weeks_alive)

# Uppgift 7
weight_kg = float(input("Skriv en vikt i kg: "))
converted_weight = weight_kg * 2.2
print(weight_kg, "in kg is", converted_weight, "in lbs")