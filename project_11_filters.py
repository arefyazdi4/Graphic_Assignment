import numpy as np
import cv2
from matplotlib import pyplot as plt

if __name__ == '__main__':
    # Load the image and show some basic information on it
    image: np.ndarray = cv2.imread(r'A:/University/Term4/Graphic/Assignment/coins.png')

    image_gray: np.ndarray = cv2.imread(r'A:/University/Term4/Graphic/Assignment/coins.png', 0)  # gray read
    cv2.imshow("Image_gray", image_gray)

    # session 11
    # laplacian filter
    lap_image = cv2.Laplacian(image_gray, cv2.CV_64F)
    lap_image = np.uint8(lap_image)
    cv2.imshow('laplacian filter', lap_image)

    # sober filter horizontal
    sobel_image = cv2.Sobel(image_gray, cv2.CV_64F, 0, 1)
    sobel_image = np.uint8(sobel_image)
    cv2.imshow('sobel filter h', sobel_image)
    # sober filter vertical
    # sober filter [[-1,-2,-1],[0,0,0],[1,2,1]] it's vertical
    sobel_image = cv2.Sobel(image_gray, cv2.CV_64F, 1, 0)
    sobel_image = np.uint8(sobel_image)
    cv2.imshow('sobel filter v', sobel_image)

    # creat a custom filter
    custom_filter = np.array([[1, 1, 1], [-2, -2, -2], [1, 1, 1]])
    filtered_image = cv2.filter2D(image_gray, -1, custom_filter)
    cv2.imshow('filtered_image', filtered_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
