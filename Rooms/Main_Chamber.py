from .Room import Room


class Main_Chamber(Room):

    def __init__(self):
        super().__init__()
        [{
            "name": "Guard Room Door",
            "actions": ["open"]
        }, {
            "name": "Armory Door",
            "actions": ["open"]
        }, {
            "name": "Exit Door",
            "actions": ["open"]
        }, {
            "name": "Cell Block Door",
            "actions": ["open"]
        }]
        self.description = "You find yourself in a jail cell..."

    def start_room(self):
        print(self.description)