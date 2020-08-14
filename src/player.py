# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, currentRoom):
        self.name = name
        self.currentRoom = currentRoom
        self.inventory = []

    def move(self, direction):
        next_room = getattr(self.currentRoom, f"{direction}_to")
        if next_room != None:
            self.currentRoom = next_room
        else:
            print("\nNot Allowed to go that way")

    def pickup_item(self, item):
        self.inventory.append(item)
        print(f'You picked up the {item.name}\n')

    def drop_item(self, item):
        self.inventory.remove(item)
        print(f'You dropped the {item.name}\n')

    def __str__(self):
        inventory_items= ''
        for item in self.inventory:
            inventory_items += f'\n{item}'
        return f"Your inventory items: {self.inventory_items}"