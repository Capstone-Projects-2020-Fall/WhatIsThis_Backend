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

# Flask Modules
from flask import Flask, request, Response

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
    """
        RECEIVING JSON FORMAT:
        {
            "image_name" : "XXXX.jpg"
            "data" : "BASE64_STRING_IMAGE_DATA"
        }
    """
    # Extract infomation from the JSON
    name = request.json.get('image_name')
    data = request.json.get('data')
    path = "containerized/temp/" + name
    # Decode the BASE64 image and save it into the temp file
    imgdata = base64.b64decode(str(data))
    image = Image.open(BytesIO(imgdata))
    img = cv2.cvtColor(np.array(image), cv2.COLOR_BGR2RGB)
    cv2.imwrite(path, img)
    # Call the image recognition function
    predictor = classifier.Classifier()
    predicted_label = predictor.image_recognition(path)
    print(predicted_label)

    return Response(status=200)
if __name__ == "__main__":
    app.run(port=8080, threaded=True)