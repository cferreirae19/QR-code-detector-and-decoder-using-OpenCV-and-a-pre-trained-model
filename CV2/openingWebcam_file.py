import cv2 as cv
import readingQR_cv2 as rd

img = cv.imread("TestImage1.jpg")
    
rd.detect_and_decode(img)

cv.waitKey()

cv.destroyAllWindows()