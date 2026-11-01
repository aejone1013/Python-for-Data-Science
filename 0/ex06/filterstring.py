import sys

from ft_filter import ft_filter


def main():
    """Print the words of S that are longer than N."""
    try:
        assert len(sys.argv) == 3, "the arguments are bad"
        assert sys.argv[2].lstrip("-").isdigit(), "the arguments are bad"
        words = [word for word in sys.argv[1].split()]
        n = int(sys.argv[2])
        print(ft_filter(lambda word: len(word) > n, words))
    except AssertionError as error:
        print(f"AssertionError: {error}")


if __name__ == "__main__":
    main()
