score = 0

question_one = int(input("Hur gammal är Viggo? "))
if (question_one == 17):
    score += 1
else:
    print("Du hade fel")

question_two = input("Vilken månad fyller Viggo år? (skriv med små bokstäver) ")
if (question_two == "mars"):
    score += 1
else: 
    print("Du hade fel")

question_three = input("Vad heter Viggos tjej? (skriv med små bokstäver) ")
if (question_three == "emma"):
    score += 1
else: 
    print("Du hade fel")

print("Du hade", score, "/ 3 rätt.")