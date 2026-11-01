import numpy as np
import matplotlib.pyplot as plt
from load_image import ft_load


def zoom(image: np.ndarray) -> np.ndarray:
    """Cut a 400x400 square out of image and turn it grey (1 channel)."""
    square = image[100:500, 450:850]
    return np.mean(square, axis=2, keepdims=True).astype(np.uint8)


def main():
    """Load animal.jpeg, zoom on it and show the result."""
    try:
        image = ft_load("animal.jpeg")
        if image is None:
            return
        print(image)
        zoomed = zoom(image)
        print(f"New shape after slicing: {zoomed.shape} "
              f"or {zoomed.shape[:2]}")
        print(zoomed)
        plt.imshow(zoomed[:, :, 0], cmap="gray")
        plt.show()
    except Exception as error:
        print(f"{type(error).__name__}: {error}")
    except KeyboardInterrupt:
        print()


if __name__ == "__main__":
    main()
