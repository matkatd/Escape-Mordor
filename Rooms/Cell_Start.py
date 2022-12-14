#standard imports
from datetime import datetime as dt
import utils
import Rooms.Room as Room
#room specific imports
# import Game as Game
import Rooms.Cell_Two as Cell_Two
import Rooms.Hallway as Hallway
import win_lose as win_lose


class Cell_Start(Room.Room):

    def __init__(self, player, starttime):
        super().__init__(
            f"{player.getName()}'s Cell",
            "You find yourself in a jail cell, three walls apear to be solid stone the third is the door. In one corner is a table with a flask, in the other lies a skeleton.",
            [{
                "name": "spooky scary skeleton",
                "actions": ["inspect", "greet"]
            }, {
                "name": "torch on the wall",
                "actions": ["inspect", "pull torch"]
            }, {
                "name": "ye olde flask",
                "actions": ["inspect", "drink", "get"]
            }, {
                "name": "cell door",
                "actions": ["open"]
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
            if current_item == "spooky scary skeleton":
                if current_action == "inspect":
                    print(
                        "It's a spooky scary skeleton... what did you expect?")
                if current_action == "greet":
                    print(
                        "The spooky scary skeleton rudely refuses to return your greeting..."
                    )
            if current_item == "torch on the wall":
                if current_action == "inspect":
                    print("Just a perfectly ordinary every day torch...")
                if current_action == "pull torch":
                    utils.print_centered_text(
                        "***A secret passage has apeared!***")
                    self.items.append({
                        "name": "secret passage",
                        "actions": ["exit"]
                    })
            if current_item == "ye olde flask":
                if current_action == "inspect":
                    print(
                        "A old flask lies upon a table, the liquid inside is murky and mysterious..."
                    )
                if current_action == "drink":
                    win_lose.end(
                        "You begin too feel woozy and suddenly you fall to the floor, darkness fills your vision...",
                        self.starttime)
                if current_action == "get":
                    self.items.pop(item_index)
                    self.player.insertItem(current_item)
                    utils.print_centered_text("*** You got ye olde flask ***")
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
                            "Your cell door is locked, maybe if you had a key..."
                        )
            if current_item == "secret passage" and current_action == "exit":
                start = Cell_Two.Cell_Two(self.player, self.starttime)
                start.start_room()
