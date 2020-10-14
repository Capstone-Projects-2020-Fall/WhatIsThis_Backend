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
        resized = cv2. resize(image, (300, 300))
        return resized

    def square(self, image):
        """ SQURE FUNCTION """
        height = image.shape[0]
        width  = image.shape[1]
        white = [255, 255, 255]

        if height != width:
            if height > width:
                dif = height - width
                squared = cv2.copyMakeBorder(image, 0, 0, int(dif/2), int(dif/2), cv2.BORDER_CONSTANT, value=white)
                # print(squared.shape)
                return squared 
            else:
                dif = width - height
                squared = cv2.copyMakeBorder(image, int(dif/2), int(dif/2), 0, 0, cv2.BORDER_CONSTANT, value=white)
                # print(squared.shape)
                return squared
        else:
            return image

    def grayscale(self, image):
        """ GRAYSCALE FUNCTION """

    def rotation(self, image):
        """ ROTATION FUNCTION """


if __name__ == '__main__':
    sampleImage = cv2.imread("dataset_original/treadmill/treadmill_004.jpg")
    print(sampleImage.shape)
    test = ImageProcess()

    # Square Test
    squared = test.square(sampleImage)
    cv2.imwrite("sample.jpg", squared)
