from .Room import Room
import utils
import POPO.Player as player

class Cell_Start(Room):

    def __init__(self):
        super().__init__("Your Cell", "You find yourself in a jail cell...",
                         [{
                             "name": "spooky scary skeleton",
                             "actions": ["inspect","greet"]
                         }, {
                             "name": "torch on the wall",
                             "actions": ["inspect", "pull"]
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
        self.listItems
