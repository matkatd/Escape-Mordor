import utils
from Room import Room
from Hallway import Hallway


class Cell_Two(Room):

    def __init__(self, player):
        super().__init__(
            "Cell Two",
            "You find yourself in another jail cell. It's identical to yours- with two exceptions. On one wall there is a tapestry, and on the floor sleeps another prisoner.",
            [{
                "name": "sleeping prisoner",
                "actions": ["wake"]
            }, {
                "name": "torch on the wall",
                "actions": ["inspect", "pull"]
            }, {
                "name": "tapestry",
                "actions": ["inspect"]
            }, {
                "name": "cell door",
                "actions": ["open"]
            }, {
                "name": "passage back to your cell",
                "actions": ["exit"]
            }], 1, 2, player)

    def start_room(self):
        utils.print_line_of_char("#")
        utils.print_centered_text(self.name)
        utils.print_line_of_char("#")
        print(self.description)
        leave = False
        while leave == False:
            current_item = self.listItems()
            current_action = self.listActions()
            if current_item == "torch on the wall" and current_action == "pull":
                print("Nothing happened")
            if current_item == "sleeping prisoner" and current_action == "wake":
                start = Hallway(self.player)
                start.start_room()