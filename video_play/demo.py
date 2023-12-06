# if you want play the video actual size

import cv2
import numpy as np

# Create a VideoCapture object and read from input file
cap = cv2.VideoCapture('video/sample.mp4')

# Check if the video file opened successfully
if not cap.isOpened():
    print("Error opening video file")

# Get the original size of the video frames
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Create a window with the original size
cv2.namedWindow('Frame', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Frame', frame_width, frame_height)

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
