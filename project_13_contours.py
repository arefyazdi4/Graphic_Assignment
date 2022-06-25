import numpy as np
import cv2
from matplotlib import pyplot as plt

# py image search _ image super resolution _ deploy a project
# ocr passport if you like _ extract data from image

if __name__ == '__main__':
    # Load the image and show some basic information on it
    image: np.ndarray = cv2.imread(r'A:/University/Term4/Graphic/Assignment/coins.png')
    image_gray: np.ndarray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # gray read
    # convert it to grayscale, and blur it slightly
    image_blurred = cv2.GaussianBlur(image_gray, (11, 11), 0)
    cv2.imshow("Image_gray", image_blurred)
    # The first thing we are going to do is apply edge detection to
    # the image to reveal the outlines of the coins
    image_edged = cv2.Canny(image_blurred, 30, 150)
    cv2.imshow("Edges", image_edged)
    # Find contours in the edged image.
    # NOTE: The cv2.findContours method is DESTRUCTIVE to the image
    # you pass in. If you intend on reusing your edged image, be
    # sure to copy it before calling cv2.findContours
    (cnts, _) = cv2.findContours(image_edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # How many contours did we find?
    print("I count {} coins in this image".format(len(cnts)))

    # Let's highlight the coins in the original image by drawing a
    # green circle around them
    coins = image.copy()
    cv2.drawContours(coins, cnts, -1, (0, 255, 0), 2)
    cv2.imshow("Coins", coins)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

