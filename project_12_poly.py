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
from matplotlib import pyplot as plt

if __name__ == '__main__':
    # Load the image and show some basic information on it
    image: np.ndarray = cv2.imread(r'A:/University/Term4/Graphic/Assignment/coins.png')

    image_gray: np.ndarray = cv2.imread(r'A:/University/Term4/Graphic/Assignment/coins.png', 0)  # gray read
    cv2.imshow("Image_gray", image_gray)
    # black and white
    max_value, image_bw = cv2.threshold(image_gray, 100, 255, cv2.THRESH_BINARY)
    cv2.imshow('black_white', image_bw)








    cv2.waitKey(0)
    cv2.destroyAllWindows()

