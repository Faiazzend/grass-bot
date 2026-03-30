import cv2

def show(frame):
    cv2.imshow("debug", frame)
    cv2.waitKey(1)