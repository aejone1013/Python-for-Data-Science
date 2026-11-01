import numpy as np
import matplotlib.pyplot as plt


def show(array: np.ndarray, title: str) -> None:
    """Display array with a title."""
    plt.imshow(array)
    plt.title(title)
    plt.show()


def is_rgb(array) -> bool:
    """Return True if array looks like an RGB image (H, W, 3)."""
    if (isinstance(array, np.ndarray) and array.ndim == 3
            and array.shape[2] == 3):
        return True
    print("Error: expected an RGB image of shape (H, W, 3)")
    return False


def ft_invert(array) -> np.ndarray:
    """Inverts the color of the image received."""
    if not is_rgb(array):
        return None
    result = 255 - array
    show(result, "Invert")
    return result


def ft_red(array) -> np.ndarray:
    """Keeps only the red channel of the image received."""
    if not is_rgb(array):
        return None
    result = array * np.array([1, 0, 0], dtype=np.uint8)
    show(result, "Red")
    return result


def ft_green(array) -> np.ndarray:
    """Keeps only the green channel of the image received."""
    if not is_rgb(array):
        return None
    result = array.copy()
    result[:, :, 0] = result[:, :, 0] - result[:, :, 0]
    result[:, :, 2] = result[:, :, 2] - result[:, :, 2]
    show(result, "Green")
    return result


def ft_blue(array) -> np.ndarray:
    """Keeps only the blue channel of the image received."""
    if not is_rgb(array):
        return None
    result = array.copy()
    result[:, :, 0] = 0
    result[:, :, 1] = 0
    show(result, "Blue")
    return result


def ft_grey(array) -> np.ndarray:
    """Converts the image received to shades of grey."""
    if not is_rgb(array):
        return None
    result = array.copy()
    result[:, :, :] = np.sum(array, axis=2, keepdims=True) / 3
    show(result, "Grey")
    return result
