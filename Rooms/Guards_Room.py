#standard imports
from datetime import datetime as dt 
import utils
import Rooms.Room as Room
#room specific imports
import Rooms.Main_Chamber as Main_Chamber
import Puzzles.guards_room_puzzle as guards_room_puzzle
import win_lose as win_lose

class Guards_Room(Room.Room):

    def __init__(self, player, starttime):
        super().__init__(
            "Guards Room",
            "You find yourself in the guards quarters. The room contains several cots for tired guards. On one cot the guard captain reclines. In one corner there is a table with a strange orb. Besides that the room is sparsly furnished.",
            [{
                "name": "mysterious orb",
                "actions": ["inspect"]
            }, {
                "name": "empty cot",
                "actions": ["inspect", "rest"]
            }, {
                "name": "guard captain",
                "actions": ["inspect","talk"]
            }, {
                "name": "table",
                "actions": ["move","look under"]
            }, {
                "name": "door to main chamber",
                "actions": ["open"]
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
            if current_item == "mysterious orb":
                if current_action == "inspect":
                    win_lose.end("Oh no that orb was a palantir, the visions it shows you temprorarly drive you mad, when you awake you are back in your cell. YOU HAVE FAILED TO ESCAPE THE DUNGEONS OF MORDOR", self.starttime)
            if current_item == "empty cot":
                if current_action == "inspect":
                    print("A pillow and a blanket! Looks comfy!")
                if current_action == "rest":
                    print("zZzZz\nzZzZz\nzZzzZz\nVery restful!")
            if current_item == "guard captain":
                if current_action == "inspect":
                    print("He looks fairly compotent, on one hip rests his sword...")
                if current_action == "talk":
                    if self.player.isInItems("sword"):
                        print("Guard Captain: 'You want to go outside? For that you would need the master key, and only the guard captain may hold the master key. WHAT! YOU DARE CHALLENGE ME! Prepare yourself!'")
                        fight = guards_room_puzzle.Fight()
                        win = fight.start()
                        if win == True:
                            print("You have won! On the guard captain's body you find the master key!")
                            utils.print_centered_text("*** You got the master key ***")
                            self.player.insertItem("master key")
                            self.items.pop(item_index)
                        else:
                            win_lose.end("The guard captain defeats you. YOU HAVE FAILED TO ESCAPE THE DUNGEONS OF MORDOR!", self.starttime)
                    else:
                        win_lose.end("You challenged the captain of the guard without a weapon, he runs you through instantly. YOU HAVE FAILED TO ESCAPE THE DUNGEONS OF MORDOR!", self.starttime)
            if current_item == "table":
                if current_action == "move":
                    print("The table is too heavy to move, this is why we don't skip leg day..")
                if current_action == "look under":
                    print("On the underside of the table someone has scratched a message:\n 'Made you look!'")