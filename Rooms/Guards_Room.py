#standard imports
from datetime import datetime as dt 
import utils
import Rooms.Room as Room
#room specific imports
import Rooms.Main_Chamber as Main_Chamber

class Guards_Room(Room.Room):

    def __init__(self, player, starttime):
        super().__init__(
            "Guards Room",
            "You find yourself in the guards quarters...",
            [{
                "name": "guard captain",
                "actions": ["inspect","talk"]
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
            if current_item == "":
                if current_action == "":
                    pass