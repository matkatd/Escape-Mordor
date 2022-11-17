import Room


class Guards_Room(Room):

    def __init__(self):
        super().__init__()
        [{
            "name": "spooky scary skeleton",
            "actions": ["action1"]
        }, {
            "name": "torch on the wall",
            "actions": ["inspect", "pull"]
        }]
        self.description = "You find yourself in a jail cell..."

    def start_room(self):
        print(self.description)