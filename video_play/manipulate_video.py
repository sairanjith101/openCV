import cv2

# Open a video file for reading
video_path = 'video/sample.mp4'
cap = cv2.VideoCapture(video_path)

# Check if the video opened successfully
if not cap.isOpened():
    print("Error: Couldn't open the video file.")
    exit()

# Create a video writer object for the output
output_path = 'video_path/demo3.mp4'
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(output_path, fourcc, 20.0, (640, 480))  # Adjust parameters as needed

# Read, resize, and write frames
while True:
    ret, frame = cap.read()

    # Break the loop if the video has ended
    if not ret:
        break

    # Resize the frame
    resized_frame = cv2.resize(frame, (640, 480))

    # Write the resized frame to the output video
    out.write(resized_frame)

    # Display the resized frame
    cv2.imshow('Resized Video Frame', resized_frame)

    # Break the loop if 'q' key is pressed
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

# Release video capture and writer objects, and close the window
cap.release()
out.release()
cv2.destroyAllWindows()
