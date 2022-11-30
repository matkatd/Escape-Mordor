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


def win(message, starttime):
    print(message)
    print(f"Total gametime elapsed: {dt.now() - starttime}")
    sys.exit()
    
def lose(message, starttime): #add playagsain/inventory reset
    bContinue = True
    print(message)
    print(starttime)
    play_again = input("Would you like to play again?\n(Enter Y to continue or press enter to exit:)").upper()
    while bContinue :
        if len(play_again) > 0 : 
            if play_again == 'Y' :
                game.run()
            else :
                play_again = input("Either type Y to play again or hit enter to exit.")
        else :
            sys.exit()

game = Game()
game.run()