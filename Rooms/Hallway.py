#standard imports
import utils
import Rooms.Room as Room
#room specific imports
import Rooms.Cell_Start as Cell_Start
import Rooms.Cell_Two as Cell_Two
import Rooms.Main_Chamber as Main_Chamber

class Hallway(Room.Room):

    def __init__(self, player):
        super().__init__(
            "Hallway",
            "You find yourself in the hallway of the cell block. There are many cells, including the one you just exited and the one you used to call your own. At the end of the hallway is the exit, but it appears to be locked.",
            [{
                "name": "Hallway exit",
                "actions": ["inspect", "open"]
            }, {
                "name": "gollum's cell",
                "actions": ["inspect", "open"]
            }, {
                "name": f"{player.getName()}'s cell",
                "actions": ["inspect", "open"]
            }, {
                "name": "tapestry",
                "actions": ["inspect", "lift corner"]
            }], player)

    def start_room(self):
        utils.print_line_of_char("#")
        utils.print_centered_text(self.name)
        utils.print_line_of_char("#")
        print(self.description)
        leave = False
        while leave == False:
            [current_item, current_action, item_index] = self.listItems()
            if current_item == "hallway exit":
                if current_action == "":
                    pass
            if current_item == "gollum's cell":
                if current_action == "":
                    pass
            if current_item == f"{self.player.getName()}'s cell":
                if current_action == "":
                    pass
            if current_item == "tapestry":
                if current_action == "":
                    pass
            