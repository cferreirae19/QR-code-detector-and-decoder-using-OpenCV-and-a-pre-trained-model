import cv2
import numpy as np
from qreader import QReader

# Open the camera
capture = cv2.VideoCapture(0)

# Create a QReader instance
qreader = QReader()

if not capture.isOpened():
    print("Couldn't open the camera")
    exit()
    
while True:
    # Capture every frame
    ret, frame = capture.read()
    
    cv2.imshow("Detect QR Code from Webcam", frame)
    
    # Get the image that contains the QR code
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    if not ret:
        print("Couldn't read a frame")
        break
    
    # Use the detect_and_decode function to get the decoded QR data
    decoded_text = qreader.detect_and_decode(image=image, return_detections=True)
    if len(decoded_text[0]) != 0:
        bbox = decoded_text[1][0]['bbox_xyxy']
        start_point = (int(bbox[0]), int(bbox[1]))
        end_point = (int(bbox[2]), int(bbox[3]))
        cv2.rectangle(frame, start_point, end_point, (255, 0, 255), 3)
        cv2.imshow("Detect QR Code from Webcam", frame)
    
    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
capture.release()
cv2.destroyAllWindows()