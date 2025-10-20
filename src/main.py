"""Main module to start and run the Pig Dice Game."""

from .game import Game

def main():
    """Start and run the Pig Dice Game."""
    game = Game()
    game.run()


if __name__ == "__main__":
    main()
