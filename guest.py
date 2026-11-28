
"""Guest module for a hotel reservation system"""

class Guest:
    """Represents a guest in the reservation system"""

    def __init__(self, guest_id, full_name, phone, email):

        if not self.validate_phone(phone):
            raise ValueError("Invalid phone number")

        if not self.validate_email(email):
            raise ValueError("Invalid email")

        self.guest_id = guest_id
        self.full_name = full_name
        self.phone = phone
        self.email = email

    def validate_phone(self, phone):
        """Checks if the phone number is valid"""
        cleaned = phone.replace("+", "").replace(" ", "")
        return cleaned.isdigit() and 7 <= len(cleaned) <= 15

    def validate_email(self, email):
        """Checks if the email is valid"""
        return "@" in email and "." in email.split("@")[1]

    def update_contact(self, new_phone, new_email):
        """Updates guest phone and email"""

        if not self.validate_phone(new_phone):
            raise ValueError("Invalid phone number")

        if not self.validate_email(new_email):
            raise ValueError("Invalid email")

        self.phone = new_phone
        self.email = new_email

    def get_info(self):
        """Returns the guest info"""
        return (f"{self.guest_id} {self.full_name} "
                f"{self.phone} {self.email}")

    def to_dict(self):
        """Return the member data as a dictionary"""
        return {
            "guest_id": self.guest_id,
            "full_name": self.full_name,
            "phone": self.phone,
            "email": self.email,
        }


if __name__ == "__main__":

    g = Guest(1, "Ali Yilmaz", "+49 151 2345678", "ali@mail.com")
    print(g.get_info())

    g.update_contact("+49 170 1112233", "ali@gmail.com")
    print(g.get_info())

    try:
        Guest(2, "Ayse Demir", "abc123", "aysei@gmail.com")
    except ValueError as error:
        print("Error:", error)

    try:
        Guest(3, "Ayse Demir", "+49 170 1234567", "aysegmail.com")
    except ValueError as error:
        print("Error:", error)
