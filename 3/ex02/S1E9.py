from abc import ABC, abstractmethod


class Character(ABC):
    """Abstract class for every character."""

    @abstractmethod
    def __init__(self, first_name: str, is_alive: bool = True):
        """Set the first name and whether the character is alive."""
        self.first_name = first_name
        self.is_alive = is_alive

    def die(self):
        """Set is_alive to False."""
        self.is_alive = False


class Stark(Character):
    """Representing the Stark family."""

    def __init__(self, first_name: str, is_alive: bool = True):
        """Create a Stark."""
        super().__init__(first_name, is_alive)
