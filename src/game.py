from dice import Dice
from dicehand import DiceHand
from intelligence import Intelligence
from player import Player

class Game:
    print("Welcom to Pig Game!")
    def menu(self):
        
        # name = input("Enter your name: ")
        # print(f"Hello {name}")
        print(
            "---------- MENU ----------\n"
            "1. Create new player\n"
            "2. Play game\n"
            "3. Show Highscore\n"
            "4. Quit\n"
        )

        while True:
            userChoice = int(input("Enter choice: "))
            if userChoice == 1:
                name = input("Enter your name: ")
                print(f"Hello {name}")
                difficulty = input("Select level of difficulty, Easy [E] or Hard [H]: ")
                
                if difficulty.lower() == "e":
                    print("You picked an easy level!")
                elif difficulty.lower() == "h":
                    print("You picked a hard level")
                else:
                    print("Error")
                
            elif userChoice == 2:
                print("play game")
                
            elif userChoice == 3:
                print("High score: ")

            elif userChoice == 4:
                print(f"Thank you for playing {name}!")
                break

        




