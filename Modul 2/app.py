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
