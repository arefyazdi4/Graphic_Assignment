import cv2 as cv
import numpy as np

if __name__ == '__main__':

    # creat central circles
    canvas_central_circle = np.zeros((300, 300, 3), dtype='uint8')
    center_canvas_central_circle = (center_x, center_y) = (canvas_central_circle.shape[0] // 2,
                                                           canvas_central_circle.shape[1] // 2)
    white_rgb = (255, 255, 255)
    for radius_var in range(5, 140, 8):
        cv.circle(img=canvas_central_circle, center=center_canvas_central_circle, radius=radius_var, thickness=1,
                  color=(30 + radius_var, 255 - radius_var * 1.4, 70 + radius_var / 2))
    cv.imshow('canvas_central_circle', canvas_central_circle)

    # creat a random circles
    canvas_random_circle = np.zeros((300, 300, 3), dtype='uint8')
    for i in range(5, 140, 8):
        radius_var = np.random.randint(low=5, high=140)
        color_var = np.random.randint(low=0, high=255, size=(3,)).tolist()
        center_var = np.random.randint(low=0, high=300, size=(2,)).tolist()
        cv.circle(canvas_random_circle, center=center_var, radius=radius_var, color=color_var)
    cv.imshow("canvas_random_circle", canvas_random_circle)

    # image transformation
    image: np.ndarray = cv.imread(r'A:/University/Term4/Graphic/Assignment/trex.png')

    # image resize
    image_resize = cv.resize(src=image, dsize=(0, 0), fx=0.5, fy=0.5)
    cv.imshow('image_resize', image_resize)

    # image shift
    trance_matrix = np.array([[1, 0, 25], [0, 1, 25]], dtype=float)
    image_shifted = cv.warpAffine(src=image, M=trance_matrix, dsize=(image.shape[1], image.shape[0]))
    cv.imshow('image_shifted_down_right', image_shifted)

    # image trance or you can creat manual function for this
    # image rotate
    center_image = (image.shape[0] // 2, image.shape[1] // 2)
    rotation_matrix = cv.getRotationMatrix2D(center=center_image, angle=45, scale=1.0)
    print(rotation_matrix)
    image_rotated = cv.warpAffine(image, rotation_matrix, (image.shape[1], image.shape[0]))
    cv.imshow('image_rotated', image_rotated)
    cv.waitKey(0)
    cv.destroyAllWindows()
