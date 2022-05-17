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
    # cv2.imshow("Image_gray", image_gray)
    blur_d = 7
    # convolutional filter , each pixel applies wight and get sum for and set for middle pixel
    # image_partial = [200:150, 150:200, :]
    # smooth or blur [[1/9,1/9,1/9],[1/9,1/9,1/9],[1/9,1/9,1/9],]
    image_blur = image.copy()
    image_blur[200:150, 150:200, :] = cv2.blur(image[200:150, 150:200, :], [blur_d, blur_d])
    cv2.imshow("blur image", image_blur)
    # gaussian filter it will help us to improve
    # [[.1,.3.,.1],[.3,.8,.3],[.1,.3,.1]]
    filter_gaussian = cv2.GaussianBlur(image, (blur_d, blur_d), 0)
    cv2.imshow("filter gaussian", filter_gaussian)
    # edge finder filter canny matrix -> [[1,1,1],[-2,-2,-2],[1,1,1]] it's only work for vertical edges
    # place where color change is massive _ [[0,-1,0],[-1,-4,-1],[0,-1,0]] v & h
    filter_canny = cv2.Canny(image_gray, 30, 150)
    cv2.imshow("canny filter", filter_canny)
    # sober filter [[-1,-2,-1],[0,0,0],[1,2,1]] it's vertical

    cv2.waitKey(0)
    cv2.destroyAllWindows()
