import cv2
import pytesseract

from os import getcwd
from PIL import ImageGrab
from datetime import datetime



def main():
    path = getcwd() + "\\resources\\screenshots\\"
    take_screenshot(path)


def take_screenshot(path):
    """
    Takes a screenshot and stores it with timestamp in a directory. 

    parameters:
      path: str - defines directory where the screenshot is saved
    """

    date = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    snapshot = ImageGrab.grab()
    filename = date + "_screenshot.jpg"
    snapshot.save(path + filename)


def apply_ocr():
    pass


if __name__ == "__main__":
    print("praise the sun")
    main()
