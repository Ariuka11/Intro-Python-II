from room import Room
from player import Player
from item import Item
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance", "North of you, the cave mount beckons", [Item("Shield", "Gives you an Armor.")]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""",  [Item("Sword", "Arthur sword")]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",  [Item("Helmet", "A long lived hero's helmet")]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""",  [Item("Bow", "Mongolian bow")]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""",  [Item("Pot of Gold", "The treasure that you have been looking for..")]),
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
player_name = input("What is your name?\n")
new_player = Player(player_name, room['outside'])

directions = ["n", "s", "e", "w", "q"]


def commands():
    for command in directions.items():
        print(f"{command}")


print(f"Welcome, {new_player.name}")
print("Command: [q] exit the game, [n,s,e,w] to move around and [g] to grab the item, [d] to drop the item ")

# Write a loop that:

# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
while True:
    cmd = input("\nWhere do you want to go?\n").lower()
    if cmd == "q":
        print("Thanks for playing")
        quit()
    elif cmd in directions:
        new_player.move(cmd)
        print(f"\nYou are in: The {new_player.currentRoom}")

    elif cmd == 'g':
        if len(new_player.currentRoom.items) == 0:
            cmd = input(
                'There are no more items to pick up. Please make your next move:\n')
        else:
            new_player.pickup_item(new_player.currentRoom.items[0])
            new_player.currentRoom.remove_item(new_player.currentRoom.items[0])
    elif cmd == 'd':
        if len(new_player.inventory) < 1:
            cmd = input(
                'You have no items to drop. Please make your next move:\n')
        else:
            new_player.currentRoom.add_item(new_player.inventory[0])
            new_player.drop_item(new_player.inventory[0])
    elif cmd == 'r':
        new_player.inventory
    else:
        print("Invalid Input")
