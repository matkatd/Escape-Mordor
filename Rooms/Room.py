class Room:

    def __init__(self, name, description, items, next, previous):
        self.name = name
        self.description = description
        self.items = items
        self.next = next
        self.previous = previous

    def listItems(self):
        print("Notable items in the room include:")
        i = 1
        for item in self.items:
            print(i + ": " + item)
            i += 1
        print("Select the number of the item you would like to interact with")

    def listActions(self, item_index):
        selection = input()
