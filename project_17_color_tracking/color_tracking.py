# USAGE
# python color_tracking.py --video video/iphonecase.mov

# import the necessary packages
import numpy as np
import time
import cv2

if __name__ == '__main__':

    # define the upper and lower boundaries for a color
    # to be considered "orange_boundary"
    orange_lower = np.array([5, 80, 140], dtype="uint8")
    orange_upper = np.array([80, 140, 255], dtype="uint8")

    # load the video
    camera = cv2.VideoCapture(0)

    # keep looping
    while True:
        # grab the current frame
        # grabbed, is a boolean indicating whether or not the frame was successfully read from the video file
        (grabbed, frame) = camera.read()

        # determine which pixels fall within the orange_boundary boundaries
        # within the upper and lower range set to white and
        # pixels that do not fall into this range set as black
        orange_boundary = cv2.inRange(src=frame, lowerb=orange_lower, upperb=orange_upper)
        # and then blur the binary image
        # to finding  contours  more  accurate
        orange_boundary = cv2.GaussianBlur(src=orange_boundary, ksize=(3, 3), sigmaX=0)

        # find contours in the image
        (contours, _) = cv2.findContours(orange_boundary.copy(), cv2.RETR_EXTERNAL,
                                         cv2.CHAIN_APPROX_SIMPLE)

        # check to see if any contours were found
        if len(contours) > 0:
            # sort the contours and find the largest one -- we
            # will assume this contour corresponds to the area
            # of my phone
            biggest_contour = sorted(contours, key=cv2.contourArea, reverse=True)[0]

            # compute the (rotated) bounding box around then
            # contour and then draw it
            # minAreaRect computes the minimum bounding box around the contour
            # boxPoints re-shapes the bounding box to be a list of points
            rect = np.int32(cv2.boxPoints(cv2.minAreaRect(biggest_contour)))
            cv2.drawContours(image=frame, contours=[rect], contourIdx=-1, color=(0, 255, 0), thickness=2)

        # show the frame and the binary image
        cv2.imshow("Tracking", frame)
        cv2.imshow("Binary", orange_boundary)

        time.sleep(0.025)

        # if the 'q' key is pressed, stop the loop
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    # cleanup the camera and close any open windows
    camera.release()
    cv2.destroyAllWindows()
