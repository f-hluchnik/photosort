import argparse
import logging

from SortPhotos import SortPhotos

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

DEFAULT_INPUT_DIRECTORY = './input/'
DEFAULT_OUTPUT_DIRECTORY = './sorted_photos/'


class Config:
    def __init__(self, input_dir: str, output_dir: str, filename: str):
        self.input_dir = input_dir
        self.output_dir = output_dir
        self.filename = filename


def parse_arguments() -> Config:
    parser = argparse.ArgumentParser(description='Sort photos by datetime and rename them.')
    parser.add_argument('-i', '--input-dir', dest='input_dir', type=str, default=DEFAULT_INPUT_DIRECTORY,
                        help='The directory containing the unsorted photos.')
    parser.add_argument('-o', '--output-dir', dest='output_dir', type=str, default=DEFAULT_OUTPUT_DIRECTORY,
                        help='Output directory for sorted photos.')
    parser.add_argument('-f', '--filename', type=str, required=True,
                        help='Filename for the sorted photos.')

    args = parser.parse_args()
    return Config(args.input_dir, args.output_dir, args.filename)


def main():
    config = parse_arguments()
    sp = SortPhotos(filename_base=config.filename, input_dir=config.input_dir, output_dir=config.output_dir)
    try:
        sp.sort_images_by_datetime()
    except Exception as error:
        logging.error(error)


if __name__ == '__main__':
    main()
