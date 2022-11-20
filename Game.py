from Rooms.Cell_Start import Cell_Start

import utils
import POPO.Player as Player

class Game:

    def run(self):
        utils.print_line_of_char("-")
        utils.print_centered_text("THE DUNGEONS OF MORDOR")
        utils.print_centered_text("\u00a92022 Mordor's IT Department")
        utils.print_line_of_char("-")
        print("Welcome to the Dungeons of Mordor adventurer! Are you ready for what awaits?")
        print("(Enter your name to start, press enter to quit)")
        name = input()
        if len(name) > 0:
            # character = Player()
            # character.setName(name)
            start = Cell_Start()
            start.start_room()
        else:
            print("Farewell!")
            return


game = Game()
game.run()