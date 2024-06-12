# QR Detection with OpenCV Python and pyzbar

Two separate files:

    ```
    - readingQR_cv2.py: detects the QR code, reads its data and draws a bounding box around it
    - openingWebcam_cv2.py: main function; starts a video capture and calls the detect_and_decode function from readingQR_cv2.py for every frame.
    ```

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

python3 openingWebcam_cv2.py

## References
- https://docs.opencv.org/3.4/d6/d00/tutorial_py_root.html
- https://pypi.org/project/pyzbar/
