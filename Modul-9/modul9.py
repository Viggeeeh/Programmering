# Uppgift 1-3
import os

question = input("Skriv något: ")
textfile = "./Modul-9/test.txt"

file_exists = os.path.exists(textfile)

if not file_exists:
    print("Inget Sparat")
    with open(textfile, "x") as f:
        f.write(question)
else:
    with open(textfile, "a") as f:
        f.write(f"\n{question}")


with open(textfile) as f:
    print(f.read())

# Uppgift 4-5
import json

json_file = "./Modul-9/test.json" 
data = {
    "score": "1",
    "user_name": "offan"
}

with open(json_file, "w") as file:
    json.dump(data, file)