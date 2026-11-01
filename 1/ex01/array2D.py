import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """Print the shape of family, then return family[start:end]."""
    try:
        assert isinstance(family, list), "family must be a list"
        assert all(isinstance(row, list) for row in family), (
            "family must be a list of lists")
        assert len(set(len(row) for row in family)) <= 1, (
            "all rows must have the same size")
        assert type(start) is int and type(end) is int, (
            "start and end must be integers")
        array = np.array(family)
        print(f"My shape is : {array.shape}")
        new = array[start:end]
        print(f"My new shape is : {new.shape}")
        return new.tolist()
    except AssertionError as error:
        print(f"AssertionError: {error}")
        return []
