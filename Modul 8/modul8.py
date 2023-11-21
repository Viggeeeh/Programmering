import datetime
import time
import os
from msvcrt import getwch

# Uppgift 1-3
"""
print("Press any button", end="")

if getwch():
    os.system("cls")

while True:
    current_date = datetime.datetime.now()
    print(f"Todays Date: {current_date.strftime('%D')}")
    print(f"Current Time: {current_date.strftime('%H:%M:%S')}")
    time.sleep(1)
    os.system("cls")
"""

# Uppgift 4
"""
counter = 0
minute = 0
hour = 0

print("Press Any Button to Begin the Timer ", end="")

if getwch():
    os.system("cls")
    while True:
        if counter == 59:
            minute += 1
            counter = 0

        if minute == 59:
            hour += 1
            minute = 0
            counter = 0

        counter += 1

        print(f"{hour}:{minute}:{counter}")
        time.sleep(1)
        os.system("cls")
"""


# Uppgift 6
"""
year = int(input("Skriv ett år: "))
month = int(input("Skriv en månad (1-12): "))
date = int(input("Skriv ett datum: "))

date_time = datetime.datetime(year, month, date)

while True:
    os.system("cls")
    current_date = datetime.datetime.now()
    result = date_time - current_date
    print(result)
    time.sleep(1)
"""