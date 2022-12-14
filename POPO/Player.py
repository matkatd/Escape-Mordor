class Player:

    def __init__(self):
        self.items = []
        self.hallway_cipher = False

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def insertItem(self, item):
        self.items.append(item)

    def deleteItem(self, item):
        self.items.remove(item)

    def isInItems(self, item):
        if (self.items.count(item) >= 1):
            return True
        else:
            return False

    def getItems(self):
        return self.items
