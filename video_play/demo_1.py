# If you want video size enter manually

import cv2
import numpy as np

# Create a VideoCapture object and read from input file
cap = cv2.VideoCapture('video/sample.mp4')

# Check if the video file opened successfully
if not cap.isOpened():
    print("Error opening video file")

# Manually specify the desired size of the video frames
desired_width = 640  # replace with your desired width
desired_height = 480  # replace with your desired height

# Create a window with the specified size
cv2.namedWindow('Frame', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Frame', desired_width, desired_height)

# Read until the video is completed
while cap.isOpened():
    # Capture frame-by-frame
    ret, frame = cap.read()
    if ret:
        # Display the resulting frame
        cv2.imshow('Frame', frame)

        # Press Q on keyboard to exit
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    else:
        break

# Release the video capture object
cap.release()

# Closes all the frames
cv2.destroyAllWindows()
