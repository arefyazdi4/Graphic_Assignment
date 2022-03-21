import numpy
import scipy
import matplotlib
import cv2
import argparse


if __name__ == '__main__':

    # Construct the argument parser and parse the arguments
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", required=True, help="Path to the image")
    args = vars(ap.parse_args())

    # Load the image and show some basic information on it
    image = cv2.imread(args["image"])
    print("width: {} pixels".format(image.shape[1]))
    print("height: {} pixels".format(image.shape[0]))
    print("channels: {}".format(image.shape[2]))

    # Show the image and wait for a keypress
    cv2.imshow("Image", image)
    cv2.waitKey(0)
    # python project_1.py --image trex.png