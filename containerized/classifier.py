"""
---------------------------------------------------------------------------
                            PROGRAM DISCRIPTION
---------------------------------------------------------------------------
This function will be responsible for creating the machine learning model
and predicting the type of a training equipment in a submitted image.
"""
import image_process
import numpy as np
import os
import keras
import cv2
import requests
from sklearn.model_selection import train_test_split
from keras.preprocessing import image
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPooling2D
from keras.optimizers import Adam

""" PATHING VARIABLES """
""" Either ./containerized or ./ is the root directory """ 

current_directory = os.getcwd()

if 'containerized' not in current_directory :
    DIRECTORY_PATH = current_directory + '/containerized'
    
class Classifier:
    """ CLASSIFIER CLASS """

    def data_split(self):
        """ SPLIT DATA FUNCTION """
        # Parameters
        input_shape = (150, 150, 3)
        labels = os.listdir("dataset")
        num_classes = len(os.listdir("dataset"))
        # array of x (images) and y (labels)
        x = []
        y = []
        # load dataset and store them in the arraies
        for i in range(len(labels)):
                pics = os.listdir(f"dataset/{labels[i]}")
                for j in range(len(pics)):
                    path = f"dataset/{labels[i]}/{pics[j]}"
                    x.append(image.img_to_array(image.load_img(path, target_size=input_shape[:2])))
                    y.append(i)
        # Convert to nparray and normalize
        x = np.asanyarray(x)
        x /= 255
        y = np.asanyarray(y)
        y = keras.utils.to_categorical(y, num_classes)
        # Split Data
        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=3)
        return x_train, x_test, y_train, y_test, input_shape, num_classes

    def crate_model(self, input_shape, num_classes):
        """ CREATE MODEL FUNCTION """
        # Create machine learning model
        model = Sequential()
        model.add(Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=input_shape))
        model.add(Conv2D(64, (3, 3), activation='relu'))
        model.add(MaxPooling2D(pool_size=(2, 2)))
        model.add(Dropout(0.125))
        model.add(Flatten())
        model.add(Dense(128, activation='relu'))
        model.add(Dropout(0.25))
        model.add(Dense(num_classes, activation='softmax'))
        model.compile(loss=keras.losses.categorical_crossentropy, optimizer=Adam(lr=0.000005), metrics=['accuracy'])
        return model

    def evaluate_accuracy(self, model, x_train, x_test, y_train, y_test, batch_size, epochs):
        """ EVALUATE ACCURACY FUNCTION """
        # Train and evaluate the accuracy in each epoch
        model.fit(x_train, y_train,
            batch_size=batch_size,
            epochs=epochs,
            verbose=1,
            validation_data=(x_test, y_test)
        )

    def image_recognition(self, path):
        """ IMAGE RECOGNITION FUNCTION """
        model = keras.models.load_model(DIRECTORY_PATH + "/model/demo2_1_model.h5")
        img_proc = image_process.ImageProcess()

        img = cv2.imread(path)
        img = img_proc.square(img)
        img = img_proc.grayscale(img)
        img = img_proc.resize(img)
        cv2.imwrite(DIRECTORY_PATH + "/temp/target.jpg", img)

        target_image= []
        input_shape = (150, 150, 3)

        target_image.append(image.img_to_array(image.load_img( DIRECTORY_PATH + "/temp/target.jpg", target_size=input_shape[:2])))
        target_image = np.asanyarray(target_image)
        target_image /= 255

        acc = model.predict(target_image)
        
        return acc


    def save_model(self, model):
        """ SAVE MODEL FUNCTION """
        model.save("demo1_model.h5")

if __name__ == '__main__':
    classifier_test = Classifier()
    """
    x_train, x_test, y_train, y_test, input_shape, num_classes = classifier_test.data_split()
    model = classifier_test.crate_model(input_shape, num_classes)
    classifier_test.evaluate_accuracy(model, x_train, x_test, y_train, y_test, 32, 20)
    """

    accuracy_matrix = classifier_test.image_recognition("dataset/treadmill/treadmill_34.jpg")
    print(accuracy_matrix)
    
