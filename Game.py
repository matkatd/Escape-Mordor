import sys
from pathlib import Path

# sys.path.insert("/Rooms/Cell_Start")
from Rooms.Cell_Start import Cell_Start


class Game:

    def run(self):
        print("Welcome to the Jungle, we've got fun and games")
        print("Press 'Y' to start, any other key to quit")
        key = input()
        if key == 'Y':
            start = Cell_Start()
            start.start_room()
        else:
            print("Goodbye!")
            return


game = Game()
game.run()