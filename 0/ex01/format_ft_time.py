import time
from datetime import datetime


def main():
    """Print seconds since epoch (two formats) and today's date."""
    now = time.time()
    print(f"Seconds since January 1, 1970: {now:,.4f} "
          f"or {now:.2e} in scientific notation")
    print(datetime.now().strftime("%b %d %Y"))


if __name__ == "__main__":
    main()
