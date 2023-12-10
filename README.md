# Photosort

The Photosort is a Python script designed to organize a directory of photos based on their capture date. It reads the
EXIF metadata of each image to extract the capture date and time, and then sorts the photos accordingly. The sorted
photos are then renamed and saved in a new location.

## Usage

1. Clone the repository.
    ```commandline
    git clone https://github.com/f-hluchnik/photosort
    cd photosort
    ```
2. Install dependencies.
    ```commandline
    pip install -r requirements.txt
    ```
3. Run the script.
    ```
    python main.py -i /path/to/photos -o /path/to/sorted-photos -f MyPhotos
    ```
    - required arguments
        - `-f` or `--filename`: Filename for the sorted photos. The index will be added automatically, so the resulting
          file name will look like this: `MyPhoto_001.JPG`
    - optional arguments
        - `-i` or `--input-dir`: The directory containing the unsorted photos.
        - `-o` or `--output-dir`: Output directory for sorted photos.
     