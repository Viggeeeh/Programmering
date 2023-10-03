import os
os.system("cls")

suits = {
    "clubs": "♣",
    "diamonds": "♦", 
    "hearts": "♥", 
    "spades": "♠"
}

cards = [
]

for i in range(13):
    for k in range(4):
        cards.append([i+1]) # begins from 1



for i in range(13):
    for k in range(4):
        if k == 0:
            cards[i] += suits["clubs"] 
        elif k == 1:
            cards[i] += suits["diamonds"] 
        elif k == 2:
            cards[i] += suits["hearts"] 
        elif k == 3:
            cards[i] += suits["spades"] 

print(cards)


