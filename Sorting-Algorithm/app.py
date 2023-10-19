import os
os.system("cls")
numbers = [2, 1]

for i in numbers:
    print(numbers)
    for k in numbers:
        if numbers[i-1] > numbers[k-1]:
            print(f"{numbers[i-1]} > {numbers[k-1]}")
            numbers[i-1] = numbers[k-1]
        elif numbers[i-1] < numbers[k-1]:
            print(f"{numbers[i-1]} < {numbers[k-1]}")
        elif numbers[i-1] == numbers[k-1]:
            print(f"{numbers[i-1]} = {numbers[k-1]}")

