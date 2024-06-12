import cv2
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
    
    # Get the image that contains the QR code
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    if not ret:
        print("Couldn't read a frame")
        break
    
    # Use the detect_and_decode function to get the decoded QR data
    decoded_text = qreader.detect_and_decode(image=image)
    if len(decoded_text) != 0:
        print(decoded_text)
    
    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
capture.release()
cv2.destroyAllWindows()