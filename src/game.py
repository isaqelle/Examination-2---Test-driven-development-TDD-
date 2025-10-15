from dice import Dice
from intelligence import Intelligence
from player import Player
from highscore import HighScore


class Game:
    WINNING_SCORE = 10  # set to 10 for testing if you want

    def __init__(self):
        self.player = None
        self.computer = Player("Computer")
        self.dice = Dice()
        self.intelligence = Intelligence()
        self.highest_score = 0
        self.game_over = False
        self.highscores = HighScore()

        print("🐖 Welcome to Pig Game!")

    # ---------- MENUS ----------
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
            """\n🎲 Game rules:
Each turn, a player repeatedly rolls a die until a 1 is rolled or the player decides to 'hold':
- Rolling a 1 = lose turn points
- Rolling 2–6 = add to turn total
- 'Hold' = add turn total to score
First to reach 100 wins.\n"""
        )

    # ---------- GAME LOOP ----------
    def run(self):
        while True:
            self.menu()
            choice = input("Enter choice: ").strip()

            if choice == "1":
                print("Enter your name: ")
                name = input(">> ").strip()
                self.player = Player(name)
                print(f"Hello, {name}!")

            elif choice == "2":
                if not self.player:
                    print("Please create a player first!")
                    continue
                self.start_game()

            elif choice == "3":
                self.highscores.display_all()

            elif choice == "4":
                self.rules()

            elif choice == "5":
                print(f"Goodbye {self.player.name if self.player else 'Player'}!")
                break

            else:
                print("Invalid choice, try again.")

    # ---------- GAME START ----------
    def start_game(self):
        if not self.player:
            print("You need to create a player first!")
            return
        self.player.reset_score()
        self.computer.reset_score()
        self.game_over = False

        print("Select difficulty (Easy [E] / Hard [H]): ")
        difficulty = input(">> ").strip().lower()
        print(f"{'Hard' if difficulty == 'h' else 'Easy'} mode selected.\nLet's begin!")

        while not self.game_over:
            self.play_turn()
            if not self.game_over:
                self.computer_turn()

        if self.player.score > self.computer.score:
            print(f"🎉 {self.player.name} wins the match!")
        elif self.computer.score > self.player.score:
            print(f"💻 {self.computer.name} wins the match!")
        else:
            print("It's a tie!")

    # ---------- PLAYER TURN ----------
    def play_turn(self):
        print(f"\n{self.player.name}'s turn!")

        while True:
            print(
                f"{self.player.name}'s score: {self.player.score} | {self.computer.name}'s score: {self.computer.score}\n"
                "[R] Roll  |  [H] Hold  |  [C] Change name  |  [X] Exit match\n"
            )
            choice = input(">> ").strip().lower()

            if choice == "x":
                self.game_over = True
                print("Exiting current game...")
                return

            elif choice == "c":
                print("Enter new name: ")
                new_name = input(">> ").strip().lower()
                self.player.name = new_name
                print(f"Name changed to {new_name}")
                continue

            elif choice == "r":
                roll = self.dice.roll()
                
                print(f"{self.player.name} rolled: {roll}")

                if roll == 1:
                    print("Rolled a 1! You lose your turn points.")
                    return  # lose turn, pass to computer
                self.player.score += roll

                if self.player.score >= self.WINNING_SCORE:
                    print(f"🎉 {self.player.name} wins with {self.player.score} points! 🎉")
                    self.highscores.add_score(self.player.name, self.player.score)
                    self.game_over = True
                    return  # end turn and end game immediately

                else:
                    print(f"Total score: {self.player.score}\n")

            elif choice == "h":
                print(f"Held! Total score: {self.player.score}")
                if self.player.score >= self.WINNING_SCORE:
                    print(f"🎉 {self.player.name} wins with {self.player.score} points!")
                    self.highscores.add_score(self.player.name, self.player.score)
                    self.game_over = True
                return  # end of turn
            else:
                print("Invalid choice.")

    # ---------- COMPUTER TURN ----------
    def computer_turn(self):
        if self.game_over:
            return

        print("\n💻 Computer's turn!")
        turn_total = 0

        while True:
            roll = self.dice.roll()
            print(f"Computer rolled: {roll}")

            if roll == 1:
                print("Computer rolled a 1 — loses turn points.")
                return  # end turn

            turn_total += roll
            projected_score = self.computer.score + turn_total

            if projected_score >= self.WINNING_SCORE:
                self.computer.score = projected_score
                print(f"💻 Computer wins with {self.computer.score} points!")
                self.highscores.add_score("Computer", self.computer.score)
                self.game_over = True
                return

            if self.intelligence.should_hold(projected_score, self.player.score):
                self.computer.score = projected_score
                print(f"Computer holds at {self.computer.score} points.")
                return

            print("Computer rolls again...")
