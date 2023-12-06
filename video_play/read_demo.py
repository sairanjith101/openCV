import cv2

# Open a video file for reading
video_path = 'path/to/your/video.mp4'
cap = cv2.VideoCapture(video_path)

# Check if the video opened successfully
if not cap.isOpened():
    print("Error: Couldn't open the video file.")
    exit()

# Read and display frames from the video
while True:
    ret, frame = cap.read()

    # Break the loop if the video has ended
    if not ret:
        break

    # Display the frame
    cv2.imshow('Video Frame', frame)

    # Break the loop if 'q' key is pressed
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

# Release the video capture object and close the window
cap.release()
cv2.destroyAllWindows()
