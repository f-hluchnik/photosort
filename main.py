from ConvertPhoto import ConvertPhoto
from SortPhotos import SortPhotos

if __name__=='__main__':
    # cp = ConvertPhoto()
    # cp.convert("./input/img.HEIC")
    sp = SortPhotos("./input_first/")
    sp.sort_images_by_datetime()