import pandas as pd


def load(path: str) -> pd.DataFrame:
    """Load a CSV file, print its dimensions and return it (None on error)."""
    try:
        assert isinstance(path, str), "path must be a string"
        assert path.lower().endswith(".csv"), "file must be a .csv"
        data = pd.read_csv(path)
        print(f"Loading dataset of dimensions {data.shape}")
        return data
    except Exception as error:
        print(f"{type(error).__name__}: {error}")
        return None
