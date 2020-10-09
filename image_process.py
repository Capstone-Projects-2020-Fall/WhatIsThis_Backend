"""
---------------------------------------------------------------------------
                            PROGRAM DISCRIPTION
---------------------------------------------------------------------------
This program will be responsible for preprocessing input images to increase
the accuracy of the image recognition and shorten the execution time.
The open source library OpenCV is used for the image processing.
"""
from cv2 import cv2

class ImageProcess:
    """ IMAGE PROCESS CLASS """

    def resize(self, image):
        """ RESIZE FUNCTION """

    def square(self, image):
        """ SQURE FUNCTION """

    def grayscale(self, image):
        """ GRAYSCALE FUNCTION """


if __name__ == '__main__':
    sampleImage = cv2.imread("dataset_original/treadmill/treadmill_001.jpg")
    print(sampleImage.shape)
