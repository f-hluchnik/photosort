import os
import shutil
from datetime import datetime

import exifread
from PIL import Image
from PIL.ExifTags import TAGS
from pillow_heif import register_heif_opener

register_heif_opener()
DATETIME_EXIF_TAG_ID = 306

class SortPhotos():

    def __init__(self, directory: str) -> None:
        self.images_directory = directory

    def get_image_metadata(self, image_path: str) -> dict:
        tags = {}
        if image_path.lower().endswith(('.jpg', '.jpeg')):
            with open(image_path, 'rb') as f:
                tags = exifread.process_file(f)
        return tags

        ## Optional code for pretty-printing the dictionary
        # for tag in tags.keys():
        #     if tag not in ('JPEGThumbnail', 'TIFFThumbnail', 'Filename', 'EXIF MakerNote'):
        #         print(f"{tag:25}: {tags[tag]}")

    def get_image_datetime(self, image_path: str) -> str:
        image = Image.open(image_path)
        exifdata = image.getexif()
        datetime = exifdata.get(DATETIME_EXIF_TAG_ID)
        if datetime is None:
            raise Exception(f"Error while reading image metadata, exif metadata ID {DATETIME_EXIF_TAG_ID} is {datetime}.")
        return datetime
    
    def sort_images_by_datetime(self, output_dir="./sorted_photos/"):
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        photo_files = [f for f in os.listdir(self.images_directory)]

        date_time_mapping = {}
        for filename in photo_files:
            image_path = os.path.join(self.images_directory, filename)
            try:
                image_datetime = self.get_image_datetime(image_path)
            except Exception as error:
                print(error)

            date_format = "%Y:%m:%d %H:%M:%S"
            try:
                date_time = datetime.strptime(image_datetime, date_format)
            except ValueError as error:
                print(error)

            date_time_mapping[filename] = date_time

        sorted_photos = sorted(photo_files, key=lambda x: date_time_mapping[x])
        print(sorted_photos)

        rename_pattern = "chata_v_prirode_{:03d}"

        for index, photo in enumerate(sorted_photos):
            _, file_extension = os.path.splitext(photo)
            new_name = rename_pattern.format(index+1)
            old_path = os.path.join(os.path.dirname(self.images_directory), photo)
            new_path = os.path.join(os.path.dirname(output_dir), new_name + file_extension)
            shutil.copy(old_path, new_path)