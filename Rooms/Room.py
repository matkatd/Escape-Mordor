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
        print("You can take the following actions: ")
        x = 1
        for action in self.items[item_index]["actions"]:
            print(f"{x}: {action}")
            x += 1
        print("Select the number of the action you would like to take:")
        action_index = int(input())-1
        return [self.items[item_index]["name"], self.items[item_index]["actions"][action_index]]

    def listItems(self):
        print("Notable items in the room include:")
        i = 1
        for item in self.items:
            print(f"{i}: {item['name']}")
            i += 1
        print("Select the number of the item you would like to interact with:")
        item_index = int(input())-1
        toreturn =  self.listActions(item_index)
        return toreturn
