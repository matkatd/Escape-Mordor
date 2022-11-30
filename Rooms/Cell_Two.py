#standard imports
from datetime import datetime as dt 
import utils
import Rooms.Room as Room
#room specific imports
import Rooms.Cell_Start as Cell_Start
import Rooms.Hallway as Hallway
import Puzzles.riddle as riddle
from Game import lose


class Cell_Two(Room.Room):

    def __init__(self, player, starttime):
        super().__init__(
            "Gollum's cell",
            "You find yourself in another jail cell. It's identical to yours- with two exceptions. On one wall there is a tapestry, and on the floor sleeps another prisoner.",
            [{
                "name": "sleeping prisoner",
                "actions": ["inspect", "wake"]
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
            if current_item == "sleeping prisoner":
                if current_action == "inspect":
                    print(
                        "This prisoner appears to be quite well fed, their sleep is quite peaceful..."
                    )
                if current_action == "wake":
                    win = riddle.read_riddle()
                    if win == True:
                        self.player.insertItem("cell key")
                    else :
                        lose('You were eaten by Gollum and failed to escape the dungeons of Mordor.', f'Game Time elapsed: {dt.now() - self.starttime}')
                        pass
            if current_item == "torch on the wall":
                if current_action == "inspect":
                    print("Just a perfectly ordinary every day torch...")
                if current_action == "pull torch":
                    print("Nothing happened")
            if current_item == "ragged tapestry":
                if current_action == "inspect":
                    pass  #maze clue?
                if current_action == "lift corner":
                    print(
                        "Upon lifting the tapestry, bemneath you find the following message: 'Not everything is a clue you know...'"
                    )
            if current_item == "cell door":
                if current_action == "open":
                    if self.player.isInItems("cell key"):
                        print(
                            "You use the key to unlock the cell door and enter the hallway beyond..."
                        )
                        start = Hallway.Hallway(self.player, self.starttime)
                        start.start_room()
                    else:
                        print(
                            "The cell door is locked, maybe if you had a key..."
                        )
            if current_item == "passage back to your cell":
                if current_action == "exit":
                    start = Cell_Start.Cell_Start(self.player, self.starttime)
                    start.start_room()
