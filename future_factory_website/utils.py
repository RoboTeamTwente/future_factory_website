from io import BytesIO
from PIL import Image
from django.core.files import File


def compress(image, quality=60):
    """
    Compresses a given image and returns it.

    :param image   The image to be compressed
    :param quality The quality of the resulting image
    """
    try:
        img = Image.open(image)
    except FileNotFoundError:
        return image
    img_io = BytesIO()
    if '.png' not in image.name.lower():
        img.save(img_io, format='JPEG', quality=quality)
    else:
        img.save(img_io, format='PNG', quality=quality)
    new_img = File(img_io, name=image.name)
    return new_img
