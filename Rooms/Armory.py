#standard imports
import utils
import Rooms.Room as Room
#room specific imports
import Rooms.Main_Chamber as Main_Chamber

class Armory(Room.Room):

    def __init__(self, player):
        super().__init__(
            "Armory",
            "You find yourself in the armory...",
            [{
                "name": "weapons chest",
                "actions": ["inspect", "open"]
            }, {
                "name": "torch on the wall",
                "actions": ["inspect", "pull"]
            }, {
                "name": "drunk guard",
                "actions": ["inspect", "talk"]
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