# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self, roomName, description, items=[]):
        self.roomName = roomName
        self.description = description
        self.items = items
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    def __str__(self):
        room_items = ''
        for item in self.items:
            room_items += f'\n{item}'
        return f"{self.roomName}\n\n{self.description}. Items in the this room : {room_items}"
