import Rooms.Cell_Start as Cell_Start
import utils
from POPO.Player import Player
from datetime import datetime as dt 
import sys


class Game:

    def run(self):
        utils.print_line_of_char("-")
        utils.print_centered_text("THE DUNGEONS OF MORDOR")
        utils.print_centered_text("\u00a92022 Mordor's IT Department")
        utils.print_line_of_char("-")
        print(
            "Welcome to the dungeons of Mordor adventurer, are you ready for what awaits?"
        )
        print("(Enter your name to start, press enter to quit)")
        name = input()
        if len(name) > 0:
            player = Player()
            player.setName(name)
            starttime = dt.now()
            start = Cell_Start.Cell_Start(player, starttime)
            start.start_room()
        else:
            print("Farewell!")
            return

    def win(self, message, starttime):
        print(message)
        print(f"Total gametime elapsed: {dt.now() - starttime}")
        sys.exit()
    
    def lose(self, message, starttime):
        print(message)
        sys.exit()


game = Game()
game.run()