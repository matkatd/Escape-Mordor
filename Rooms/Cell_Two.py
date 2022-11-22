import utils
from .Room import Room
from .Cell_Start import Cell_Start
from .Hallway import Hallway
import POPO.Player as player
import Puzzles.riddle as riddle

class Cell_Two(Room):

    def __init__(self, player):
        super().__init__(
            "Cell Two",
            "You find yourself in another jail cell. It's identical to yours- with two exceptions. On one wall there is a tapestry, and on the floor sleeps another prisoner.",
            [{
                "name": "sleeping prisoner",
                "actions": ["inspect","wake"]
            }, {
                "name": "torch on the wall",
                "actions": ["inspect", "pull"]
            }, {
                "name": "ragged tapestry",
                "actions": ["inspect", "lift corner"]
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
            [current_item, current_action, item_index] = self.listItems()
            if current_item == "sleeping prisoner":
                if current_action == "inspect":
                    print("This prisoner appears to be quite well fed, their sleep is quite peacefull...")
                if current_action == "wake":
                    win = riddle.read_riddle()
                    if win == True:
                        self.player.insertItem("cell key")
            if current_item == "torch on the wall":
                if current_action == "inspect":
                    print("Just a perfectly ordinary every day torch...")
                if current_action == "pull torch":
                    print("Nothing happened")
            if current_item == "ragged tapestry":
                if current_action == "inspect":
                    pass #maze clue?
                if current_action == "lift corner":
                    print("Upon lifting the tapestry, bemneath you find the following message: 'Not everything is a clue you know...'")
            if current_item == "cell door":
                if current_action == "open":
                    if self.player.isInItems("cell key"):
                        print("You use the key to unlock the cell door and enter the hallway beyond...")
                        start = Hallway(player)
                        start.start_room()
                    else:
                        print("The cell door is locked, maybe if you had a key...")
            if current_item == "passage back to your cell":
                if current_action == "exit":
                    start = Cell_Start(player)
                    start.start_room()
