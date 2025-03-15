import cv2
import numpy as np
from cropr import proc
cap = cv2.VideoCapture(0)
while True:
        frame = proc(cap)
        cv2.imshow('Live Video Stream', frame)
        if cv2.waitKey(1) == ord('w'):
            break
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
while True:
    adj = proc(cap)
    cv2.imshow('Make a move', adj)
    if cv2.waitKey(1) == ord('w'):
        break
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
newf = proc(cap)
diff = cv2.absdiff(frame,newf)

while True:
    cv2.imshow("diff",diff)
    if cv2.waitKey(1) == ord('k'):
        break
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()