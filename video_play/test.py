import cv2

# Open a video file for writing
output_path = 'video_1/demo.mp4'
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Use the default codec for MP4
out = cv2.VideoWriter(output_path, fourcc, 20.0, (640, 480))  # Adjust parameters as needed

# Generate frames (for demonstration purposes, you can replace this with actual frames)
for i in range(100):
    frame = cv2.putText(
        cv2.imread('image/1.jpg'), f'Frame {i}', (50, 50),
        cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA
    )

    # Resize the frame to match the specified dimensions
    frame = cv2.resize(frame, (640, 480))

    # Write the frame to the video file
    out.write(frame)

# Release the video writer object
out.release()
