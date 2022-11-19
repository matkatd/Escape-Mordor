class Player:

    def __init__(self):

        self.items = []

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def insertItem(self, item):
        self.items.append(item)

    def isInItems(self, item):
        if (item.count(item) > 0):
            return True
        else:
            return False

    def getItems(self):
        return self.items
