"""Hotel Module: manages rooms, guests, and reservations."""

import json

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

    def find_room(self, room_number):
        """Returns the room with the given number."""
        for room in self.rooms:
            if room.room_number == room_number:
                return room
        return None

    def find_guest(self, guest_id):
        """Returns the guest with the given ID."""
        for guest in self.guests:
            if guest.guest_id == guest_id:
                return guest
        return None

    def find_reservation(self, reservation_id):
        """Returns the reservation with the given ID."""
        for reservation in self.reservations:
            if reservation.reservation_id == reservation_id:
                return reservation
        return None

    def create_reservation(self, guest_id, room_number, nights):
        """Create a new reservation and mark the room as reserved."""
        if nights < 1:
            raise ValueError("Number of nights must be at least 1.")


        guest = self.find_guest(guest_id)
        room = self.find_room(room_number)

        if guest is None or room is None:
            raise ValueError("Guest or room not found.")

        room.book_room()
        reservation_id = len(self.reservations) + 1
        reservation = Reservation(reservation_id, guest, room, nights)
        self.reservations.append(reservation)
        return reservation

    def cancel_reservation(self, reservation_id):
        """Cancel an existing reservation."""
        reservation = self.find_reservation(reservation_id)
        if reservation is None:
            raise ValueError("Reservation not found.")
        reservation.cancel_reservation()

    def save_to_file(self):
        """Save all rooms, guests and reservations to the JSON file."""
        rooms_data = []
        for room in self.rooms:
            rooms_data.append(room.to_dict())

        guests_data = []
        for guest in self.guests:
            guests_data.append(guest.to_dict())

        reservations_data = []
        for reservation in self.reservations:
            reservations_data.append(reservation.to_dict())

        data = {
            "rooms": rooms_data,
            "guests": guests_data,
            "reservations": reservations_data
        }

        with open(self.data_file, "w") as file:
            json.dump(data, file, indent=4)

    def load_from_file(self):
        """Load all rooms, guests and reservations from the JSON file.
        If the file does not exist, stays empty.
        """
        try:
            with open(self.data_file, "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            print("No saved data found. Starting with an empty hotel.")
            return

        self.rooms = []
        for item in data["rooms"]:
            room = Room(
                item["room_number"],
                item["room_type"],
                item["price_per_night"],
                item["is_available"]
            )
            self.rooms.append(room)

        self.guests = []
        for item in data["guests"]:
            guest = Guest(
                item["guest_id"],
                item["full_name"],
                item["phone"],
                item["email"]
            )
            self.guests.append(guest)

        self.reservations = []
        for item in data["reservations"]:
            guest = self.find_guest(item["guest_id"])
            room = self.find_room(item["room_number"])
            reservation = Reservation(
                item["reservation_id"], guest, room, item["nights"]
            )
            reservation.status = item["status"]
            self.reservations.append(reservation)


if __name__ == "__main__":
    hotel_system = HotelSystem("test_hotel.json")

    hotel_system.add_room(Room(1, "single", 80.0))
    hotel_system.add_room(Room(2, "double", 100.0))
    hotel_system.add_room(Room(3, "double", 100.0))

    hotel_system.rooms[0].book_room()

    hotel_system.add_guest(
        Guest(1, "John Doe", "123456789", "john@example.com")
    )

    hotel_system.create_reservation(1, 2, 3)

    hotel_system.cancel_reservation(1)

    hotel_system.save_to_file()

    new_hotel = HotelSystem("test_hotel.json")
    new_hotel.load_from_file()

    print("Rooms:")
    for room in new_hotel.rooms:
        print(room.get_details())

    print("Reservations:")
    for reservation in new_hotel.reservations:
        print(reservation.get_summary())