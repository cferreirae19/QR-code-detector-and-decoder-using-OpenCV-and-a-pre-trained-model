# QR Detection

Three separate projects:

  ```
  -CV2 folder: it contains the QR detector based on OpenCV and pyzbar. More detailed instructions about it are included on its own readme file.
  -YOLO folder: it contains the QR detector based on a pre-trained model. More detailed instructions about it are included on its own readme file. It is highly suggested to use the detector+decoder version (i.e., the yolo-dbr-camera.py file).
  -QREADER folder: it contains a real time detector and decoder based on the Eric Cañas QReader project.
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

- Dynamsoft Barcode Reader

    ```
    pip install dbr
    ```
