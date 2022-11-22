import utils
from .Room import Room
from .Cell_Two import Cell_Two
import POPO.Player as player


class Cell_Start(Room):

    def __init__(self, player):
        super().__init__(f"{player.getName()}'s Cell",
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
                         }], 0, 1, player)

    def start_room(self):
        utils.print_line_of_char("#")
        utils.print_centered_text(self.name)
        utils.print_line_of_char("#")
        print(self.description)
        leave = False
        while leave == False:
            [current_item, current_action, item_index] = self.listItems()
            if current_item == "spooky scary skeleton":
                if current_action == "inspect":
                    print("It's a spooky scary skeleton... what did you expect?")
                if current_action == "greet":
                    print("The spooky scary skeleton rudely refuses to return your greeting...")
            if current_item == "torch on the wall":
                if current_action == "inspect":
                    print("Just a perfectly ordinary every day torch...")
                if current_action == "pull torch":
                    print("A secret passage has apeared!")
                    self.items.append({
                        "name": "secret passage",
                        "actions": ["exit"]
                    })
            if current_item == "ye olde flask":
                if current_action == "inspect":
                    print("A old flask lies upon a table, the liquid inside is murky and mysterious...")
                if current_action == "drink":
                    print("You begin to feel woozy...")
                    self.items.pop(item_index)
                if current_action == "get":
                    print(f"You got {current_item}")
                    self.items.pop(item_index)
                    self.player.insertItem(current_item)
            if current_item == "cell door":
                if current_action == "open":
                    print("Your cell door is locked...")
            if current_item == "secret passage" and current_action == "exit":
                start = Cell_Two(player)
                start.start_room()
