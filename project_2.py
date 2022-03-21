import numpy
import scipy
import matplotlib
import cv2

if __name__ == '__main__':
    # Load the image and show some basic information on it
    image = cv2.imread(r'A:/University/Term4/Graphic/Assignment/beach.png')

    # Show the image and wait for a keypress
    cv2.imshow("Image", image)
    cv2.imshow("image cut", image[40:180, 90:, :])
    image_switch_color = image.copy()
    image_switch_color[:, :, 2] = image_switch_color[:, :, 2] * 1.5
    cv2.imshow('image increase red intensity', image_switch_color)
    cv2.imshow('image flip', image[::-1, ::-1])
    image_gray = cv2.imread(r'A:/University/Term4/Graphic/Assignment/beach.png', cv2.IMREAD_GRAYSCALE)
    cv2.imshow('image_gray', image_gray)
    cv2.imshow('image_switch_blue_red', image[:, :, ::-1])
    cv2.waitKey(0)
    cv2.destroyAllWindows()
