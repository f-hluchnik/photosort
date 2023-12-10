import logging

import exifread
from PIL import Image


def get_image_metadata(image_path: str, print_metadata: bool = False) -> dict:
    """
    Gets image metadata.

    Args:
        image_path: path to the image
        print_metadata: set to true if you want to pretty-print the image metadata

    Returns:
        dictionary of image tags
    """

    tags = {}
    if image_path.lower().endswith(('.jpg', '.jpeg')):
        with open(image_path, 'rb') as f:
            tags = exifread.process_file(f)
            if print_metadata:
                pretty_print_metadata(tags)
    return tags


def pretty_print_metadata(tags: dict) -> None:
    """
    Pretty-prints the metadata of the picture.

    Args:
        tags: dictionary of image metadata
    """

    for tag in tags.keys():
        if tag not in ('JPEGThumbnail', 'TIFFThumbnail', 'Filename', 'EXIF MakerNote'):
            logging.info(f"{tag:25}: {tags[tag]}")


def get_image_exif_tag(image_path: str, exif_tag: int) -> str:
    """
    Retrieves the specified exif tag from the image.

    Args:
        image_path: path to the image
        exif_tag: number of the tag you want to retrieve
    """
    image = Image.open(image_path)
    exif_data = image.getexif()
    tag_value = exif_data.get(exif_tag)
    if tag_value is None:
        raise ValueError(f"Error reading image metadata, exif metadata ID {exif_tag} is None.")
    return tag_value
