#standard imports
import utils
import Rooms.Room as Room
#room specific imports
import Rooms.Hallway as Hallway
import Rooms.Armory as Armory
import Rooms.Guards_Room as Guards_Room

class Main_Chamber(Room.Room):

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
            [current_item, current_action, item_index] = self.listItems()
            if current_item == "":
                if current_action == "":
                    pass