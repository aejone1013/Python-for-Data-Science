from S1E9 import Character


class Baratheon(Character):
    """Representing the Baratheon family."""

    def __init__(self, first_name: str, is_alive: bool = True):
        """Create a Baratheon: brown eyes, dark hair."""
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def __str__(self):
        """Return the family, eyes and hairs as a vector."""
        return (f"Vector: ('{self.family_name}', '{self.eyes}', "
                f"'{self.hairs}')")

    def __repr__(self):
        """Same as __str__."""
        return self.__str__()


class Lannister(Character):
    """Representing the Lannister family."""

    def __init__(self, first_name: str, is_alive: bool = True):
        """Create a Lannister: blue eyes, light hair."""
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def __str__(self):
        """Return the family, eyes and hairs as a vector."""
        return (f"Vector: ('{self.family_name}', '{self.eyes}', "
                f"'{self.hairs}')")

    def __repr__(self):
        """Same as __str__."""
        return self.__str__()

    @classmethod
    def create_lannister(cls, first_name: str, is_alive: bool = True):
        """Create a Lannister from the class itself."""
        return cls(first_name, is_alive)
