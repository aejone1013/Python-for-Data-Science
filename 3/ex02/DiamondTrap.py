from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """Representing a king who is both Baratheon and Lannister."""

    def __init__(self, first_name: str, is_alive: bool = True):
        """Create a King (Baratheon first because of the MRO)."""
        super().__init__(first_name, is_alive)

    def get_eyes(self):
        """Return the eye color."""
        return self.__dict__["eyes"]

    def set_eyes(self, eyes: str):
        """Set the eye color."""
        self.__dict__["eyes"] = eyes

    def get_hairs(self):
        """Return the hair color."""
        return self.__dict__["hairs"]

    def set_hairs(self, hairs: str):
        """Set the hair color."""
        self.__dict__["hairs"] = hairs

    eyes = property(get_eyes, set_eyes)
    hairs = property(get_hairs, set_hairs)
