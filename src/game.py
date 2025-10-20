"""Module to define the Game class for the Pig Dice Game."""

from .dice import Dice
from .intelligence import Intelligence
from .player import Player
from .highscore import HighScore

TITLE = "🐖  P I G   G A M E  🐖"
WIDTH = 53

class Game:
    """A class to represent a Pig Dice Game session."""

    WINNING_SCORE = 10  # set to 10 for testing purposes

    def __init__(self):
        """Initialize a new game session, including player, computer, dice,
        AI, and highscore tracking. Also prints the game title banner.
        """
        self.player = None
        self.computer = Player("Computer")
        self.dice = Dice()
        self.intelligence = Intelligence()
        self.highest_score = 0
        self.game_over = False
        self.highscores = HighScore()
        self.width = WIDTH

        print("\n╔" + "═" * WIDTH + "╗")
        print("║" + " " * WIDTH + "║")
        print("║" + TITLE.center(WIDTH - 2) + "║")
        print("║" + " " * WIDTH + "║")
        print("╚" + "═" * WIDTH + "╝")

    # ---------- MENUS ----------
    def menu(self):
        """Display the main game menu with options for creating a player,
        starting the game, viewing high scores, reading game rules, or quitting.
        """
        print("\n╔" + "═" * WIDTH + "╗")
        print("║" + " " * WIDTH + "║")
        print("║" + "1) Create new Player".center(WIDTH) + "║")
        print("║" + "2) Play Game".center(WIDTH) + "║")
        print("║" + "3) Show Highscore".center(WIDTH) + "║")
        print("║" + "4) Game Rules".center(WIDTH) + "║")
        print("║" + "5) Quit".center(WIDTH) + "║")
        print("║" + " " * WIDTH + "║")
        print("╚" + "═" * WIDTH + "╝")

    def rules(self):
        """Display the game rules in a formatted ASCII frame.

        Explains how turns work, scoring, and how to win.
        """
        print("╔" + "═" * WIDTH + "╗")
        print("║" + " " * WIDTH + "║")
        print("║" + "🎲 GAME RULES".center(WIDTH - 1) + "║")
        print("║" + "Each turn, a player repeatedly rolls a die until".center(WIDTH) + "║")
        print("║" + "a 1 is rolled or the player decides to 'hold':".center(WIDTH) + "║")
        print("║" + "- Rolling a 1 = lose turn points".center(WIDTH) + "║")
        print("║" + "- Rolling 2–6 = add to turn total".center(WIDTH) + "║")
        print("║" + "- 'Hold' = add turn total to score".center(WIDTH) + "║")
        print("║" + "First to reach 100 wins.".center(WIDTH) + "║")
        print("║" + " " * WIDTH + "║")
        print("╚" + "═" * WIDTH + "╝")

    # ---------- GAME LOOP ----------
    def run(self):
        """Run the main game loop.

        Displays menus and handles user choices: create player, start game,
        show highscores, view rules, or quit the application.
        """
        while True:
            self.menu()
            print("Enter choice:")
            choice = input(">> ").strip()

            if choice == "1":
                while True:
                    print("Enter your name: ")
                    name = input(">> ").strip()
                    if not name:
                        print("Name cannot be null.")
                        continue
                    self.player = Player(name)
                    print(f"Player created, welcome {name}!")
                    break

            elif choice == "2":
                if not self.player:
                    print("Please create a player first!")
                    continue
                self.start_game()
                continue

            elif choice == "3":
                self.highscores.display_all()
                continue

            elif choice == "4":
                self.rules()
                continue

            elif choice == "5":
                print(f"Goodbye {self.player.name if self.player else 'Player'}!")
                break

            else:
                print("Invalid choice, try again.")

    # ---------- GAME START ----------
    def start_game(self):
        """Handle the human player's turn.

        Displays the current scores, provides choices to Roll, Hold, Change name,
        or Exit match. Updates scores and checks for winning conditions.
        """
        if not self.player:
            print("You need to create a player first!")
            return

        self.player.reset_score()
        self.computer.reset_score()
        self.game_over = False

        while True:
            print("Select difficulty (Easy [E] / Hard [H]): ")
            difficulty = input(">> ").strip().lower()
            if difficulty not in ("e", "h"):
                print("Please select [E] or [H]")
                continue
            break

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
        """Handle the human player's turn."""
        print(f"\n{self.player.name}'s turn!")

        while True:
            print("\n╔" + "═" * (WIDTH + 14) + "╗")
            print(
                "║"
                + f"{self.player.name}'s score: {self.player.score} | "
                f"{self.computer.name}'s score: {self.computer.score}".center(WIDTH + 14)
                + "║"
            )
            print("╚" + "═" * (WIDTH + 14) + "╝")
            print("\n╔" + "═" * (WIDTH + 14) + "╗")
            print("║" + " " * (WIDTH + 14) + "║")
            print(
                "║"
                + "[R] Roll  |  [H] Hold  |  [C] Change name  |  [X] Exit match".center(
                    WIDTH + 14
                )
                + "║"
            )
            print("║" + " " * (WIDTH + 14) + "║")
            print("╚" + "═" * (WIDTH + 14) + "╝")
            print("")
            choice = input(">> ").strip().lower()

            if choice == "x":
                self.game_over = True
                print("Exiting current game...")
                return

            if choice == "c":
                print("Enter new name: ")
                new_name = input(">> ").strip().lower()
                self.player.name = new_name
                print(f"Name changed to {new_name}")
                continue

            if choice == "r":
                roll = self.dice.roll()
                print(f"{self.player.name} rolled: {roll}")

                if roll == 1:
                    print("Rolled a 1! You lose your turn points.")
                    return

                self.player.score += roll

                if self.player.score >= self.WINNING_SCORE:
                    print(f"🎉 {self.player.name} wins with {self.player.score} points! 🎉")
                    self.highscores.add_score(self.player.name, self.player.score)
                    self.game_over = True
                    return

                print(f"Total score: {self.player.score}\n")
                continue

            if choice == "h":
                print(f"Held! Total score: {self.player.score}")
                if self.player.score >= self.WINNING_SCORE:
                    print(f"🎉 {self.player.name} wins with {self.player.score} points!")
                    self.highscores.add_score(self.player.name, self.player.score)
                    self.game_over = True
                return

            print("Invalid choice.")

    # ---------- COMPUTER TURN ----------
    def computer_turn(self):
        """Execute the computer player's turn using AI logic."""
        if self.game_over:
            return

        print("\n💻 Computer's turn!")
        turn_total = 0

        while True:
            roll = self.dice.roll()
            print(f"Computer rolled: {roll}")

            if roll == 1:
                print("Computer rolled a 1 — loses turn points.")
                return

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
