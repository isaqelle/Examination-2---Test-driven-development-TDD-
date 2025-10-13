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
            userChoice = input("Enter choice: ")
            if userChoice == '1':
                name = input("Enter your name: ")
                print(f"Hello {name}")
                difficulty = input("Select level of difficulty, Easy [E] or Hard [H]: ")
                
                if difficulty.lower() == "e":
                    print("You picked an easy level!")
                elif difficulty.lower() == "h":
                    print("You picked a hard level")
                else:
                    print("Error")
                
            elif userChoice == '2':
                player_score = 0
                computer_score = 0
                while True:
                    print("play game")
                    print('Press "X" to exit the game or "P" to play.')
                    player_choice = input('>> ')
                    if player_choice.upper() == 'X':
                        break 
                    elif player_choice.upper() == 'P':
                        print('Player starts throwing dice')
                        my_dice = Dice()
                        player_result = my_dice.roll()
                        player_score += player_result
                        print(f'You rolled: {player_result}')
                        print(f'Your current score: {player_score}')

                        if player_result == 1:
                            print('Computers turn!')
                            computer_player = Intelligence()
                            computer_result = computer_player.should_hold(computer_score, player_score)
                            # computer_player += computer_result 
                            print(f'The computer rolled: {computer_result}')
                            print(f'Your current score: {computer_score}')
                            

                    if player_score >= 100 | computer_score >=100 :
                        break


            elif userChoice == '3':
                print("High score: ")

            elif userChoice == '4':
                print(f"Thank you for playing {name}!")
                break

        




