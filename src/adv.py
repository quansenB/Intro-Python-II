from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player("Inaki", room["outside"])

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.


def move(direction):
    newRoom = getattr(player.current_room, f"{direction}_to")
    if newRoom is not None:
        player.current_room = newRoom
        global printCondition
        printCondition = True
    else:
        print("There is no room in this direction, please choose another direction or q to end game")


endCondition = False
printCondition = True

while endCondition is not True:
    if(printCondition):
        print(
            f"\nYou are in the room {player.current_room.name}: {player.current_room.description}")
        direction = input(
            "Choose the direction you want to go (n/e/s/w) or press q to exit the game:").lower()
        printCondition = False
    else:
        direction = input(
            "Choose the direction you want to go (n/e/s/w) or press q to exit the game:").lower()

    if direction == "q":
        endCondition = True
        print("\nThank you for playing, see you next time")
    elif direction == "n" or direction == "e" or direction == "s" or direction == "w":
        move(direction)
    else:
        print(
            "This is not a valid direction. Please choose n, e, s or w. To end game type q")


""" while True:
    print(
        f"\nYou are in the room {player.current_room.name}: {player.current_room.description}")
    direction = input(
        "Choose the direction in which you want to go (n/e/s/w):").lower()

    def move(direction):
        try:
            newRoom = getattr(player.current_room, f"{direction}_to")
            if newRoom is not None:
                player.current_room = newRoom
            else:
                direction = input(
                    "You cannot go there, please select another direction (n/e/s/w):").lower()
        except: 
            print("here")
            direction = input("Invalid input, select n, e, s or w:").lower()

    while not (direction == "n" or direction == "e" or direction == "s" or direction == "w"):
        print("here")
        direction = input("Invalid input, select n, e, s or w:").lower()
    else:
        move(direction) """
