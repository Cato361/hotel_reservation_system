
"""room module for a simple reservation system"""
class Room:
    """represents a room in the reservation system"""
    def __init__ (self, room_number, room_type, price_per_night, is_available = True ) :

        self.room_number = room_number
        self.room_type = room_type
        self.price_per_night = price_per_night
        self.is_available = is_available

    def book_room(self):
        if not self.is_available:
            raise ValueError(f"room {self.room_number} is already booked")
        self.is_available = False

    def free_room(self):
        self.is_available = True


    def get_details(self):
        status= "not booked" if self.is_available else "booked"
        return f"{self.room_number}: {status}"


    def to_dict(self):
        return {
            "room_number": self.room_number,
            "room_type": self.room_type,
            "price_per_night": self.price_per_night,
            "is_available": self.is_available
        }




