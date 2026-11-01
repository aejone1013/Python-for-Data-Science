import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    """Return a random id of 15 lowercase letters."""
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    """A student with a login and a random id."""
    name: str
    surname: str
    active: bool = True
    login: str = field(init=False)
    id: str = field(init=False, default_factory=generate_id)

    def __post_init__(self):
        """Build the login from the first letter of name and surname."""
        self.login = self.name[0].upper() + self.surname
