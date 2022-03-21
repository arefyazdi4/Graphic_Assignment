import numpy
import numpy as np
import scipy
import matplotlib
import cv2

if __name__ == '__main__':
    # Load the image and show some basic information on it
    image: np.ndarray = cv2.imread(r'A:/University/Term4/Graphic/Assignment/beach.png')
    cv2.imshow("Image", image)

    # Image_high_intensity_for_loop
    image2: np.ndarray = cv2.imread(r'A:/University/Term4/Graphic/Assignment/beach.png')
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            for k in range(image.shape[2]):
                new_color_map = np.array(image2[i, j, k], dtype='uint32') + 70
                image2[i, j, k] = np.min([new_color_map, 255])
    cv2.imshow("Image_high_intensity_for_loop", image2)

    # Image_low_intensity_for_loop"
    image3: np.ndarray = cv2.imread(r'A:/University/Term4/Graphic/Assignment/beach.png')
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            for k in range(image.shape[2]):
                new_color_map = np.array(image3[i, j, k], dtype='uint32') - 70
                image3[i, j, k] = np.max([new_color_map, 0])
    cv2.imshow("Image_low_intensity_for_loop", image3)

    # adding func
    intensity_matrix = np.ones(image.shape, dtype='uint8') * 130
    image_added = cv2.add(image, intensity_matrix)
    cv2.imshow('Added', image_added)

    # subtracting func
    intensity_matrix = np.ones(image.shape, dtype='uint8') * 130
    image_subtract = cv2.subtract(image, intensity_matrix)
    cv2.imshow('Subtract', image_subtract)

    # increase red intensity
    (blue, green, red) = cv2.split(image)
    increased_red = cv2.add(red, 100)
    cv2.imshow('red_increased', cv2.merge([blue, green, increased_red]))

    # mixing to image
    image_darker: np.ndarray = np.uint8(image * 0.6)
    image_trex: np.ndarray = cv2.resize(cv2.imread(r'A:/University/Term4/Graphic/Assignment/trex.png'), (350, 233))
    cv2.imshow('terex', image_trex)
    # dropping a background white color
    image_trex_darker: np.ndarray = np.uint8(image_trex)
    for i in range(image_trex.shape[0]):
        for j in range(image_trex.shape[1]):
            sum_color = 0
            for k in range(image_trex.shape[2]):
                sum_color += image_trex[i, j, k]
            if sum_color in range(650, 770):
                image_trex_darker[i, j] = (0, 0, 0)
    cv2.imshow('image_trex_darker', image_trex_darker)

    image_mixed = cv2.add(image_darker, image_trex_darker)
    cv2.imshow('mixed image', image_mixed)
    # Show the image and wait for a keypress
    cv2.waitKey(0)
    cv2.destroyAllWindows()
