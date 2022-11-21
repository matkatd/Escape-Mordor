from .Room import Room
from Rooms.Cell_Two import Cell_Two
import utils
import POPO.Player as player

class Cell_Start(Room):

    def __init__(self, player):
        super().__init__(f"{player.getName()}'s Cell", "You find yourself in a jail cell...",
                         [{
                             "name": "spooky scary skeleton",
                             "actions": ["inspect","greet"]
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
            current_item = self.listItems()
            current_action = self.listActions()
            if current_item == "torch on the wall" and current_action == "pull torch":
                print("A secret passage has apeared!")
                self.items.append({"name":"secret passage", "actions":["exit"]})
            if current_item == "secret passage" and current_action == "exit":
                start = Cell_Two(player)
                start.start_room()
            
                

