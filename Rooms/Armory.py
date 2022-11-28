from Rooms.Room import Room
import utils
import POPO.Player as player

class Armory(Room):

    def __init__(self, player):
        super().__init__(
            "Armory",
            "You find yourself in the armory...",
            [{
                "name": "spooky scary skeleton",
                "actions": ["action1"]
            }, {
                "name": "torch on the wall",
                "actions": ["inspect", "pull"]
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