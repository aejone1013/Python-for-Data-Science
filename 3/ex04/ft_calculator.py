class calculator:
    """Operations between two vectors of the same size."""

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """Print the dot product of V1 and V2."""
        result = sum(a * b for a, b in zip(V1, V2))
        print(f"Dot product is: {result}")

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """Print V1 + V2."""
        result = [float(a + b) for a, b in zip(V1, V2)]
        print(f"Add Vector is : {result}")

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """Print V1 - V2."""
        result = [float(a - b) for a, b in zip(V1, V2)]
        print(f"Sous Vector is: {result}")
