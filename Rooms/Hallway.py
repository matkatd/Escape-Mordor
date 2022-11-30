#standard imports
from datetime import datetime as dt
import utils
import Rooms.Room as Room
#room specific imports
import Rooms.Cell_Start as Cell_Start
import Rooms.Cell_Two as Cell_Two
import Rooms.Main_Chamber as Main_Chamber
import Puzzles.hallway_cipher as cipher
import win_lose as win_lose


class Hallway(Room.Room):

    def __init__(self, player, starttime):
        super().__init__(
            "Hallway",
            "You find yourself in the hallway of the cell block. There are many cells, including the gollum's and the your's. At the end of the hallway is the exit, but it appears to be locked.",
            [{
                "name": "hallway exit",
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
            }, {
                "name": "rat",
                "actions": ["say hello", "attempt to capture"]
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

            if current_item == "hallway exit":
                if current_action == "inspect":
                    print(
                        "The exit is a large door, the locking mechanism appears to require some sort code..."
                    )
                if current_action == "open":
                    if self.player.hallway_cipher == True:
                        valid = False
                        while not valid:
                            answer = input(
                                "Enter the three digit combination: ")
                            if answer == "201":
                                valid = True
                                start = Main_Chamber.Main_Chamber(
                                    self.player, self.starttime)
                                start.start_room()

                    else:
                        print(
                            "The mechanism is too complex to pick, you'll need the combination to unlock"
                        )
            if current_item == "gollum's cell":
                if current_action == "inspect":
                    print("Gollum appears to have gone back to sleep...")
                if current_action == "open":
                    start = Cell_Two.Cell_Two(self.player, self.starttime)
                    start.start_room()
            if current_item == f"{self.player.getName()}'s cell":
                if current_action == "inspect":
                    print("Your cell appears much smaller from the outside...")
                if current_action == "open":
                    start = Cell_Start.Cell_Start(self.player, self.starttime)
                    start.start_room()
            if current_item == "tapestry":
                if current_action == "inspect":
                    print("Maze clue2")
                if current_action == "lift corner":
                    win = cipher.cipher_solver()
                    if win:
                        self.player.hallway_cipher = True
                        print(
                            "You may want to look at the door at the end of the hallway..."
                        )
            if current_item == "rat":
                if current_action == "say hello":
                    print(
                        "The rat stares at you with a questioning look, as if it's judging your intelligence\nYou feel uncomfortable and walk away."
                    )
                if current_action == "attempt to capture":
                    answer = input(
                        "Are you sure you want to do this? It may have rabies: (Y/N)"
                    )
                    if answer.upper() == "Y":
                        win_lose.end(
                            "The rat didn't vibe with your feeble attempts to capture it.\nIt bites you.\nAfter a moment, you feel the effects of infection and black out.\nThe end...",
                            self.starttime)
                    if answer.upper() == "N":
                        print(
                            "The rat scurries into another corner of the room")
