import numpy as np
import matplotlib.pyplot as plt
from load_image import ft_load


def cut_square(image: np.ndarray) -> np.ndarray:
    """Cut a 400x400 square out of image and turn it grey (1 channel)."""
    square = image[100:500, 450:850]
    return np.mean(square, axis=2, keepdims=True).astype(np.uint8)


def ft_transpose(matrix) -> list:
    """Transpose a 2D matrix by hand."""
    rows = len(matrix)
    cols = len(matrix[0]) if rows else 0
    return [[matrix[r][c] for r in range(rows)] for c in range(cols)]


def main():
    """Load animal.jpeg, cut a square, transpose it and show it."""
    try:
        image = ft_load("animal.jpeg")
        if image is None:
            return
        square = cut_square(image)
        print(f"The shape of image is: {square.shape} "
              f"or {square.shape[:2]}")
        print(square)
        transposed = np.array(ft_transpose(square[:, :, 0]))
        print(f"New shape after Transpose: {transposed.shape}")
        print(transposed)
        plt.imshow(transposed, cmap="gray")
        plt.show()
    except Exception as error:
        print(f"{type(error).__name__}: {error}")
    except KeyboardInterrupt:
        print()


if __name__ == "__main__":
    main()
