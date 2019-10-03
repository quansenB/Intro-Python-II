# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, currrent_room):
        self.name = name
        self.current_room = currrent_room
        self.items = []

    def addItem(self, item):
        self.items.append(item)

    def dropItem(self, item):
        return self.items.remove(item)

    def printItems(self):
        string = "You have the following items in your inventory: "
        for item in self.items:
            string += item.name
            string += ", "
        string = string[:-2]
        print(string)