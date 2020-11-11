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
import requests
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
            "data" : "BASE64_STRING_IMAGE_DATA"
        }
    """
    # Extract infomation from the JSON
    data = request.json.get('data')
    path = "containerized/temp/test.jpg"
    # Decode the BASE64 image and save it into the temp file
    imgdata = base64.b64decode(str(data))
    image = Image.open(BytesIO(imgdata))
    img = cv2.cvtColor(np.array(image), cv2.COLOR_BGR2RGB)
    cv2.imwrite(path, img)

    r = requests.post(
        'https://api.remove.bg/v1.0/removebg',
        files={'image_file': open('containerized/temp/test.jpg', 'rb')},
        data={'size': 'auto', 'bg_color': 'white'},
        headers={'X-Api-Key': 'TR4kRBeFb6Uwfwg3Q8yPS1Ss'},
    )
    if r.status_code == requests.codes.ok:
        with open('containerized/temp/test.png', 'wb') as out:
            out.write(r.content)
    else:
        print("Error:", r.status_code, r.text)

    # Call the image recognition function
    predictor = classifier.Classifier()
    predicted_label = predictor.image_recognition('containerized/temp/test.png')
    print(predicted_label)

    return Response(status=200)
if __name__ == "__main__":
    app.run(port=8080, threaded=True)