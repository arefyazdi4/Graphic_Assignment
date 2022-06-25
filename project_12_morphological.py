# Morphological Processing

# hit : when at least one of structure pixels cover the picture
# fit : when all the pixels of structure cover the picture
# miss : when None of pixels cover picture
# struct_sample_1 = [[1,1,1],[1,1,1],[1,1,1]]
# struct_sample_2_cross = [[0,1,0],[1,1,1],[0,1,0]]

# Erosion
# we apply a filter(structuring element) if it's fit we set the center value 1 other than that 0
# it can split joined obj
# it can strips elements
# watch out: it cause shrink obj

# Dilation
# we apply a filter if it's fit or hit we set the center value 1 and it 0 if it's miss
# can repair breaks
# it can repair intrusions
# watch out : it cause enlarge obj

# Opening
# the opening of image f by structuring elements s,
# denoted fos is simply an erosion followed by a dilation

# Closing
# a dilation followed by erosion


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

    # it's better to do Morphological Processing on gray level images
    # Dilation
    structure_element = np.ones((8, 8), dtype=np.uint8)  # kernel
    image_dilate = cv2.dilate(src=image_negative, kernel=structure_element, iterations=1)
    cv2.imshow("Image dilation", image_dilate)
    # Erosion
    structure_element = np.ones((4, 4), dtype=np.uint8)  # kernel
    image_erode = cv2.erode(src=image_negative, kernel=structure_element, iterations=2)
    cv2.imshow("Image erosion", image_erode)

    image_gray: np.ndarray = cv2.imread(r'A:/University/Term4/Graphic/Assignment/openning_sample.png')  # gray read
    cv2.imshow("Image_gray", image_gray)
    # Opening
    # an erosion followed by a dilation
    structure_element = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (25, 25))  # kernel
    image_open = cv2.morphologyEx(image_gray, cv2.MORPH_OPEN, structure_element)
    cv2.imshow("Image Opening", image_open)
    # Closing
    # a dilation followed by erosion
    structure_element = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))  # kernel
    image_close = cv2.morphologyEx(image_gray, cv2.MORPH_CLOSE, structure_element)
    cv2.imshow("Image Closing", image_close)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
