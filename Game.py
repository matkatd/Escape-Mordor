import Rooms.Room
import Rooms.Cell_Start as Cell_Start
import utils
from POPO.Player import Player


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
            start = Cell_Start.Cell_Start(player)
            start.start_room()
        else:
            print("Farewell!")
            return


game = Game()
game.run()