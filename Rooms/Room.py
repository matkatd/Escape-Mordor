import POPO.Player as player


class Room:

    def __init__(self, name, description, items, next, previous, player):
        self.name = name
        self.description = description
        self.items = items
        self.next = next
        self.previous = previous
        self.player = player

    def listActions(self, item_index):
        valid = False
        while valid == False:
            print("You can take the following actions: ")
            x = 1
            print(f"0: nothing")
            for action in self.items[item_index]["actions"]:
                print(f"{x}: {action}")
                x += 1
            print("Select the number of the action you would like to take:")
            try:
                action_index = int(input()) - 1
                if (action_index > len(self.items[item_index])) or (action_index < 0):
                    print("Please enter an integer in the desired range")
                else:
                    valid = True
            except:
                print("Please enter an integer")
        return [
            self.items[item_index]["name"],
            self.items[item_index]["actions"][action_index],
            item_index
        ]

    def listItems(self):
        valid = False
        while valid == False:
            print("Notable items in the room include:")
            i = 1
            for item in self.items:
                print(f"{i}: {item['name']}")
                i += 1
            print("Select the number of the item you would like to interact with:")
            try:
                item_index = int(input()) - 1
                if (item_index > len(self.items)) or (item_index < 0):
                    print("Please enter an integer in the desired range")
                else:
                    valid = True
            except:
                print("Please enter an integer")
        toreturn = self.listActions(item_index)
        return toreturn
