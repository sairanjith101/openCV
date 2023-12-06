# write single image

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

'''
frame = cv2.putText(
    cv2.imread('image/1.jpg'),  # Read the image from the file 'image/1.jpg'
    f'Frame {i}',               # Text to be added to the image, where {i} is a variable placeholder
    (50, 50),                    # Position of the text (x, y) in the image
    cv2.FONT_HERSHEY_SIMPLEX,    # Font type (simplex in this case)
    1,                           # Font scale factor
    (255, 255, 255),             # Color of the text (in BGR format, white in this case)
    2,                           # Thickness of the text
    cv2.LINE_AA                  # Line type (anti-aliased line, smooth edges)
)
'''