import cv2              # OpenCV library for image processing
import numpy as np      # NumPy for numerical operations (used implicitly by OpenCV)


def resize_image(image, w, h):
    # Create a tuple representing the desired output size (width, height)
    dsize = (w, h)

    # Resize the input image to the specified dimensions
    resized_image = cv2.resize(image, dsize)

    # Return the resized image
    return resized_image


def rotate_image(image, rotation_value):
    # Extract the height and width of the image
    h, w = image.shape[:2]

    # Compute the center point of the image
    center = (w // 2, h // 2)

    # Create a rotation matrix using the center, angle, and scale factor
    T = cv2.getRotationMatrix2D(center, rotation_value, 1)

    # Apply the rotation transformation to the image
    rotated_image = cv2.warpAffine(image, T, (w, h))

    # Return the rotated image
    return rotated_image


def blur_image(image, ksize):
    # If kernel size is zero, return the original image (no blur)
    if ksize == 0:
        return image

    # Kernel size must be odd for blurring operations
    if ksize % 2 == 0:
        ksize += 1

    # Create a square kernel of size (ksize x ksize)
    kernel_size = (ksize, ksize)

    # Apply averaging blur to the image
    blurred_image = cv2.blur(image, kernel_size)

    # Return the blurred image
    return blurred_image


def thresh_image(image, thresh_value):
    # Convert the image from BGR color space to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply binary thresholding to the grayscale image
    _, thresh_img = cv2.threshold(gray_image,thresh_value,255,cv2.THRESH_BINARY)

    # Return the thresholded image
    return thresh_img
