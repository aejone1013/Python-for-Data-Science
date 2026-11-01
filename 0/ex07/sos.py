import sys

NESTED_MORSE = {
    " ": "/ ", "A": ".- ", "B": "-... ", "C": "-.-. ", "D": "-.. ",
    "E": ". ", "F": "..-. ", "G": "--. ", "H": ".... ", "I": ".. ",
    "J": ".--- ", "K": "-.- ", "L": ".-.. ", "M": "-- ", "N": "-. ",
    "O": "--- ", "P": ".--. ", "Q": "--.- ", "R": ".-. ", "S": "... ",
    "T": "- ", "U": "..- ", "V": "...- ", "W": ".-- ", "X": "-..- ",
    "Y": "-.-- ", "Z": "--.. ", "0": "----- ", "1": ".---- ",
    "2": "..--- ", "3": "...-- ", "4": "....- ", "5": "..... ",
    "6": "-.... ", "7": "--... ", "8": "---.. ", "9": "----. ",
}


def main():
    """Encode the single string argument into Morse code."""
    try:
        assert len(sys.argv) == 2, "the arguments are bad"
        try:
            morse = "".join(NESTED_MORSE[c] for c in sys.argv[1].upper())
        except KeyError:
            raise AssertionError("the arguments are bad")
        print(morse.rstrip())
    except AssertionError as error:
        print(f"AssertionError: {error}")


if __name__ == "__main__":
    main()
