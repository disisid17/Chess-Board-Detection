import cv2
import numpy as np
from cropr import proc
from stock import *
import os
import time
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
    for contour in contours:
        print(cv2.contourArea(contour))
        if cv2.contourArea(contour) > 600 and cv2.contourArea(contour)<5000:  # Filter out small contours
            print(cv2.contourArea(contour))
            x, y, w, h = cv2.boundingRect(contour)
            row, col = get_chessboard_square(x + w // 2, y + h // 2, frame_width, frame_height)
            print(f"Difference detected at row {row}, column {col}")
            toap = colu[col] + rowu[row]
            if toap not in move:
                move.append(toap)
                i+=1 
    print(move)    
    return move

            

cap = cv2.VideoCapture(0)
ex = False
frame_width = 800  # Width of the cropped frame
frame_height = 800  # Height of the cropped frame
#setfen("r1bqk2r/ppp2ppp/2n5/4p3/1bP5/3P1N2/PPQ1nPPP/R1B1K2R w KQkq - 0 9")
while True:
    print("align your move")
    while True:
        frame = proc(cap)
        cv2.imshow('Live Video Stream', frame)
        if cv2.waitKey(1) & 0xFF == ord('w'):
            break
        if cv2.waitKey(1) & 0xFF == ord('q'):
            ex = True
            break
    cv2.destroyAllWindows()
    os.system('say \"{}\"'.format("make your move"))
    print("Make your move")
    while True:
        adj = proc(cap)
        cv2.imshow('Make a move', adj)
        if cv2.waitKey(1) & 0xFF == ord('w'):
            break
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cv2.destroyAllWindows()
    newf = proc(cap)
    diff = cv2.absdiff(frame, newf)
    #cv2.imshow("diff", diff)
    mover = retmo(diff)
    fir = 0
    if val(mover[0]):
        fir = mover[0]+mover[1]
    else:
        fir = mover[1]+mover[0]
    print(fir)
    text = "White moves :" + str(fir)
    os.system('say \"{}\"'.format(text))
    make(fir)
    #time.sleep(1)
    moveds = besmove()
    text = "Black moves :" + str(moveds)
    os.system('say \"{}\"'.format(text))
    print(moveds)
    print(reboard())
    print(besmove(False))
    print(fenot())
    print(eva()[0])
    if eva()[1]:
        os.system('say \"{}\"'.format("Black checkmate"))
        print("Game Over")
        break
# while True:
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         ex = True
#         break

# cap.release()
# cv2.destroyAllWindows()