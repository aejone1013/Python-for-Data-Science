from typing import Any


def ft_mean(data: list) -> float:
    """Return the mean of data."""
    return sum(data) / len(data)


def ft_median(data: list) -> float:
    """Return the median of data."""
    s = sorted(data)
    n = len(s)
    mid = n // 2
    if n % 2 == 1:
        return s[mid]
    return (s[mid - 1] + s[mid]) / 2


def ft_quartile(data: list) -> list:
    """Return [Q1, Q3] of data."""
    s = sorted(data)
    n = len(s)
    return [float(s[n // 4]), float(s[(3 * n) // 4])]


def ft_var(data: list) -> float:
    """Return the variance of data."""
    m = ft_mean(data)
    return sum((x - m) ** 2 for x in data) / len(data)


def ft_std(data: list) -> float:
    """Return the standard deviation of data."""
    return ft_var(data) ** 0.5


def ft_statistics(*args: Any, **kwargs: Any) -> None:
    """Print each statistic asked in kwargs, computed on args."""
    operations = {
        "mean": ft_mean,
        "median": ft_median,
        "quartile": ft_quartile,
        "std": ft_std,
        "var": ft_var,
    }
    data = list(args)
    if any(not isinstance(x, (int, float)) or isinstance(x, bool)
           for x in data):
        print("TypeError: all arguments must be numbers")
        return
    for request in kwargs.values():
        if request not in operations:
            continue
        if not data:
            print("ERROR")
            continue
        print(f"{request} : {operations[request](data)}")
