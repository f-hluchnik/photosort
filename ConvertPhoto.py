import pyheif
from PIL import Image


class ConvertPhoto():
    def __init__(self) -> None:
        pass

    def convert(self, path: str) -> None:
        # pillow_heif.register_heif_opener()
        heif_file = pyheif.read("./input/img.HEIC")
        print(heif_file.metadata)
        # for metadata in heif_file.metadata.keys():
        #     print(f"{metadata:25}: {heif_file.metadata[metadata]}")

        # image = Image.frombytes(
        #     heif_file.mode, 
        #     heif_file.size, 
        #     heif_file.data,
        #     "raw",
        #     heif_file.mode,
        #     heif_file.stride,
        #     )
        # image.save("./input/output.jpg", "JPEG")
        # img = Image.open(path)
        # img.save("./input/output.jpeg")