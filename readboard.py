import cv2
import numpy as np

cap = cv2.VideoCapture(0)
while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Failed to capture image.")
            break
        frame = frame[145:930,595:1380]
        # Call the crop and resize functions (currently do nothing)
        cropped_frame = crop_image(frame)
        

        cv2.imshow('Live Video Stream', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()