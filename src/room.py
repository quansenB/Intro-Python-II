# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, description, n_to=None, e_to=None, s_to=None, w_to=None):
        self.name = name
        self.description = description
        self.n_to = n_to
        self.e_to = e_to
        self.s_to = s_to
        self.w_to = w_to
        self.items = []

    def addItem(self, item):
        self.items.append(item)

    def takeItem(self, item):
        return self.items.remove(item)

    def printItems(self):
        string = "In this room you can take the following items: "
        for item in self.items:
            string += item.name
            string += ", "
        string = string[:-2]
        print(string)
