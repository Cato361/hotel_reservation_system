
"""room module for a simple reservation system"""
class Room:
    """represents a room in the reservation system"""
    def __init__ (self, room_number, room_type, price_per_night, is_available = True ) :
        """Initializes a room with its details and availability status."""

        self.room_number = room_number
        self.room_type = room_type
        self.price_per_night = price_per_night
        self.is_available = is_available

    def book_room(self):
        """Books the room if it is available."""
        if not self.is_available:
            raise ValueError(f"room {self.room_number} is already booked")
        self.is_available = False

    def free_room(self):
        """Makes the room available for booking."""
        self.is_available = True


    def get_details(self):
        """Returns the room number and booking status."""
        status= "not booked" if self.is_available else "booked"
        return f"{self.room_number}: {status}"


    def to_dict(self):
        """Returns the room information as a dictionary."""
        return {
            "room_number": self.room_number,
            "room_type": self.room_type,
            "price_per_night": self.price_per_night,
            "is_available": self.is_available
        }


if __name__ == "__main__":


    room1 = Room(101, "Single", 80)


    print(room1.get_details())


    room1.book_room()
    print(room1.get_details())


    try:
        room1.book_room()
    except ValueError as error:
        print("Error:", error)


    room1.free_room()
    print(room1.get_details())


    print(room1.to_dict())



