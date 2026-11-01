import numpy as np
from PIL import Image


def ft_load(path: str) -> np.ndarray:
    """Load an image, print its shape and return its RGB pixels."""
    try:
        assert isinstance(path, str), "path must be a string"
        with Image.open(path) as image:
            pixels = np.array(image.convert("RGB"))
        print(f"The shape of image is: {pixels.shape}")
        return pixels
    except Exception as error:
        print(f"{type(error).__name__}: {error}")
        return None
