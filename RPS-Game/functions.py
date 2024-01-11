from symbols import symbols
import random

class functions:
    def AI():
        choice = random.randint(1, 3)
        if choice == 1:
            print(f"AI Chose:{symbols.rock}")
            result = "R"
        elif choice == 2:
            print(f"AI Chose:{symbols.paper}")
            result = "P"
        elif choice == 3:
            print(f"AI Chose:{symbols.scissors}")
            result = "S"
            
        return result
    
    def win_conditions(player_choice, AI_choice):
        # Rock beats Scissors
        if player_choice == "R" and AI_choice == "S":
            print("\nYou Won!")
        elif AI_choice == "R" and player_choice == "S":
            print("\nYou Lost...")
        # Scissors beats Paper
        elif player_choice == "S" and AI_choice == "P":
            print("\nYou Won!")
        elif AI_choice == "S" and player_choice == "P":
            print("\nYou Lost...")
        # Paper beats Rock
        elif player_choice == "P" and AI_choice == "R":
            print("\nYou Won!")
        elif AI_choice == "P" and player_choice == "R":
            print("\nYou Lost...")
        # Tie
        elif AI_choice == player_choice:
            print("\nIt's a tie!")

