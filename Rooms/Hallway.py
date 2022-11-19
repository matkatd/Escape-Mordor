from .Room import Room


class Hallway(Room):

    def __init__(self):
        super().__init__()

    def start_room(self):
        print(self.description)