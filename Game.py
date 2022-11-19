from Rooms.Cell_Start import Cell_Start


class Game:

    def run(self):
        print("THE DUNGEONS OF MORDOR\n\u00a92022 Mordor's IT Department\n\nWelcome to the dungeons of Mordor adventurer!")
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