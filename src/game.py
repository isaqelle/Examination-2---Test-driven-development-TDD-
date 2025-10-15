from dice import Dice
from dicehand import DiceHand
from intelligence import Intelligence
from player import Player


class Game:
    def __init__(self):
        self.player = None
        self.player_score = 0
        self.computer_score = 0
        self.highest_score = 0
        self.game_over = False
        print("Welcome to Pig Game!")

    def menu(self):
        print(
            "\n---------- MENU ----------\n"
            "1. Create new player\n"
            "2. Play game\n"
            "3. Show Highscore\n"
            "4. Game Rules\n"
            "5. Quit\n"
        )

    def rules(self):
        print(
            """\nGame rules:
Each turn, a player repeatedly rolls a die until a 1 is rolled or the player decides to 'hold':
- If the player rolls a 1, they score nothing and it becomes the next player's turn.
- If the player rolls any other number, it is added to their turn total and the player's turn continues.
- If a player chooses to 'hold', their turn total is added to their score, and it becomes the next player's turn.
The first player to score 100 or more points wins.\n"""
        )

    def play_turn(self):
        """Handle player's turn."""
        print("\nYour turn!")
        turn_total = 0

        while True:
            roll = Dice().roll()
            print(f"You rolled: {roll}")

            if roll == 1:
                print("Rolled a 1! Turn over, you lose your turn points.")
                turn_total = 0
                break
            else:
                turn_total += roll
                print(f"Turn total: {turn_total}")
                print(f"{self.player.name}'s overall score: {self.player.score}")

            # Always show options to player after each roll
            print('\nPress:')
            print('  "H" to hold and keep your points')
            print('  "R" to roll again')
            print('  "C" to change your name')
            print('  "X" to exit game\n')

            choice = input(">> ").strip().lower()

            if choice == "x":
                print("Exiting game...")
                self.game_over = True
                return  # exit entire game
            elif choice == "c":
                new_name = input("Enter new name: ").strip()
                self.player.name = new_name
                print(f"Name changed to {new_name}")
                continue
            elif choice == "h":
                self.player.add_points(turn_total)
                self.player_score = self.player.score
                print(f"You hold with {turn_total} points.")
                print(f"Total score: {self.player_score}\n")

                if self.player_score >= 10:
                    print(f"\n🎉 {self.player.name} wins with {self.player_score} points! 🎉")
                    self.highest_score = max(self.highest_score, self.player_score)
                    self.game_over = True
                break
            elif choice == "r":
                continue
            else:
                print("Invalid input, rolling again...")

    def computer_turn(self):
        """Handle computer's turn."""
        print("\nComputer's turn!")
        comp = Intelligence()
        turn_total = 0

        while True:
            roll = Dice().roll()
            print(f"Computer rolled: {roll}")

            if roll == 1:
                print("Computer rolled a 1 and loses its turn points.\n")
                break

            turn_total += roll
            if self.computer_score + turn_total >= 10:
                self.computer_score += turn_total
                print(f"\n💻 Computer wins with {self.computer_score} points! 💻")
                self.game_over = True
                break

            decision = comp.should_hold(self.computer_score + turn_total, self.player_score)
            if decision:
                self.computer_score += turn_total
                print(f"Computer holds with {self.computer_score} total points.\n")
                break
            else:
                print("Computer rolls again...")

    def runGame(self):
        while True:
            self.menu()
            choice = input("Enter choice: ").strip()

            if choice == "1":
                name = input("Enter your name: ").strip()
                self.player = Player(name)
                print(f"Hello, {name}!")

            elif choice == "2":
                if not self.player:
                    print("You need to create a player first!")
                    continue

                difficulty = input("Select difficulty (Easy [E] / Hard [H]): ").strip().lower()
                if difficulty == "e":
                    print("Easy mode selected.")
                elif difficulty == "h":
                    print("Hard mode selected.")
                else:
                    print("Invalid difficulty. Defaulting to Easy.")

                self.player_score = 0
                self.computer_score = 0
                self.player.reset_score()
                self.game_over = False

                while not self.game_over:
                    print('\nPress "X" to exit, "P" to play, or "C" to change name.')
                    player_choice = input(">> ").strip().upper()

                    if player_choice == "X":
                        break
                    elif player_choice == "C":
                        new_name = input("Enter new name: ")
                        self.player.name = new_name
                        print(f"Name changed to {new_name}")
                    elif player_choice == "P":
                        self.play_turn()
                        if self.game_over:
                            break
                        self.computer_turn()
                    else:
                        print("Invalid option.")
                        
                print("\nGame over!")
                if self.player_score > self.computer_score:
                    print(f"{self.player.name} wins the match!")
                elif self.computer_score > self.player_score:
                    print("Computer wins the match!")
                else:
                    print("It's a tie!")

            elif choice == "3":
                print(f"Highest Score: {self.highest_score}")

            elif choice == "4":
                self.rules()

            elif choice == "5":
                if self.player:
                    print(f"Thank you for playing, {self.player.name}!")
                else:
                    print("Thank you for playing!")
                break

            else:
                print("Invalid menu choice.")
