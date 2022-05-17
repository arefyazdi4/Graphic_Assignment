import numpy
import numpy as np
import scipy
import cv2
from matplotlib import pyplot as plt

if __name__ == '__main__':
    # Load the image and show some basic information on it
    image: np.ndarray = cv2.imread(r'A:/University/Term4/Graphic/Assignment/trex.png')

    image_gray: np.ndarray = cv2.imread(r'A:/University/Term4/Graphic/Assignment/trex.png', 0)  # gray read
    cv2.imshow("Image_gray", image_gray)

    # threshold  manual
    image_threshold_manual = image_gray.copy()
    for i in range(image_gray.shape[0]):
        for j in range(image_gray.shape[1]):
            if image_gray[i, j] <= 100:
                image_threshold_manual[i, j] = 40

    cv2.imshow('threshold_manual', image_threshold_manual)

    # threshold auto
    max_value, image_threshold_auto = cv2.threshold(image_gray, 100, 255, cv2.THRESH_BINARY)
    cv2.imshow('threshold_auto', image_threshold_auto)

    # finding optimal threshold by histogram
    max_value, image_threshold_auto = cv2.threshold(image_gray, 100, 255, cv2.THRESH_OTSU)
    print(max_value)  # it take avg from histogram





    cv2.waitKey(0)
    cv2.destroyAllWindows()
