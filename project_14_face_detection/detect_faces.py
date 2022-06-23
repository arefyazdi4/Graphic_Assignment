# USAGE
# python detect_faces.py --face cascades/haarcascade_frontalface_default.xml --image images/obama.png

# import the necessary packages
from __future__ import print_function
from pyimagesearch.facedetector import FaceDetector
import argparse
import cv2

if __name__ == '__main__':

    # load the image and convert it to grayscale
    image = cv2.imread(r'images/obama2.png')
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # find faces in the image
    fd = FaceDetector(r'cascades/haarcascade_frontalface_default.xml')
    faceRects = fd.detect(gray, scaleFactor=1.1, minNeighbors=5,
                          minSize=(30, 30))
    print("I found {} face(s)".format(len(faceRects)))

    # loop over the faces and draw a rectangle around each
    for (x, y, w, h) in faceRects:
        cv2.rectangle(img=image, pt1=(x, y), pt2=(x + w, y + h), color=(0, 255, 0), thickness=2)

    # show the detected faces
    cv2.imshow("Faces", image)
    cv2.waitKey(0)
