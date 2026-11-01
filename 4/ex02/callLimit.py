from typing import Any


def callLimit(limit: int):
    """Let the decorated function be called at most limit times."""
    count = 0

    def callLimiter(function):
        """Wrap function with the call counter."""

        def limit_function(*args: Any, **kwds: Any):
            """Call function, or print an error once limit is reached."""
            nonlocal count
            if count < limit:
                count += 1
                return function(*args, **kwds)
            print(f"Error: {function} call too many times")
        return limit_function
    return callLimiter
