import numpy
import numpy as np
import scipy
import matplotlib
import cv2

if __name__ == '__main__':
    # Load the image and show some basic information on it
    image: np.ndarray = cv2.imread(r'A:/University/Term4/Graphic/Assignment/trex.png')
    cv2.imshow("Image", image)

    # resize an image with width
    width_size = 200
    height = image.shape[0]
    resize_ratio = width_size / image.shape[1]
    new_size = (width_size, int(resize_ratio * height))
    image_resize_width = cv2.resize(src=image, dsize=new_size, interpolation=cv2.INTER_AREA)
    cv2.imshow('image_resize_width', image_resize_width)

    # resize an image with height
    width_size = image.shape[1]
    height = 200
    resize_ratio = height / image.shape[0]
    new_size = (int(resize_ratio * width_size), height)
    image_resize_height = cv2.resize(src=image, dsize=new_size, interpolation=cv2.INTER_AREA)
    cv2.imshow('image_resize_height', image_resize_height)

    # flip an image with cv2 flip
    image_flip_h = cv2.flip(image, 1)  # 1 -> horizontal , 0 -> vertically , -1 -> rotate 180
    # cv2.imshow('image_flip_h_cv2', image_flip_h)

    # flip an image with np flip
    image_flip_v = np.flipud(image)
    # cv2.imshow('image_flip_v_np', image_flip_v)

    # flip an image with index iterate
    image_flip_180 = image[::-1, ::-1]
    # cv2.imshow('image_flip_180_index', image_flip_180)

    # contact all the flipped images
    stick_flipped_image_1 = cv2.vconcat([image, image_flip_v])
    stick_flipped_image_2 = cv2.vconcat([image_flip_h, image_flip_180])
    stick_flipped_image = cv2.hconcat([stick_flipped_image_1, stick_flipped_image_2])
    cv2.imshow('contact_flipped', stick_flipped_image)

    # Show the image and wait for a keypress
    cv2.waitKey(0)
    cv2.destroyAllWindows()
