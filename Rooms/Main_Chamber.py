#standard imports
from datetime import datetime as dt 
import utils
import Rooms.Room as Room
#room specific imports
import Rooms.Hallway as Hallway
import Rooms.Armory as Armory
import Rooms.Guards_Room as Guards_Room
import Puzzles.hangman as hangman

class Main_Chamber(Room.Room):

    def __init__(self, player, starttime):
        super().__init__(
            "Main_Chamber",
            "You find yourself in a large chamber, in each wall there is a door. In the far wall is the door to the armory, in the wall to the left is the door to the guards room, in the wall to your right is the door to the outside world. Various machines rest haphazerdly about the room, some glow with heat others lay dormant. In one corner is a gallows, presumably for prisoners like you. Besides the gallows, with their back to you, stands the excecutioner.",
            [{
                "name": "hallway door",
                "actions": ["open"]
            }, {
                "name": "armory door",
                "actions": ["open"]
            }, {
                "name": "guard's room door",
                "actions": ["open"]
            }, {
                "name": "door to outside",
                "actions": ["open"]
            }, {
                "name": "gallows",
                "actions": ["inspect"]
            }, {
                "name": "excecutioner",
                "actions":["inspect", "talk"]
            }], player, starttime)

    def start_room(self):
        utils.print_line_of_char("#")
        utils.print_centered_text(self.name)
        utils.print_line_of_char("#")
        print(f"Gametime elapsed: {dt.now() - self.starttime}")
        print(self.description)
        leave = False
        while leave == False:
            [current_item, current_action, item_index] = self.listItems()
            if current_item == "hallway door":
                if current_action == "open":
                    start = Hallway.Hallway(self.player, self.starttime)
                    start.start_room()
            if current_item == "armory door":
                if current_action == "open":
                    start = Armory.Armory(self.player, self.starttime)
                    start.start_room()
            if current_item == "guard's room door":
                if current_action == "open":
                    if self.player.IsInItems(""):
                        start = Guards_Room.Guards_Room(self.player, self.starttime)
                        start.start_room()
            if current_item == "door to outside":
                if current_action == "open":
                    if self.player.isInItems("master key"):
                        print("YOU HAVE ESCAPED!")
                        #Win condition goes here
                    else:
                        print("The door is locked, you didn't think it would be that easy did you...")
            if current_item == "gallows":
                if current_action == "inspect":
                    print("Just your ordinary gallows, they look quite well cared for though...")
            if current_item == "executioner":
                if current_action == "inspect":
                    print("The excecutioner appears to not have noticed your entrance, they are standing with their back to you, mending a noose from the gallows.")
                if current_action == "talk":
                    if self.player.isInItems("guard's uniform"):
                        print("Excecutioner: 'Hello there, have you heard of the new security protocol? (Cackles) If you don't know the password you hang! Don't remember? Care to guess? Of course you do!'")
                        win = hangman.play_game()
                        if win == True:
                            print("Congradulations!")
                        else:
                            print("You lost!")
                            #lose func call goes here
                            pass
                    else:
                        print("Excecutioner: 'You're an escaped prisoner! GUARDS! GUARDS!'")
                        #lose func call goes here