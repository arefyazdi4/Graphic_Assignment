import numpy
import numpy as np
import scipy
import cv2
from matplotlib import pyplot as plt
from skimage.util import random_noise


if __name__ == '__main__':
    # Load the image and show some basic information on it
    image: np.ndarray = cv2.imread(r'A:/University/Term4/Graphic/Assignment/trex.png')

    image_gray: np.ndarray = cv2.imread(r'A:/University/Term4/Graphic/Assignment/trex.png', 0)  # gray read
    cv2.imshow("Image_gray", image_gray)

    image_noise_gaussian: np.ndarray = random_noise(image=image_gray, mode='gaussian')  # result num is array range 0 to 1.
    image_noise: np.ndarray = random_noise(image=image_gray, mode='s&p')  # result num is array range 0 to 1.
    cv2.imshow("Image_gaussian", image_noise_gaussian)
    # it's like s&p but increase or decrease random value and random pixels

    image_noise: np.ndarray = np.array(image_noise*255, dtype='uint8')
    # it increase or decrease one pixel with avg 0_1
    #
    cv2.imshow("Image_noise", image_noise)

    image_filter = cv2.fastNlMeansDenoising(image_noise, None, 20, 20, 25)  # src, dsd = distnation, h= filter power, serach window, blocksize = number pixel
    # this is best for gaussian
    # 1/9 value filter applies on each pixel
    cv2.imshow("Image_filter", image_filter)
    image_filter = cv2.medianBlur(image_noise, 7, None)
    # this is best for salt and paper
    # it will sort adj pixels around (expect it self) and select mid on
    # conclusion

    cv2.waitKey(0)
    cv2.destroyAllWindows()
