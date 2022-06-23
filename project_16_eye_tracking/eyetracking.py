# USAGE
# python eyetracking.py --face cascades/haarcascade_frontalface_default.xml --eye cascades/haarcascade_eye.xml --video video/adrian_eyes.mov
# python eyetracking.py --face cascades/haarcascade_frontalface_default.xml --eye cascades/haarcascade_eye.xml

# import the necessary packages
from pyimagesearch.eyetracker import EyeTracker
from pyimagesearch import imutils
import argparse
import cv2

if __name__ == '__main__':

    # construct the eye tracker
    et = EyeTracker(r'cascades/haarcascade_frontalface_default.xml',
                    r'cascades/haarcascade_eye.xml')

    camera = cv2.VideoCapture(0)

    # keep looping
    while True:
        # grab the current frame
        (grabbed, frame) = camera.read()

        # resize the frame and convert it to grayscale
        frame = imutils.resize(frame, width=300)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # detect faces and eyes in the image
        rects = et.track(gray)

        # loop over the face bounding boxes and draw them
        for rect in rects:
            cv2.rectangle(frame, (rect[0], rect[1]), (rect[2], rect[3]), (0, 255, 0), 2)

        # show the tracked eyes and face
        cv2.imshow("Tracking", frame)

        # if the 'q' key is pressed, stop the loop
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    # cleanup the camera and close any open windows
    camera.release()
    cv2.destroyAllWindows()
