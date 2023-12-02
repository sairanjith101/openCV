import cv2
import numpy as np

video = cv2.VideoCapture('video/sample.mp4')

if video.isOpened() == False:
    print('Error! video file not open')

while True:
    if video.isOpened():
        ret, frame = video.read()
        if ret == True:
            cv2.imshow('frame', frame)

            if cv2.waitKey(25) == ord('q'):
                break
    
    else:
        break

video.release()

cv2.destroyAllWindows()