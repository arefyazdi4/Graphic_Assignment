# Morphological Processing
# py image search _ image super resolution _ deploy a project
# ocr passport if you like _ extract data from image
import numpy as np
import cv2

if __name__ == '__main__':
    # Load the image and show some basic information on it
    image: np.ndarray = cv2.imread(r'A:/University/Term4/Graphic/Assignment/coins.png')
    image_gray: np.ndarray = cv2.imread(r'A:/University/Term4/Graphic/Assignment/coins.png', 0)  # gray read

    # black and white
    max_value, image_bw = cv2.threshold(image_gray, 160, 255, cv2.THRESH_BINARY)
    # negativing the image so background became black and that make process easier
    image_negative = 255 - image_bw
    cv2.imshow("Image_negative", image_negative)

    # Closing
    # a dilation followed by erosion
    # it's better to do Morphological Processing on gray level images

    # Dilation
    structure_element = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))  # kernel
    image_dilate = cv2.dilate(src=image_negative, kernel=structure_element, iterations=1)
    cv2.imshow("Image dilation", image_dilate)
    # Erosion
    structure_element = np.ones((3, 3), dtype=np.uint8)  # kernel
    image_erode = cv2.erode(src=image_dilate, kernel=structure_element, iterations=2)
    cv2.imshow("Image erosion, Closing", image_erode)

    image_open = cv2.morphologyEx(image_negative, cv2.MORPH_OPEN, structure_element)
    cv2.imshow("Image Opening", image_open)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
