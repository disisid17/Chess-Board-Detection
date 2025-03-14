import cv2

def crop_image(image):
    # Placeholder function to crop the image
    pass

def resize_image(image):
    # Placeholder function to resize the image
    pass

def main():
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open video stream.")
        return

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

if __name__ == "__main__":
    main()