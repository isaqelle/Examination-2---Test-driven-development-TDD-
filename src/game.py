from dice import Dice
from dicehand import DiceHand
from intelligence import Intelligence
from player import Player

class Game:
    player_score = 0 
    
    # computer_score = 0
    # name = ""
    print("Welcom to Pig Game!")

    def menu(self):
            
            # name = input("Enter your name: ")
            # print(f"Hello {name}")
            print(
                "---------- MENU ----------\n"
                "1. Create new player\n"
                "2. Play game\n"
                "3. Show Highscore\n"
                "4. Game Rules\n"
                "5. Quit\n"
            )

    def rules(self):
         print("""Game rules:\nEach turn, a player repeatedly rolls a die until a 1 is rolled or the player decides to 'hold':
If the player rolls a 1, they score nothing and it becomes the next player's turn.
If the player rolls any other number, it is added to their turn total and the player's turn continues.
If a player chooses to 'hold', their turn total is added to their score, and it becomes the next player's turn.
The first player to score 100 or more points wins.\n""")
         

    def runGame(self):
        player_score = 0 
        computer_score = 0
        name = ""
        highest_score = 0
        player = None

        while True:
            self.menu()
            userChoice = input("Enter choice: ")

            if userChoice == '1':
                name = input("Enter your name: ")
                player = Player(name)
                print(f"Hello {name}")
                
                
            elif userChoice == '2':
                    while True:
                        if name == "":
                            print("You need to enter your name before playing")
                            name = input("Enter your name: ")
                            print(name)
                            
                        else:
                             break


                
                    difficulty = input("Select level of difficulty, Easy [E] or Hard [H]: ")
                
                    if difficulty.lower() == "e":
                        print(f"{name} picked an easy level!")
                    elif difficulty.lower() == "h":
                        print(f"{name} picked a hard level")
                    else:
                        print("Error")
                    while True:
                        print('\nPress "X" to exit the game or "P" to play or press "C" to change name.')
                    
                        player_choice = input('>> ')
                        if player_choice.upper() == 'X':
                            break 
                        elif player_choice.upper() == 'P':
                            print('Player starts throwing dice')
                            turn_over = False
                            while not turn_over:
                                player_result = Dice().roll()
                                print(f"{name} rolled: {player_result}")

                                if player_result == 1:
                                    print("ROlled 1! Turn over.")
                                    turn_over = True
                                else:
                                   playResult = player.add_points(player_result)
                                   player_score = player.score
                                   print(f"{name}'s current score: {playResult}")

                                   hold = input("Press H to hold, any other to keep playing")
                                   if hold.strip().lower() == "h":
                                       turn_over = True

                            if player_result > highest_score:
                                highest_score += player_result
                            
                                # player_score += player_result
                                # playerscores = Player(name)
                                # playResult = playerscores.add_points(player_score)
                                # player_score += playResult
                             
                            print(f'{name} rolled: {player_result}')
                            print(f"{name}'s current score: {player_score}")

                            print("\nComputer's turn!")
                            computer_player = Intelligence()
                            while True:
                                computer_result = Dice().roll()
                                computer_score += computer_result
                                print(f"The computer rolled: {computer_result}")
                                print(f"Comupter curret score: {computer_score}\n")

                                decision = computer_player.should_hold(computer_score, player_score)
                                if decision:
                                    print("Computer decides to hold this turn\n")
                                    break
                                else:
                                    print("Computer decides to roll again.")

                        elif player_choice.upper() == "C":
                            name = input("Enter new name: ")
                            print(f"New name set to: {name}\n")
                                
                        # CHANGE LATER TO 100
                        if player_score >= 10 or computer_score >=10 :
                            break
            # CHANGE LATER TO 100
            if player_score >= 10:
                new_highscore = player_score
                print(f"{name} wins!\nScore: {new_highscore}")
            elif computer_score >= 10:
                print("Computer Agnetha wins")

            elif userChoice == '3':
                print("High score: ")
                print(f"Your highscore: {new_highscore}")

            elif userChoice == '4':
                self.rules()    
            elif userChoice == '5':
                print(f"Thank you for playing {name}!")
                break

        




