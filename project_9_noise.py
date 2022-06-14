import numpy
import numpy as np
import scipy
import cv2
from matplotlib import pyplot as plt
from skimage.util import random_noise


if __name__ == '__main__':
    # Load the image and show some basic information on it
    image: np.ndarray = cv2.imread(r'A:/University/Term4/Graphic/Assignment/coins.png')

    image_gray: np.ndarray = cv2.imread(r'A:/University/Term4/Graphic/Assignment/coins.png', 0)  # gray read
    cv2.imshow("Image_gray", image_gray)

    # it's like s&p but increase or decrease random value and random pixels by variance of 0
    image_noise_gaussian: np.ndarray = random_noise(image=image_gray, mode='gaussian')  # result num is array range 0 to 1.
    image_noise_gaussian: np.ndarray = np.array(image_noise_gaussian * 255, dtype='uint8')
    cv2.imshow("Image_gaussian", image_noise_gaussian)

    # salt and paper filter randomly put turns some pixels to 0 or 256
    image_noise_sp: np.ndarray = random_noise(image=image_gray, mode='s&p')  # result num is array range 0 to 1.
    image_noise_sp: np.ndarray = np.array(image_noise_sp * 255, dtype='uint8')
    cv2.imshow("Image_sp", image_noise_sp)

    # this is best for gaussian
    # 1/9 value filter applies on each pixel
    # src, dsd = destination, h= filter power, search window, block size = number pixel
    image_de_noise = cv2.fastNlMeansDenoising(image_noise_gaussian, None, 20, 20, 25)
    cv2.imshow("Image_gau_deNoise", image_de_noise)

    # this is best for salt and paper
    # it will sort adj pixels around (expect it self) and select mid on
    # conclusion
    image_de_noise = cv2.medianBlur(image_noise_sp, 7, None)
    cv2.imshow("Image_s&p_deNoise", image_de_noise)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
