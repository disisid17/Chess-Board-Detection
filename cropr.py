import cv2
def main():
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open video stream.")
        return

    while True:
        frame = proc(cap)
        # Call the crop and resize functions (currently do nothing)
        cv2.imshow('Live Video Stream', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

def proc(cap):
    ret, frame = cap.read()
    frame = frame[140:940,590:1390]
    frame = cv2.rotate(frame, cv2.ROTATE_180)
    return frame
if __name__ == "__main__":
    main()