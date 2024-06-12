import cv2 as cv
import readingQR_cv2 as rd

# Open the camera
capture = cv.VideoCapture(0)

if not capture.isOpened():
    print("Couldn't open the camera")
    exit()
    
while True:
    # Capture every frame
    ret, frame = capture.read()
    
    if not ret:
        print("Couldn't read a frame")
        break
    
    rd.detect_and_decode(frame)
    
    # Press 'q' to quit
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
    
capture.release()
cv.destroyAllWindows()