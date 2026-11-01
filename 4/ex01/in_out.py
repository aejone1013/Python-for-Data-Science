def square(x: int | float) -> int | float:
    """Return x * x."""
    return x * x


def pow(x: int | float) -> int | float:
    """Return x ** x."""
    return x ** x


def outer(x: int | float, function) -> object:
    """Return a function that applies function to its last result."""
    value = x

    def inner() -> float:
        """Apply function to the stored value and return it."""
        nonlocal value
        value = function(value)
        return value
    return inner
