# USAGE
# python webcam_face_detect.py --face cascades/haarcascade_frontalface_default.xml
# python webcam_face_detect.py --face cascades/haarcascade_frontalface_default.xml --video video/adrian_face.mov

# import the necessary packages
from pyimagesearch.facedetector import FaceDetector
from pyimagesearch import imutils
import argparse
import cv2

if __name__ == '__main__':
    # construct the face detector
    fd = FaceDetector(r'cascades/haarcascade_frontalface_default.xml')
    camera = cv2.VideoCapture(0)
    # keep looping
    while True:
        # grab the current frame
        (grabbed, frame) = camera.read()
        # resize the frame and convert it to grayscale
        frame = imutils.resize(frame, width=300)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # detect faces in the image and then clone the frame
        # so that we can draw on it
        faceRects = fd.detect(gray, scaleFactor=1.1, minNeighbors=5,
                              minSize=(30, 30))
        frameClone = frame.copy()

        # loop over the face bounding boxes and draw them
        for (fX, fY, fW, fH) in faceRects:
            cv2.rectangle(frameClone, (fX, fY), (fX + fW, fY + fH), (0, 255, 0), 2)

        # show our detected faces
        cv2.imshow("Face", frameClone)

        # if the 'q' key is pressed, stop the loop
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    # cleanup the camera and close any open windows
    camera.release()
    cv2.destroyAllWindows()
