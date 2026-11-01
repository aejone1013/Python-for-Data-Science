class calculator:
    """Vector and scalar operations, done in place."""

    def __init__(self, vector: list):
        """Store the vector as floats."""
        self.vector = [float(x) for x in vector]

    def __add__(self, object) -> None:
        """Add object to each element and print the vector."""
        self.vector = [x + object for x in self.vector]
        print(self.vector)

    def __mul__(self, object) -> None:
        """Multiply each element by object and print the vector."""
        self.vector = [x * object for x in self.vector]
        print(self.vector)

    def __sub__(self, object) -> None:
        """Subtract object from each element and print the vector."""
        self.vector = [x - object for x in self.vector]
        print(self.vector)

    def __truediv__(self, object) -> None:
        """Divide each element by object and print the vector."""
        if object == 0:
            print("Error: division by zero")
            return
        self.vector = [x / object for x in self.vector]
        print(self.vector)
