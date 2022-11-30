#standard imports
from datetime import datetime as dt 
import utils
import Rooms.Room as Room
#room specific imports
import Rooms.Main_Chamber as Main_Chamber
import Puzzles.guards_room_puzzle as guards_room_puzzle

class Guards_Room(Room.Room):

    def __init__(self, player, starttime):
        super().__init__(
            "Guards Room",
            "You find yourself in the guards quarters...",
            [{
                "name": "guard captain",
                "actions": ["inspect","talk"]
            }, {
                "name": "table",
                "actions": ["move","look under"]
            }, {
                "name": "door to main chamber",
                "actions": ["open"]
            }], player, starttime)

    def start_room(self):
        utils.print_line_of_char("#")
        utils.print_centered_text(self.name)
        utils.print_line_of_char("#")
        print(f"Gametime elapsed: {dt.now() - self.starttime}")
        print(self.description)
        leave = False
        while leave == False:
            [current_item, current_action, item_index] = self.listItems()
            if current_item == "guard captain":
                if current_action == "inspect":
                    print("")
                if current_action == "talk":
                    print("pre-script")
                    win = guards_room_puzzle.fight()
                    if win == True:
                        print("You have won! For your troubles you have recieved a master key")
                        utils.print_centered_text("*** You got the master key ***")
                        self.player.insertItem("master key")
                        self.items.pop(item_index)
                    else:
                        pass
            if current_item == "table":
                if current_action == "move":
                    print("The table is too heavy to move, this is why we don't skip leg day..")
                if current_action == "look under":
                    print("On the underside of the table someone has scratched a message:\n 'Made you look!'")