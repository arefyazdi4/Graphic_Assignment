# famous model for finding face is cascade
# first project face detection
# second project face detection with web cam
# third project eye detecting
# fourth project color_tracking recreate it to use webcam as source instead of video use orange color instead of blue
# py image search _ image super resolution _ deploy a project
# ocr passport if you like _ extract data from image
import numpy as np
import cv2
from matplotlib import pyplot as plt

if __name__ == '__main__':
    # Load the image and show some basic information on it
    image: np.ndarray = cv2.imread(r'A:/University/Term4/Graphic/Assignment/coins.png')

    image_gray: np.ndarray = cv2.imread(r'A:/University/Term4/Graphic/Assignment/coins.png', 0)  # gray read
    cv2.imshow("Image_gray", image_gray)



    cv2.waitKey(0)
    cv2.destroyAllWindows()

