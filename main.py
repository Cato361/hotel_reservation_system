
"""Main module: text menu for the hotel reservation system."""

from room import Room
from guest import Guest
from hotel_system import HotelSystem


def show_menu():
    """Print the main menu."""
    print("\n===== HOTEL RESERVATION MENU =====")
    print("1 - List available rooms")
    print("2 - Add a new guest")
    print("3 - Create a reservation")
    print("4 - List all reservations")
    print("5 - Cancel a reservation")
    print("6 - Save and exit")


def get_int(prompt):
    """Ask the user for a whole number until a valid one is entered.

    Args:
        prompt (str): The text shown to the user.

    Returns:
        int: The number the user typed.
    """
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a number, not letters.")


def add_sample_rooms(hotel_system):
    """Add some rooms so the program is usable on the first run."""
    hotel_system.add_room(Room(1, "single", 80.0))
    hotel_system.add_room(Room(2, "double", 100.0))
    hotel_system.add_room(Room(3, "double", 100.0))


def main():
    """Run the hotel menu until the user chooses to exit."""
    hotel_system = HotelSystem()
    hotel_system.load_from_file()

    if len(hotel_system.rooms) == 0:
        add_sample_rooms(hotel_system)

    while True:
        show_menu()
        choice = get_int("Your choice: ")

        try:
            if choice == 1:
                available_rooms = hotel_system.list_available_rooms()

                if len(available_rooms) == 0:
                    print("There are no available rooms.")

                for room in available_rooms:
                    print(room.get_details())

            elif choice == 2:
                guest_id = len(hotel_system.guests) + 1
                name = input("Full name: ")
                phone = input("Phone: ")
                email = input("Email: ")

                hotel_system.add_guest(
                    Guest(guest_id, name, phone, email)
                )
                print(f"Guest added with ID {guest_id}.")

            elif choice == 3:
                guest_id = get_int("Guest ID: ")
                room_number = get_int("Room number: ")
                nights = get_int("Number of nights: ")

                reservation = hotel_system.create_reservation(
                    guest_id, room_number, nights
                )
                print("Reservation created:", reservation.get_summary())

            elif choice == 4:
                if len(hotel_system.reservations) == 0:
                    print("There are no reservations yet.")

                for reservation in hotel_system.reservations:
                    print(reservation.get_summary())

            elif choice == 5:
                reservation_id = get_int("Reservation ID to cancel: ")
                hotel_system.cancel_reservation(reservation_id)
                print(f"Reservation {reservation_id} cancelled.")

            elif choice == 6:
                hotel_system.save_to_file()
                print("Data saved. Goodbye!")
                break

            else:
                print("Invalid choice. Please choose 1-6.")

        except ValueError as error:
            print("Error:", error)


if __name__ == "__main__":
    main()
