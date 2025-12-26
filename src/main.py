import cv2                 # Import OpenCV for image processing and GUI
import imageops as im      # Import custom image processing functions


def trackbarCallback(value):
    # Callback function required by OpenCV trackbars
    # The current trackbar value is passed automatically
    # We do not use it because we query trackbar values manually
    pass


def main():
    # Relative path to the input image (project root → assets)
    image_path = "assets/cute_kitten.jpg"

    # Load the image from disk
    image = cv2.imread(image_path)

    # Stop execution if the image failed to load
    if image is None:
        raise FileNotFoundError(f"Could not load image: {image_path}")

    # Name of the OpenCV control window
    windowName = "Edit"

    # Create an OpenCV window
    cv2.namedWindow(windowName)

    # Create trackbars for interactive control
    cv2.createTrackbar("Resize H", windowName, 50, 350, trackbarCallback)
    cv2.createTrackbar("Resize W", windowName, 50, 750, trackbarCallback)
    cv2.createTrackbar("Blur", windowName, 0, 25, trackbarCallback)
    cv2.createTrackbar("Threshold", windowName, 127, 255, trackbarCallback)
    cv2.createTrackbar("Rotate", windowName, 0, 360, trackbarCallback)

    # Main application loop (runs until user exits)
    while True:
        # Exit loop when the user presses the 'q' key
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

        # Read current values from each trackbar
        resize_h = cv2.getTrackbarPos("Resize H", windowName)
        resize_w = cv2.getTrackbarPos("Resize W", windowName)
        blur_val = cv2.getTrackbarPos("Blur", windowName)
        thresh_val = cv2.getTrackbarPos("Threshold", windowName)
        rotate_val = cv2.getTrackbarPos("Rotate", windowName)

        # Create a fresh copy of the original image
        processed_image = image.copy()

        # Apply resizing using width and height values
        processed_image = im.resize_image(processed_image, resize_w, resize_h)

        # Rotate the image by the selected angle
        processed_image = im.rotate_image(processed_image, rotate_val)

        # Apply blur with the selected kernel size
        processed_image = im.blur_image(processed_image, blur_val)

        # Apply binary thresholding
        processed_image = im.thresh_image(processed_image, thresh_val)

        # Display the processed image
        cv2.imshow("image editing toolkit", processed_image)

    # Close all OpenCV windows and release resources
    cv2.destroyAllWindows()


# Run the program only if this file is executed directly
if __name__ == "__main__":
    main()
