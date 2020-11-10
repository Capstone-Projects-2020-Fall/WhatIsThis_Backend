#!usr/bin/env python

"""
---------------------------------------------------------------------------------------------------
                                        PROGRAM DESCRIPTION
---------------------------------------------------------------------------------------------------
    This file is meant to act as the server running with the docker container. It should contain
    all the necessary files, models, and other libraries needed to run the model. This should
    be designed to work cross platform, on windows/linux/and mac.
"""

# System Modules
import os 
import sys
import base64
from io import BytesIO
from PIL import Image
from cv2 import cv2
import numpy as np
import image_process
import classifier
import tensorflow as tf

# Flask Modules
from flask import Flask, request, Response
from werkzeug.datastructures import FileStorage


# Variables
MODEL_DIR = os.path.join(os.getcwd(), "model")


"""
    Main program is located here. Responsible for handling the requests and sending 
    a response to the client
"""

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    """ PREDICT THE POTENTIAL PIECE OF EQUIPMENT BASED ON THE REQUEST """
    name = request.json.get('image_name')
    data = request.json.get('data')
    path = "temp/" + name

    imgdata = base64.b64decode(str(data))
    image = Image.open(BytesIO(imgdata))
    img = cv2.cvtColor(np.array(image), cv2.COLOR_BGR2RGB)
    cv2.imwrite(path, img)

    predictor = classifier.Classifier()
    predicted_label = predictor.image_recognition(path)
    print(predicted_label)

    # Process the request, if necessary

    # Run the image recognition model 

    # Construct the response

    # Return the response
    return Response(status=200)
if __name__ == "__main__":
    app.run(port=8080, threaded=True)