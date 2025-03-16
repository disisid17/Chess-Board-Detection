import cv2
import numpy as np
from cropr import proc
from stock import make, besmove
def get_chessboard_square(x, y, width, height):
    square_width = width // 8
    square_height = height // 8
    col = x // square_width
    row = y // square_height
    return row, col
def retmo(diff):
    move=[]
    rowu = "87654321"
    colu = "abcdefgh"
    gray_diff = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    _, thresh_diff = cv2.threshold(gray_diff, 30, 255, cv2.THRESH_BINARY)

    # Find contours of the thresholded difference image
    contours, _ = cv2.findContours(thresh_diff, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    i = 0
    # Iterate through contours to find the grid cells with differences
    for con,contour in enumerate(contours):
        print(cv2.contourArea(contour))
        if cv2.contourArea(contour) > 1300 and cv2.contourArea(contour)<4000:  # Filter out small contours
            print("cont: " + str(con))
            x, y, w, h = cv2.boundingRect(contour)
            row, col = get_chessboard_square(x + w // 2, y + h // 2, frame_width, frame_height)
            print(f"Difference detected at row {row}, column {col}")
            toap = colu[col]+  rowu[row]
            if toap not in move:
                move.append(toap)
            i+=1 
           
    return move

            

cap = cv2.VideoCapture(0)
ex = False
frame_width = 800  # Width of the cropped frame
frame_height = 800  # Height of the cropped frame

while True:
    frame = proc(cap)
    cv2.imshow('Live Video Stream', frame)
    if cv2.waitKey(1) & 0xFF == ord('w'):
        break
    if cv2.waitKey(1) & 0xFF == ord('q'):
        ex = True
        break
while True:
    adj = proc(cap)
    cv2.imshow('Make a move', adj)
    if cv2.waitKey(1) & 0xFF == ord('r'):
        break
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
newf = proc(cap)
diff = cv2.absdiff(frame, newf)
cv2.imshow("diff", diff)
mover = retmo(diff)
print(mover)

while True:
    if cv2.waitKey(1) & 0xFF == ord('q'):
        ex = True
        break

cap.release()
cv2.destroyAllWindows()