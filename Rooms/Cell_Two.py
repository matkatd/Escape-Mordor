import utils
from .Room import Room


class Cell_Two(Room):

    def __init__(self):
        super().__init__()
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
        }]
        self.description = "You find yourself in another jail cell. It's identical to yours- with two exceptions. On one wall there is a tapestry, and on the floor sleeps another prisoner."

    def start_room(self):
        utils.print_line_of_char("#")
        utils.print_centered_text(self.name)
        utils.print_line_of_char("#")
        print(self.description)