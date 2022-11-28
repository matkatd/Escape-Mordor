from Rooms.Room import Room
import utils
import Rooms.Main_ChamberA as Main_Chamber


class Hallway(Room):

    def __init__(self, player):
        super().__init__(
            "Hallway",
            "You find yourself in the hallway of the cell block. There are many cells, including the one you just exited and the one you used to call your own. At the end of the hallway is the exit, but it appears to be locked. ",
            [{
                "name": "exit",
                "actions": ["inspect, unlock"]
            }, {
                "name": "open cell",
                "actions": ["enter"]
            }, {
                "name": "banner",
                "actions": ["inspect"]
            }, {
                "name": "cell door",
                "actions": ["open"]
            }, {
                "name": "passage back to your cell",
                "actions": ["exit"]
            }], 2, 3, player)

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
                start = Main_Chamber.Main_Chamber(self.player)
                start.start_room()