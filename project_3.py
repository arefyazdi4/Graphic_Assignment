import cv2
import numpy as np

if __name__ == '__main__':
    # Load the image and show some basic information on it
    image: np.ndarray = cv2.imread(r'A:/University/Term4/Graphic/Assignment/beach.png')
    print(image.shape[0], image.shape[1])
    image_red_box = image.copy()
    image_red_box[50:140, 30:100] = (128, 0, 128)
    cv2.imshow('image', image_red_box)

    canvas = np.zeros((300, 300, 3), dtype='uint8')
    # cv2.line(canvas, (2, 3), (100, 120), (9, 200, 40), thickness=7)
    cv2.rectangle(canvas, (70, 250), (110, 50), (16, 16, 131), thickness=-1)
    cv2.rectangle(canvas, (190, 250), (230, 50), (16, 16, 131), thickness=-1)
    polygon = np.array([[70, 50], [110, 50], [230, 250], [190, 250]])
    polygon = polygon.reshape((-1, 1, 2))
    cv2.fillPoly(canvas, [polygon], (20, 9, 229))

    cv2.imshow('canvas', canvas)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
