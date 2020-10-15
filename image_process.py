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

        grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        cv2.imshow('Grayscale', grayscale)

        return grayscale

    def nDegreeRotation(self, image, degree):
        """ NDEGREEROTATION FUNCTION """
        (rows,cols) = image.shape[:2]

        matrix = cv2.getRotationMatrix2D((cols/2, rows/2), degree, 1)
        rotation = cv2.warpAffine(image, matrix, (cols, rows))

        return rotation

    def rotation(self, image):
        """ ROTATION FUNCTION """
        degree = 45
        imageList = []

        while degree != 300:
            imageList.append(self.nDegreeRotation(image, degree)) 
            degree -= 15
            if(degree == -15):
                degree = 345

        return imageList

if __name__ == '__main__':
    sampleImage = cv2.imread("dataset_original/treadmill/treadmill_004.jpg")
    sampleGreyscaleImage = cv2.imread("dataset_original/dumbbell/dumbbell_004.jpg")

    print(sampleImage.shape)
    test = ImageProcess()

    # Square Test
    squared = test.square(sampleImage)

    # Grayscale Test
    grayscale = test.grayscale(sampleGreyscaleImage)

    # Rotation test
    rotation = test.rotation(sampleImage)

    cv2.imwrite("test_images/sample.jpg", squared)
    cv2.imwrite("test_images/grayscaled.jpg", grayscale)

    for index, image in enumerate(rotation):
        cv2.imwrite("test_images/rotation" + str(index) + ".jpg", image)
