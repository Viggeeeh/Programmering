# Uppgift 1
"""
x = input("Skriv något: ")
for i in range(10):
    print(x)

# Uppgift 2
for i in range(10):
    print(i+1)

# Uppgift 3 
y = int(input("Säg ett nummer: "))
for i in range(y):
    print(i+1)
"""
# Uppgift 4
num = float(input("Säg ett nummer: "))
for i in range(10):
    print(num * (i + 1))



# Uppgift 5
# 2^1 => 2*1
# 2^2 => 2*2
# 2^3 => 2*2*2 => 

# Kan inte ta cred för denna uppgift, löste 50% sen gav upp.
x = 2

for i in range(6):
    y = 1
    for j in range(i+1):
        y *= x
    