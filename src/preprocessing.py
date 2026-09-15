import cv2
from pathlib import Path


def load_image(image_path):
    """
    Load an image from the given file path.

    Args:
        image_path (str): Path to the input image.

    Returns:
        image: Loaded OpenCV image.

    Raises:
        FileNotFoundError: If the image does not exist.
        ValueError: If OpenCV cannot read the image.
    """
    image_path = Path(image_path)

    if not image_path.exists():
        raise FileNotFoundError(f"Image not found: {image_path}")

    image = cv2.imread(str(image_path))

    if image is None:
        raise ValueError(f"Unable to read image: {image_path}")

    return image


def resize_image(image, width=640):
    """
    Resize an image while maintaining its aspect ratio.

    Args:
        image: OpenCV image.
        width (int): Desired image width.

    Returns:
        Resized OpenCV image.
    """
    height, original_width = image.shape[:2]

    if original_width == width:
        return image

    scale = width / original_width
    new_height = int(height * scale)

    resized = cv2.resize(
        image,
        (width, new_height),
        interpolation=cv2.INTER_AREA
    )

    return resized


def preprocess_image(image_path, output_path):
    """
    Load, resize and save an image.

    Args:
        image_path (str): Input image path.
        output_path (str): Output image path.

    Returns:
        str: Path of the processed image.
    """
    image = load_image(image_path)
    processed_image = resize_image(image)

    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    cv2.imwrite(str(output_path), processed_image)

    return str(output_path)