import logging
import os
import shutil
from datetime import datetime
from pathlib import Path
from typing import List, Dict

from utils.utils import get_image_exif_tag

DATETIME_EXIF_TAG_ID = 306


class SortPhotos:

    def __init__(self, filename_base: str, input_dir: str = "./input/", output_dir: str = "./sorted_photos/") -> None:
        self.logger = logging.getLogger()
        self.input_dir = input_dir
        self.filename_base = filename_base
        self.output_dir = output_dir

    def sort_images_by_datetime(self):
        self.create_output_directory()

        photo_filenames = [f for f in os.listdir(self.input_dir)]
        date_time_mapping = self.map_filenames_to_datetimes(photo_filenames)

        self.logger.info("Sorting photos...")
        sorted_photos = sorted(photo_filenames, key=lambda x: date_time_mapping[x])
        self.logger.info("Photos sorted.")

        self.logger.info("Saving photos to new location...")
        self.rename_and_save(sorted_photos)
        self.logger.info(f"Photos saved in {self.output_dir}.")

    def create_output_directory(self):
        """
        Creates output directory if it does not exist.
        """
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

    def map_filenames_to_datetimes(self, photo_files: List[str]) -> Dict[str, datetime]:
        """
        Creates mapping between filenames and their datetime exif tags values.
        Args:
            photo_files: list of filenames

        Returns:
            dictionary with the filename-datetime mapping
        """
        date_time_mapping = {}
        for filename in photo_files:
            image_path = str(Path(self.input_dir) / filename)
            image_datetime = get_image_exif_tag(image_path, DATETIME_EXIF_TAG_ID)
            date_format = "%Y:%m:%d %H:%M:%S"
            date_time = datetime.strptime(image_datetime, date_format)
            date_time_mapping[filename] = date_time
        return date_time_mapping

    def rename_and_save(self, sorted_photos: List[str]) -> None:
        """
        Rename the photos and save them to the output directory.
        Args:
            sorted_photos: list of filenames
        """
        rename_pattern = f"{self.filename_base}" + "_{:03d}"
        for index, photo in enumerate(sorted_photos):
            _, file_extension = os.path.splitext(photo)
            new_name = rename_pattern.format(index + 1)
            old_path = Path(self.input_dir) / photo
            new_path = Path(self.output_dir) / (new_name + file_extension)
            shutil.copy2(old_path, new_path)
