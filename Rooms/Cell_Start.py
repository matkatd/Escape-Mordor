from .Room import Room


class Cell_Start(Room):

    def __init__(self):
        super().__init__("Cell Start", "You find yourself in a jail cell...",
                         [{
                             "name": "spooky scary skeleton",
                             "actions": ["action1"]
                         }, {
                             "name": "torch on the wall",
                             "actions": ["inspect", "pull"]
                         }], 0, 1)

    def start_room(self):
        print(self.description)
