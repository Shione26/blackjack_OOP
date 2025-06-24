from game_class import Game

def main():
    while True:
        game = Game()
        game.start()

        # exit program
        new_game = input("\nPlay another hand? [Y/N] ")
        while new_game.lower() not in ["y", "n"]:
            new_game = input("Invalid Input. Please enter 'y' or 'n' ")

        if new_game.lower() != "y":
            print("\n------------------------Thanks for playing!---------------------\n")
            break

if __name__ == "__main__":
    main()