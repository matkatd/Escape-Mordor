#standard imports
import utils
import POPO.Player as player
from Rooms.Room import Room
#room specific imports
import Rooms.Hallway as Hallway
import Rooms.Armory as Armory
import Rooms.Guards_Room as Guards_Room

class Main_Chamber(Room):

    def __init__(self, player):
        super().__init__(
            "Main_Chamber",
            "You find yourself in a large chamber...",
            [{
                "name": "Guard Room Door",
                "actions": ["inspect","open"]
            }, {
                "name": "Armory Door",
                "actions": ["inspect","open"]
            }, {
                "name": "Exit Door",
                "actions": ["open"]
            }, {
                "name": "Cell Block Door",
                "actions": ["open"]
            }], player)

    def start_room(self):
        utils.print_line_of_char("#")
        utils.print_centered_text(self.name)
        utils.print_line_of_char("#")
        print(self.description)
        leave = False
        while leave == False:
            current_item = self.listItems()
            current_action = self.listActions()
            if current_item == "":
                if current_action == "":
                    pass