# import the necessary packages
import cv2


class FaceDetector:
    # classifier is serialized as an XML file
    def __init__(self, faceCascadePath):
        # load the face detector
        # in order to build face recognition software, we have to
        # use the built-in Haar cascade classifiers in OpenCV
        # these classifiers have already been pre-trained to recognize faces
        self.faceCascade = cv2.CascadeClassifier(faceCascadePath)

    # deserialize the classifier, load it into memory
    def detect(self, image
               , scaleFactor=1.1  # How much the image size is reduced at each image scale
               , minNeighbors=5  # The cascade classifier will detect multiple
               # windows around a face. This parameter controls how
               # many rectangles (neighbors) need to be detected for
               # the window to be labeled a face
               , minSize=(30, 30)  # width and height (in pixels)
               # indicating the minimum size of the window. Bounding
               # boxes smaller than this size are ignored
               ):
        # detect faces in the image
        # return the rectangles representing bounding boxes around the faces
        # These bounding boxes are simply the (x, y) location
        # of the face, along with the width and height of the box
        rects = self.faceCascade.detectMultiScale(image,
                                                  scaleFactor=scaleFactor,
                                                  minNeighbors=minNeighbors,
                                                  minSize=minSize,
                                                  flags=cv2.CASCADE_SCALE_IMAGE)
        return rects
