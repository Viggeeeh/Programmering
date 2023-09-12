# Uppgift 1 
names = ["Greger", "Lisa", "Greta"]
for i in names:
    print(i)


# Uppgift 2
names[0] = "Axel"
print(names[0])


# Uppgift 3
names.append("Adolf")
for i in names:
    print(f"name: {i}")

# Uppgift 4
print(f"Det finns {len(names)} namn i listan")


# Uppgift 5
names.pop()
print(names)


# Uppgift 6 & 7
nameslist = []
print("/q to quit /delete to remove the last name")

while True:
    name = input("Enter a name: ")

    if name == "/q":
        break
    if name == "/delete":
        nameslist.pop()
    else:
        nameslist.append(name)

    print(nameslist)


# Uppgift 8 
favourite_car = [
{
    "brand": "Audi",
    "model": "R8",
    "year": "2013",
    "engine": "v10"   
},]

favourite_car.append({"brand": "Ford", "model": "Mustang", "year": "2015", "engine": "V8"})
print(favourite_car)