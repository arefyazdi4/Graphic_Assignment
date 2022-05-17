import numpy
import numpy as np
import scipy
import cv2
from matplotlib import pyplot as plt

if __name__ == '__main__':
    # Load the image and show some basic information on it
    image: np.ndarray = cv2.imread(r'A:/University/Term4/Graphic/Assignment/trex.png')
    cv2.imshow("Image_origin", image)
    #  Histogram
    image_gray: np.ndarray = cv2.imread(r'A:/University/Term4/Graphic/Assignment/trex.png', 0)  # gray read
    image_gray_add = cv2.add(image_gray, 50)
    cv2.imshow("Image_gray_add", image_gray_add)
    image_gray_sub = cv2.subtract(image_gray, 70)
    cv2.imshow("Image_gray_sub", image_gray_sub)

    plt.figure('gray')  # showing extra window plot
    plt.title("Gray Histogram")
    plt.xlabel("Bins")
    plt.ylabel("Pixels")

    histogram_add = cv2.calcHist(images=[image_gray_add], channels=[0], mask=None, histSize=[256], ranges=[0, 256])
    # print(histogram)
    plt.plot(histogram_add, color='r')
    plt.xlim(0, 256)

    histogram_sub = cv2.calcHist(images=[image_gray_sub], channels=[0], mask=None, histSize=[256], ranges=[0, 256])
    plt.plot(histogram_sub, color='b')
    plt.xlim(0, 256)
    plt.show()

    plt.figure('color')  # showing extra window plot
    plt.title("Color Histogram")
    plt.xlabel("Bins")
    plt.ylabel("Pixels")
    color_map = {0: 'b', 1: 'g', 2: 'r'}
    for color_index in color_map.keys():
        histogram = cv2.calcHist(images=[image], channels=[color_index], mask=None, histSize=[256], ranges=[0, 256])
        plt.plot(histogram, color=color_map[color_index])
        plt.xlim(0, 256)
    plt.show()

    cv2.waitKey(0)
    cv2.destroyAllWindows()
