#standard imports
from datetime import datetime as dt 
import utils
import Rooms.Room as Room
#room specific imports
import Rooms.Main_Chamber as Main_Chamber
import Puzzles.armory_sequence as armory_sequence

class Armory(Room.Room):

    def __init__(self, player, starttime):
        super().__init__(
            "Armory",
            "You find yourself in the armory. Against the far wall rests a large weapons chest, above it is a bracket holding three torches. In one corner a sleeping guard rests. To your left hangs a guard's uniform'. To your right hangs a pair of crossed axes.",
            [{
                "name": "weapons chest",
                "actions": ["inspect", "open"]
            }, {
                "name": "torch bracket",
                "actions": ["inspect", "interact"]
            }, {
                "name": "sleeping guard",
                "actions": ["inspect", "talk"]
            }, {
                "name": "crossed axes",
                "actions": ["inspect", "get"]
            }, {
                "name": "guard's uniform",
                "actions": ["inspect", "get"]
            }, {
                "name": "door back to main chamber",
                "actions": ["exit"]
            }], player, starttime)

    def start_room(self):
        utils.print_line_of_char("#")
        utils.print_centered_text(self.name)
        utils.print_line_of_char("#")
        print(f"Gametime elapsed: {dt.now() - self.starttime}")
        print(self.description)
        open = False
        leave = False
        while leave == False:
            [current_item, current_action, item_index] = self.listItems()
            if current_item == "weapons chest":
                if current_action == "inspect":
                    print("An undiscript chest with no visable locking mechanism")
                if current_action == "open":
                    if open == True:
                        if self.player.isInItems("sword"):
                            print("The chest is empty...")
                        else:
                            print("Upon opening the chest you find a sword")
                            utils.print_centered_text("*** You got a sword ***")
                            self.player.insertItem("sword")
                    else:
                        print("The chest is locked...")
            if current_item == "torch bracket":
                if current_action == "inspect":
                    print("A inconspicous torch bracket with three torches...")
                if current_action == "interact":
                    open = armory_sequence.pull_torches()
                    if open == True:
                        print("You hear a loud click from the chest below...")
                    else:
                        print("Nothing happened...")
            if current_item == "sleeping guard":
                if current_action == "inspect":
                    print("A guard lies sleeping in the corner, based on his current condition and the pile of empty bottles around him, he seeems to like a good drink...")
                if current_action == "talk":
                    print("Guard: 'WHAT! I wasn't asleep on duty... I would like a drink though...'")
                    self.items.pop(item_index)
                    self.items.append({
                        "name": "thirsty guard",
                        "actions": ["talk", "give drink"]
                    })
            if current_item == "thirsty guard":
                if current_action == "talk":
                    print("Guard: 'I wish I had a drink...'")
                if current_action == "give drink":
                    if self.player.isInItems("ye olde flask"):
                        print("Guard: 'Thank you kindly! By the way if you need a weapon from the weapons chest, you need to pull the torches in the torch bracket in the following order: '")
                        print("1. LEFT")
                        print("2. LEFT")
                        print("3. RIGHT")
                        print("4. LEFT")
                        print("5. MIDDLE")
                        print("6. RIGHT")
                    else:
                        print("You don't have a drink to give the guard...")
            if current_item == "crossed axes":
                if current_action == "inspect":
                    print("On the wall hangs a pair of crossed axes, they seem to be tied to the wall with some wire...")
                if current_action == "get":
                    print("The axes are stuck to the wall...")
            if current_item == "guard's uniform":
                if current_action == "inspect":
                    print("On the wall hangs a fresh guard's uniform...")
                if current_action == "get":
                    self.player.insertItem("guard's uniform")
                    self.items.pop(item_index)
                    utils.print_centered_text("*** You got a guard's uniform ***")
            if current_item == "door back to main chamber":
                if current_action == "exit":
                    start = Main_Chamber.Main_Chamber(self.player, self.starttime)
                    start.start_room()