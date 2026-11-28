"""Reservation module for a hotel reservation system"""

from guest import Guest
from room import Room


class Reservation:
    """Represents a reservation that links a guest to a room."""

    def __init__(self, reservation_id, guest, room, nights):
        """Create new reservation."""
        self.reservation_id = reservation_id
        self.guest = guest
        self.room = room
        self.nights = nights
        self.status = "active"
        self.total_price = self.calculate_total()

    def calculate_total(self):
        """Return total price of the reservation."""
        return self.nights * self.room.price_per_night

    def cancel_reservation(self):
        """Cancel reservation and make the room available."""
        if self.status == "cancelled":
            raise ValueError(
                f"Reservation {self.reservation_id} already cancelled"
            )

        self.status = "cancelled"
        self.room.free_room()

    def get_summary(self):
        """Return a short text summary of the reservation."""
        return (
            f"Reservation {self.reservation_id} | "
            f"{self.guest.full_name} | "
            f"Room {self.room.room_number} | "
            f"{self.nights} nights | "
            f"{self.total_price} EUR | "
            f"{self.status}"
        )

    def to_dict(self):
        """Return a dictionary representation of the reservation."""
        return {
            "reservation_id": self.reservation_id,
            "guest_id": self.guest.guest_id,
            "room_number": self.room.room_number,
            "nights": self.nights,
            "total_price": self.total_price,
            "status": self.status
        }


if __name__ == "__main__":

    room = Room(101, "Double", 120.0)
    guest = Guest(1, "John Doe", "123456789", "john@example.com")

    room.book_room()

    reservation = Reservation(1, guest, room, 3)

    print(reservation.get_summary())

    reservation.cancel_reservation()

    print(reservation.get_summary())
    print(room.get_details())

    try:
        reservation.cancel_reservation()
    except ValueError as error:
        print("Error:", error)
