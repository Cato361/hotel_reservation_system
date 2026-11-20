"""Hotel Module: manages rooms, guests, and reservations."""

from room import Room
from guest import Guest
from reservation import Reservation


class HotelSystem:
    """Central system that stores and manages all hotel data."""

    def __init__(self, data_file="hotel_data.json"):
        """Creates a new hotel system object."""
        self.rooms = []
        self.guests = []
        self.reservations = []
        self.data_file = data_file

    def add_room(self, room: Room):
        """Adds a room to the hotel system."""
        self.rooms.append(room)

    def add_guest(self, guest: Guest):
        """Adds a guest to the hotel system."""
        self.guests.append(guest)

    def list_available_rooms(self):
        """Returns a list of all available rooms."""
        available_rooms = []
        for room in self.rooms:
            if room.is_available:
                available_rooms.append(room)
        return available_rooms


if __name__ == "__main__":
    hotel_system = HotelSystem()
    hotel_system.add_room(Room(1, "single", 80.0))
    hotel_system.add_room(Room(2, "double", 100.0))
    hotel_system.add_room(Room(3, "double", 100.0))

    hotel_system.rooms[0].book_room()

    for room in hotel_system.list_available_rooms():
        print(room.get_details())
        