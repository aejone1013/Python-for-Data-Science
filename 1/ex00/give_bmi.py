import numpy as np


def is_number(value) -> bool:
    """Return True if value is an int or a float (not a bool)."""
    return type(value) in (int, float)


def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    """Return the BMI for each (height, weight) pair."""
    try:
        assert isinstance(height, list) and isinstance(weight, list), (
            "height and weight must be lists")
        assert len(height) == len(weight), (
            "height and weight must have the same size")
        assert all(is_number(v) for v in height + weight), (
            "values must be int or float")
        assert all(h > 0 for h in height), "height must be positive"
        h = np.array(height)
        w = np.array(weight)
        return (w / h ** 2).tolist()
    except AssertionError as error:
        print(f"AssertionError: {error}")
        return []


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """Return True for each bmi above limit, False otherwise."""
    try:
        assert isinstance(bmi, list), "bmi must be a list"
        assert all(is_number(v) for v in bmi), "values must be int or float"
        assert is_number(limit), "limit must be int or float"
        return (np.array(bmi) > limit).tolist()
    except AssertionError as error:
        print(f"AssertionError: {error}")
        return []
