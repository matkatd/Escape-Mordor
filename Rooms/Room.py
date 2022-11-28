import POPO.Player as player


class Room:

    def __init__(self, name, description, items, next, previous, player):
        self.name = name
        self.description = description
        self.items = items
        self.player = player

    def listActions(self, item_index):
        valid_b = False
        while valid_b == False:
            print("You can take the following actions: ")
            x = 1
            print(f"0: nothing")
            for action in self.items[item_index]["actions"]:
                print(f"{x}: {action}")
                x += 1
            print("Select the number of the action you would like to take:")
            try: 
                action_index = int(input())
                action_count = len(self.items[item_index]["actions"])
                if (action_index > action_count) or (action_index < 0):
                    print(f"Please enter an integer in the desired range: ({0}-{action_count})")
                elif action_index == 0:
                    return [self.items[item_index]["name"],"nothing",item_index]
                else:
                    action_index = action_index - 1
                    valid_b = True
            except:
                print("Please enter an integer")
        return [
            self.items[item_index]["name"],
            self.items[item_index]["actions"][action_index],
            item_index
        ]

    def listItems(self):
        valid_a = False
        while valid_a == False:
            print("Notable items in the room include:")
            i = 1
            for item in self.items:
                print(f"{i}: {item['name']}")
                i += 1
            print("Select the number of the item you would like to interact with:")
            try:
                item_index = int(input())
                item_count = len(self.items)
                if (item_index > item_count) or (item_index < 1):
                    print(f"Please enter an integer in the desired range: ({1}-{item_count})")
                else:
                    item_index = item_index - 1
                    valid_a = True
            except:
                print("Please enter an integer")
        toreturn = self.listActions(item_index)
        return toreturn
