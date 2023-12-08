import cv2

cap = cv2.VideoCapture('video/sample.mp4')

if (cap.isOpened == False):
    print("Error! Video not open")
    
video_path = 'video_path/demo3.mp4'
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(video_path, fourcc, 20.0, (640,480))

while (cap.isOpened()):
    ret, frame = cap.read()
    if not ret:
        break
    resized_frame = cv2.resize(frame, (640,480))
    out.write(resized_frame)
    cv2.imshow('Resizesd_Frame', resized_frame)
    if cv2.waitKey(300) == ord('q'):
        break
    
cap.release()
out.release()
cv2.destroyAllWindows()

