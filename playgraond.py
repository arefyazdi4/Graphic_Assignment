import numpy as np
import scipy
import matplotlib
import cv2
import matplotlib.pyplot as plt
import matplotlib.style
from numpy import sin

if __name__ == '__main__':
    # Load the image and show some basic information on it
    image: np.ndarray = cv2.imread(r'A:/University/Term4/Graphic/Assignment/beach.png')
    cv2.imshow("Image", image)

    x = (1, 2, 3)
    y = (1, 4, 9)
    z = (1, 8, 27)
    plt.plot(x, y, color='b', marker='x', )  # market -≥ x,o,H , regular plot
    plt.bar(x, y)  # bar plot
    plt.pie(y, labels=x)  # circular

    plt.style.use('ggplot')  # pro mode,using a different lib for variant utility
    plt.title('square')
    plt.xlabel('n')
    plt.ylabel('n²')

    x = [i for i in np.range(0, 8, 0.1)]
    sin_x = [sin(i) for i in x]
    plt.show()


    x_axis = np.array([1, 2, 3, 4])
    y_axis = np.array([1, 4, 9, 16])
    plt.subplot(2, 2, 3)
    plt.plot(x_axis, y_axis)
    plt.subplot(2, 2, 2)
    plt.plot(x_axis, sin_x)
    plt.show()


