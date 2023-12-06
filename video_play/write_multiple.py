import cv2
import os
import time

# Open a video file for writing
output_path = 'video_1/demo_2.mp4'
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Use the default codec for MP4
fps = 1.0 # Adjust the frame rate as needed (e.g., reduce to slow down playback)
out = cv2.VideoWriter(output_path, fourcc, fps, (640, 480))  # Adjust parameters as needed

# List of image paths
image_paths = ['image/1.jpg', 'image/2.jpg', 'image/3.jpg', 'image/4.jpg', 'image/5.jpg']  # Add more image paths as needed

# Generate frames using multiple images
for i, image_path in enumerate(image_paths):
    if os.path.exists(image_path):
        frame = cv2.putText(
            cv2.imread(image_path), f'Frame {i}', (50, 50),
            cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA
        )

        # Resize the frame to match the specified dimensions
        frame = cv2.resize(frame, (640, 480))

        # Write the frame to the video file
        out.write(frame)

        # Introduce a delay (100 milliseconds in this example)
        time.sleep(0.1)
    else:
        print(f"Image not found: {image_path}")

# Release the video writer object
out.release()
