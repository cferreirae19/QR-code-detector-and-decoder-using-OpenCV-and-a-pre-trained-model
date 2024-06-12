# QR Detection with OpenCV Python and pyzbar

Three separate files:

    - readingQR_cv2.py: detects the QR code, reads its data and draws a bounding box around it
    - openingWebcam_cv2.py: main function; starts a video capture and calls the detect_and_decode function from readingQR_cv2.py for every frame.
    - openingWebcam_file.py: same behavior as the previous one, but it loads an image from memory instead of starting a video recording.

## Installation

- OpenCV 
    
    ```
    pip install opencv-python
    ```

- pyzbar

    ```
    pip install pyzbar
    ```

## Usage

2 different modes:

    - Webcam: python3 openingWebcam_cv2.py

    - Load an image: python3 openingWebcam_file.py

## References
- https://docs.opencv.org/3.4/d6/d00/tutorial_py_root.html
- https://pypi.org/project/pyzbar/
