import POPO.Player as player
class Room:

    def __init__(self, name, description, items, next, previous, player):
        self.name = name
        self.description = description
        self.items = items
        self.next = next
        self.previous = previous
        self.player = player

    def listItems(self):
        print("Notable items in the room include:")
        i = 1
        for item in self.items:
            print(f"{i}: {item['name']}")
            i += 1
        print("Select the number of the item you would like to interact with:")
        selected_item= input()
        x = i-1
        return self.items[x]["name"]

    def listActions(self, item_index):
        
        selection = input()
        
        return
        
