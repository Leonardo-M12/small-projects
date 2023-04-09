"""The main game. Everything is inside the MainGame class. 
   Contains the game map, the game engine and the parser.
"""

from Classes import *
from sys import exit
import time


class MainGame:
    """The main game class. Contains:
       - Game map: a dictionary mapping each keyword to its corresponding
         location class.
       - Instantiates Link class as self.player.
       - Then, comes the game engine, which shows the intro, allows the parser
         to take input, and when the player arrives to SFM, shows the ending.
       - Parser: takes input from the player. Allows for manual help commands
         and has some easter eggs.
    """

    def __init__(self):
        self.game_map = {
            "KF": KokiriForest(),
            "LW-1": LostWoods1(),
            "LW-2": LostWoods2(),
            "LW-3": LostWoods3(),
            "LW-4": LostWoods4(),
            "LW-5": LostWoods5(),
            "LW-6": LostWoods6(),
            "LW-7": LostWoods7(),
            "GC": GoronCity(),
            "SFM": SacredForestMeadow()
        }

        self.player = Link()

        # Beginning of the game.

        KokiriForest().intro()

        time.sleep(5)

        while True:
            # Show description and name of the place.
            print(self.player.location)
            print()
            print(self.player.location.description)
            print()

            # The player makes a move, parser processes, changes location.
            self.player.location = self.parser(self.player.location)
            print()

            """If the player arrives to the Sacred Forest Meadow, execute
               SFM code, and end the game.
            """
            if isinstance(self.player.location, SacredForestMeadow):
                print(self.player.location)
                print()
                print(self.player.location.description)
                print()

                time.sleep(2)
                
                # Ending.
                SacredForestMeadow().ending()

                exit()



    def parser(self, LocationSubclass):
        """Takes input from the player when selecting where to move in the
           game. Returns a valid entry, which will be used by the main
           class.
        """

        while True:
            user_choice = input("> ")

            user_choice = user_choice.lower()

            if user_choice == "help":
                print("""
Select a direction to move to (north, south, east, west), type 'exit' to exit 
the game, or type 'description' to see the description of the place you are in.
""")

            elif user_choice == "exit":
                exit()

            elif user_choice == "description":
                print()
                print(self.player.location)
                print()
                print(self.player.location.description)
                print()
                continue

            # Now, easter eggs.

            elif user_choice == "navi":
                print("Hello!")
                continue

            elif user_choice == "ganon" or user_choice == "ganondorf":
                print("The Great King of Evil, at your service.")
                continue

            elif user_choice not in LocationSubclass.adj_places.keys():
                print("Choose a valid entry.")
                continue

            else:
                
                # Translate input to tuple, defined in each location class.
                user_choice_tuple = self.player.location.adj_places[user_choice]

                input_message = user_choice_tuple[1]

                if not input_message: 
                    # Translate directly to the corresponding location.
                    user_choice = self.game_map[user_choice_tuple[0]]
                    return user_choice

                else:
                    print(input_message)
                    print("Are you sure? (y/n)\n")

                    # User validation loop.
                    while True:
                        user_confirmation = input("> ")
                        if user_confirmation.lower() == "y":
                            # The user is sure. Translate.
                            user_choice = self.game_map[user_choice_tuple[0]]
                            return user_choice
                        elif user_confirmation.lower() == "n":
                            # Begin all the input cycle again.
                            print("Choose a move.\n")
                            break
                        else:
                            print("Write 'y' for yes or 'n' for no.")
                            continue


if __name__ == '__main__':
    MainGame()