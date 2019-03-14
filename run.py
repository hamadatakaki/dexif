from PIL import Image
import os.path
from config import dirname


if __name__ == "__main__":
    PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
    IMAGES_PATH = os.path.join(PROJECT_ROOT, "images", dirname)

    for IMAGE_NAME in os.listdir(IMAGES_PATH):
        with Image.open(os.path.join(IMAGES_PATH, IMAGE_NAME)) as image:
            data = image.getdata()
            mode = image.mode
            size = image.size

        with Image.new(mode, size) as dst:
            dst.putdata(data)
            dst.save(os.path.join(IMAGES_PATH, "dst_"+IMAGE_NAME))

